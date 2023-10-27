from motor_controller_interface import MotorControllerInterface
from odrive_can.msg import ControllerStatus, ControlMessage, ODriveStatus
from odrive_can.srv import AxisState as AxisStateService
from odrive.enums import AxisState, ControlMode, InputMode
from dataclasses import dataclass
from rclpy.node import Node
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.task import Future
from motor_controller_utils import rps_to_rpm, rpm_to_rps
from contextlib import contextmanager
import time
#import lgpio # raspberry ubuntu gpio package

DEFAULT_QOS = 10
MAGNETIC_BRAKE_PIN = 22 #TS

# TODO create generic motor error class
# TODO must use try except in higher implementation to catch motor errors
# TODO: raise error if unable to complete request, and catch and deal with error in higher logic

@dataclass
class OdriveTelemetry:
    def __init__(self):
        self.position_cycles = 0.0
        self.velocity_rpm = 0.0
        self.torque_target = 0.0
        self.torque_estimate = 0.0
        self.iq_setpoint = 0.0
        self.iq_measured = 0.0
        self.active_errors = 0
        self.axis_state = 0
        self.procedure_result = 0
        self.trajectory_done_flag = False
        self.bus_voltage = 0.0
        self.bus_current = 0.0
        self.fet_temperature = 0.0
        self.motor_temperature = 0.0
        self.active_errors = 0
        self.disarm_reason = 0

        self.is_brake_locked = False


class OdriveController(MotorControllerInterface):
    NOMINAL_ODRIVE_STATES = [AxisState.IDLE, AxisState.CLOSED_LOOP_CONTROL]

    def __init__(self, node: Node):
        # init class attributes
        self.node = node
        self.telemetry = OdriveTelemetry()
        
        # init ros interfaces
        self._odrive_status_subscriber = self.node.create_subscription(ODriveStatus, "odrive_status", self._odrive_status_subscriber_callback, DEFAULT_QOS, callback_group=ReentrantCallbackGroup())
        self._controller_status_subscriber = self.node.create_subscription(ControllerStatus, "controller_status", self._controller_status_subscriber_callback, DEFAULT_QOS, callback_group=ReentrantCallbackGroup())
        self._control_message_publisher = self.node.create_publisher(ControlMessage, "control_message", DEFAULT_QOS)
        self._axis_state_service_client = self.node.create_client(AxisStateService, "request_axis_state", callback_group=ReentrantCallbackGroup())

        # init brake gpio pin
        # self._gpio_controller = lgpio.gpiochip_open(0)
        # self._magnetic_brake_gpio_pin = lgpio.gpio_claim_output(self._gpio_controller, MAGNETIC_BRAKE_PIN)

    async def roll_position(self, requested_position_cycles: float):
        # TODO: idea - define a minimum average travel velocity and check if since start_time the actual average velocity is larger
        async with self._closed_loop_control:
           with self._open_brake:
                self._publish_position_command(requested_position_cycles=requested_position_cycles)
                await self._reach_requested_position(requested_position_cycles)

    # TODO - idea: estimate the time needed to reach the requested position and add a timeout
    async def _reach_requested_position(self, requested_position_cycles):
        # TODO: move final position margin of error to external variable
        while True:
            await self._async_ros_sleep(0.1)
            if abs(self.telemetry.position_cycles - requested_position_cycles) < 1:
                break

    async def roll_velocity(self, requested_velocity_rpm: float):
        await self._request_axis_state(AxisState.CLOSED_LOOP_CONTROL)
        self.set_brake_state(is_brake_locked=False)
        self._publish_velocity_command(requested_velocity_rpm=requested_velocity_rpm)

    async def roll_duty(self, duty_cycle: float):
        pass
               

    async def calibrate(self):
        await self._request_axis_state(AxisState.FULL_CALIBRATION_SEQUENCE)
        # TODO return if successful or not

    async def abort(self):
        if self.telemetry.axis_state == AxisState.IDLE:
            return
        
        self._publish_velocity_command(requested_velocity_rpm=0)
        await self._reach_complete_stop()
        self.set_brake_state(is_brake_locked=True)
        await self._request_axis_state(AxisState.IDLE)

    async def _reach_complete_stop(self):
        # TODO: add a slow_to_stop_timeout that sends the command again if there is no deceleration or not reaching stop in allowed time
        # TODO: move the minimum brake speed to an external variable
        while True:
            await self._async_ros_sleep(0.1)
            if abs(self.telemetry.velocity_rpm) < 10: # or (time.time() - start_time) < operation timeout
                break
        
    
    def reset_cycles(self, position_cycles: float):
        pass

    def set_brake_state(self, is_brake_locked: bool):
        pass
        #lgpio.gpio_write(self._gpio_controller, self._magnetic_brake_gpio_pin, int(is_brake_locked))

    
    @contextmanager
    async def _closed_loop_control(self):
        await self._request_axis_state(AxisState.CLOSED_LOOP_CONTROL)
        yield

        await self._request_axis_state(AxisState.IDLE)

    @contextmanager
    def _open_brake(self):
        # WARNING! YOU MUST USE CLOSED LOOP CONTROL BEFORE BRAKE!
        if self.telemetry.is_brake_locked:
            self.set_brake_state(is_brake_locked=False)
        yield

        self.set_brake_state(is_brake_locked=True)

    def _async_ros_sleep(self, time_seconds: float) -> Future:
        self._sleep_future = Future()
        self._end_sleep_timer = self.node.create_timer(time_seconds, self._end_sleep_timer_callback)
        return self._sleep_future

    def _end_sleep_timer_callback(self):
        self._sleep_future.done()
        self._end_sleep_timer.cancel()

    async def _request_axis_state(self, requested_state: AxisState) -> AxisStateService.Response:
        # TODO: add timeout
        # TODO check for returned axis errors
        # TODO!!! CHECK WHEN THE SERVICE RETURNS??? DOES IT WAIT FOR THE STATE CHANGE TO COMPLETE???
        if self.telemetry.axis_state not in self.NOMINAL_ODRIVE_STATES:
            raise MotorControllerError # TODO add error type
        if self.telemetry.axis_state != requested_state:
            axis_state_service_request = AxisStateService.Request(axis_requested_state=AxisState.CLOSED_LOOP_CONTROL)
            await self._axis_state_service_client.call_async(axis_state_service_request)
    
    def _publish_velocity_command(self, requested_velocity_rpm: float):
        velocity_command = ControlMessage(control_mode = ControlMode.VELOCITY_CONTROL, input_mode = InputMode.VEL_RAMP)
        velocity_command.input_vel = rpm_to_rps(requested_velocity_rpm)
        self._control_message_publisher.publish(velocity_command)

    def _publish_position_command(self, requested_position_cycles: float):
        position_command = ControlMessage(control_mode = ControlMode.POSITION_CONTROL, input_mode = InputMode.TRAP_TRAJ)
        position_command.input_pos = requested_position_cycles
        self._control_message_publisher.publish(position_command)

    def _odrive_status_subscriber_callback(self, msg: ODriveStatus):
        self.telemetry.bus_voltage = msg.bus_voltage
        self.telemetry.bus_current = msg.bus_current
        self.telemetry.fet_temperature = msg.fet_temperature
        self.telemetry.motor_temperature = msg.motor_temperature
        self.telemetry.active_errors = msg.active_errors
        self.telemetry.disarm_reason = msg.disarm_reason

    def _controller_status_subscriber_callback(self, msg: ControllerStatus):
        self.telemetry.position_cycles = msg.pos_estimate
        self.telemetry.velocity_rpm = rps_to_rpm(msg.vel_estimate)
        self.telemetry.torque_target = msg.torque_target
        self.telemetry.torque_estimate = msg.torque_estimate
        self.telemetry.iq_setpoint = msg.iq_setpoint
        self.telemetry.iq_measured = msg.iq_measured
        self.telemetry.active_errors = msg.active_errors
        self.telemetry.axis_state = msg.axis_state
        self.telemetry.procedure_result = msg.procedure_result
        self.telemetry.trajectory_done_flag = msg.trajectory_done_flag

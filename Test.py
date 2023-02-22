


import numpy
import odrive
import time
import math

#add: create section for odrive motor parameters or import robot parameters from file

class actuator:
    #create a list of actuators for ease of for loop
    list = []

    def __init__(self, odrive_unit, odrive_port, angle, distance):
        actuator.odrive_unit = odrive_unit
        actuator.odrive_port = odrive_port
        actuator.angle = angle
        actuator.distance = distance
        actuator.list.append(self)
        
    def check_state(odrive_unit, odrive_port):
        return odrive_unit.odrive_port.current_state

    def request_state(odrive_unit, odrive_port, requested_state):
         odrive_unit.odrive_port.requested_state = requested_state

    def startup():
        print("starting calibration...")
        #calibrate
        for joint in actuator.list:
            joint.request_state(joint.odrive_unit, joint.odrive_port, "AXIS_STATE_FULL_CALIBRATION_SEQUENCE")
        
        #checks if calibration is complete
        for joint in actuator.list:
            while joint.check_state(joint.odrive_unit, joint.odrive_port) != "AXIS_STATE_IDLE":
                time.sleep(0.1)
            joint.request_state(joint.odrive_unit, joint.odrive_port, "AXIS_STATE_CLOSED_LOOP_CONTROL")
        print("calibration complete")

    def home():
        #move actuators to home position
        pass

    def move(current_angle, requested_angle):
        #odrive command to requested angle
        pass

class motor:

class encoder:















def request_position():
    #need fix - make sure that height and redius is inside circle
    #need fix - make option to use coordinates
    while True:
       requested_angle = input("Please provide the requested angle between 0 and 360: ")
       if 0 < requested_angle < 360:
           break
    while True:
       requested_redius = input("Please provide the requested redius between 0 and 3000 mm: ")
       if 0 < requested_redius < 3000:
           break
        
    while True:
       requested_height = input("Please provide the requested height between 0 and 360: ")
       if 0 < requested_height < 360:
           break
    return requested_angle, requested_redius, requested_height

def calc_angles(requested_angle, requested_radius, requested_height):
    #fix - include min angle to avoid collision
    requested_angle_list = []
    requested_angle_list.append(requested_angle)
                                                                     


    return [angle list]
    pass

def update_position():
    for joint in actuator.list:
        #read joint encoder position between 0 and 360, perhaps use odrive 2nd avilable encoder to make reading easier
        encoder_angle = 0.0
        joint.angle = encoder_angle

def main():
    print("Welcome to the robot arm controller :)")

    #define odrive serial numbers
    odrive_serial0 = "1234"
    #odrive_serial1 = "1234"

    #connect to odrive
    odrive0 = odrive.find_any(serial_number = odrive_serial0)
    #odrive1 = odrive.find_any(serial_number = odrive_serial1)
    #add: print connected message

    #init actuator parameters: odrive unit, odrive port number, axis angle, axis distance to next axis
    actuator0 = actuator(odrive0, "axis0", 0, 20)
    #actuator1 = actuator(odrive0, "axis1", 0, 150)
    #actuator2 = actuator(odrive1, "axis0", 0, 150)

    #calibrate all axis
    actuator.startup()

    #update actuator position
    update_position()

    #home all axis
    actuator.home()


    while True:
        requested_angle, requested_radius, requested_height = request_position()
        requested_angle_list = calc_angles(requested_angle, requested_radius, requested_height)
        actuator.move(current angle list, requested angle list)


if __name__ == "__main__":
    main()




odrv0.axis0.motor.config.current_lim = 10 #To change the current limit
odrv0.axis0.controller.config.vel_limit = 2 #The motor will be limited to this speed in [turn/s]

odrv0.config.enable_brake_resistor = False #Set this to True if using a brake resistor
odrv0.config.brake_resistance = 200 #This is the resistance [Ohms] of the brake resistor
odrv0.config.dc_max_negative_current = 1 #This is the amount of current [Amps] allowed to flow back into the power supply

odrv0.axis0.motor.config.pole_pairs #This is the number of magnet poles in the rotor, divided by two. To find this, you can simply count the number of permanent magnets in the rotor.
odrv0.axis0.motor.config.torque_constant #This is the ratio of torque produced by the motor per Amp of current delivered to the motor. This should be set to 8.27 / (motor KV).
odrv0.axis0.motor.config.motor_type #This is the type of motor being used. Currently two types of motors are supported: High-current motors (MOTOR_TYPE_HIGH_CURRENT, [0]) and gimbal motors (MOTOR_TYPE_GIMBAL, [2]).

odrv0.axis0.encoder.config.cpr #Set the encoder count per revolution [CPR] value. This is 4x the Pulse Per Revolution (PPR) value.

axis.config.enable_watchdog = True #Each axis has a configurable watchdog timer that can stop the motors if the control connection to the ODrive is interrupted. Each axis has a configurable watchdog timeout: axis.config.watchdog_timeout, measured in seconds


import odrive
import time

class Motor:
    def __init__(self, odrive, axis_num):
        #define odrive motor path
        axis_path = {
        0: odrive.axis0
        1: odrive.axis1
        }
        
        self.axis = axis_path[axis_num]

    def check_state(self):
        return self.axis.current_state

    def request_state(self, state):
        self.axis.requested_state = state



#connect to odrive devices
def connect_odrives(odrive_serials_list):
    #map of odrive devices
    odrive_map = []
    for serial in odrive_serials_list:
        odrive_map.append(odrive.find_any(serial_number = serial))
        print(f"Connected to ODrive {serial}")
    return odrive_map


#set odrive parameters for actuators - to add - command to set parameter in odrive
def configure_motors(odrive_map):
    axis_params = [
        {
            "odrive_num": 0,
            "axis_num": 0,
            "pole_pairs": 14,
            "torque_constant": 0.026677420362830162,
            "cpr": 16384
        }
    ]

    motor_map = []
    for axis in axis_params:
        motor_map.append(Motor(odrive_map[axis[odrive_num]], axis[axis_num]))
    return actuator_map


def calibrate_actuators(actuator_map):
    #calibrate state number is 3
    for motor in motor_map:
        motor.request_state(3)

    #checks if calibration is complete
    for motor in motor_map:
        while motor.check_state() != 1:
            time.sleep(0.1)
        #set the actuator to close loop control (state number 8)
        motor.request_state(8)
    print("calibration complete")



def main():
    print("Welcome to the super-duper robot arm controller")
    #list of odrive serial numbers by order of actuators
    odrive_serials_list = ["53155462262832"]
    odrive_map = connect_odrives(odrive_serials_list)

    #set parameters
    motor_map = configure_motors(odrive_map)

    #startup and home all axis
    calibrate_actuators(motor_map)   
    

if __name__ == "__main__":
    main()

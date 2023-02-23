import numpy
import odrive
import time
import math

class Actuator:
    def __init__(self, odrive_map, actuator_params):
        #define actuator gear ratio
        self.gear_ratio = actuator_params["gear_ratio"]
        #add position and angle

        #define odrive axis port
        if actuator_params["motor_num"] == 0:
            self.axis = odrive_map[actuator_params["odrive_num"]].axis0
        else:
            self.axis = odrive_map[actuator_params["odrive_num"]].axis1

        #set parameters for odrive axis
        self.set_params(actuator_params)

    def check_state(self):
        return self.axis.current_state

    def request_state(self, state):
        self.axis.requested_state = state

    def set_params(self, actuator_params):
        self.axis.motor.config.current_lim = 25
        self.axis.controller.config.vel_limit = 50
        #self.axis.motor.pole_pairs = actuator_params["pole_pairs"]
        #self.axis.motor.torque_constant = actuator_params["torque_constant"]
        #self.axis.motor.config.motor_type = 0
        #self.axis.encoder.config.cpr = actuator_params["cpr"]


#connect to odrive devices
def connect_odrives(odrive_serials):
    #map of odrive devices
    odrive_map = []
    for serial in odrive_serials:
        odrive_map.append(odrive.find_any(serial_number = serial))
        print("connected to odrive", serial)
    return odrive_map


#set odrive parameters for actuators - to add - command to set parameter in odrive
def configure_actuators(odrive_map):
    actuator_params = [
        {
            "odrive_num": 0,
            "motor_num": 0,
            "gear_ratio": 1,
            "pole_pairs": 14,
            "torque_constant": 0.026677420362830162,
            "cpr": 16384
        }
    ]

    actuator_map = []
    for actuator in actuator_params:
        actuator_map.append(Actuator(odrive_map, actuator))
        print("actuator set")
    return actuator_map

def calibrate_actuators(actuator_map):
    #calibrate state number is 3
    for actuator in actuator_map:
        actuator.request_state(3)

    #checks if calibration is complete
    for actuator in actuator_map:
        while actuator.check_state() != 1:
            time.sleep(0.1)
        #set the actuator to close loop control (state number 8)
        actuator.request_state(8)
    print("calibration complete")



def main():
    print("Welcome to the super-duper robot arm controller")
    #list of odrive serial numbers by order of actuators
    odrive_serials = ["53155462262832"]
    odrive_map = connect_odrives(odrive_serials)

    #set parameters
    actuator_map = configure_actuators(odrive_map)

    #startup and home all axis
    calibrate_actuators(actuator_map)   
    

if __name__ == "__main__":
    main()

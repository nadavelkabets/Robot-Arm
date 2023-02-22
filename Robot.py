import numpy
import odrive
import time
import math

#need to fix - show error messages for user

class actuator:
    #create a list of actuators for ease of for loop
    list = []

    def __init__(self, odrive_unit, odrive_axis, gear_ratio):
        actuator.odrive_unit = odrive_unit
        actuator.odrive_axis = odrive_axis
        actuator.gear_ratio = gear_ratio
        actuator.list.append(actuator)

    def check_state(self):
        return getattr(self.odrive_unit, self.odrive_axis).current_state

    def request_state(self, state):
        getattr(self.odrive_unit, self.odrive_axis).requested_state = state

    class motor:
        def __init__(self, pole_pairs, torque_constant, motor_type):
            actuator.motor.pole_pairs = pole_pairs
            actuator.motor.torque_constant = torque_constant
            actuator.motor.motor_type = motor_type

    class encoder:
        def __init__(self, cpr):
            actuator.encoder.cpr = cpr

def connect():
    #define odrive serial numbers, add more to the list as needed
    odrive_serials = ["1234"]
    odrv = []
    for counter in range(len(odrive_serials)):
        odrv.append(odrive.find_any(serial_number = odrive_serials[counter]))
    print("Connected to all ODrives")
    return odrv


def initiate(odrv):
    #actuator 0 parameters
    actuator0 = actuator(odrive_unit = odrv[0], odrive_axis = "axis0", gear_ratio = 50)
    actuator0.motor = actuator.motor(pole_pairs = 8, torque_constant = 5, motor_type = 0)
    actuator0.encoder = actuator.encoder(cpr = 4000)

    #actuator 1 parameters...
    #actuator1 = actuator(odrive_unit = "odrv0", odrive_axis = "axis1", gear_ratio = 50)
    #actuator1.motor = actuator.motor(pole_pairs = 8, torque_constant = 5, motor_type = 0)
    #actuator1.encoder = actuator.encoder(cpr = 4000)

def startup():
    #calibrate state number is 3
    for actu in actuator.list:
        actu.request_state(actu, state = 3)
    time.sleep(0.5)

    #checks if calibration is complete
    for actu in actuator.list:
        while actu.check_state(actu) != 1:
            time.sleep(0.1)
        #set the actuator to close loop control (state number 8)
        actu.request_state(actu, state = 8)
    print("calibration complete")

def main():
    print("Welcome to the super-duper robot arm controller")\

    #connect to odrives
    odrv = connect()
    
    #set parameters
    initiate(odrv)
    #set_param() set cpr... settings in odrive

    #startup and home all axis
    startup()
    #home() - function to home all axis (absolute encoder 0)
    

if __name__ == "__main__":
    main()

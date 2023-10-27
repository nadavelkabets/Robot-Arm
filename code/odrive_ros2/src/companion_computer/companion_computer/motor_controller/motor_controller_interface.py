from abc import ABC, abstractmethod

class MotorControllerInterface(ABC):
    @abstractmethod
    def roll_position(position_cycles: float):
        pass

    @abstractmethod
    def roll_velocity(velocity_rpm: float):
        pass

    @abstractmethod
    def roll_duty(duty_cycle: float):
        pass

    @abstractmethod
    def calibrate():
        pass

    @abstractmethod
    def abort():
        pass
    
    @abstractmethod
    def reset_cycles(position_cycles: float):
        pass

    @abstractmethod
    def set_brake_state(is_brake_locked: bool):
        pass
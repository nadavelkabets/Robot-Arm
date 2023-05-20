## Quick introduction to BLDC driver design:
A brushless DC motor (Actually it's PMSM) has 3 phases. For accurate and efficient operation, we need to implement FOC (field oriented control) in a closed loop sensored system. This way the voltage on each phase can be controlled precisely based on the angle of the motor.
The most popular circuit to operate a 3 phase motor is a 3 half-bridge system. each half bridge consists of 2 MOSFETs - high side connected to V+ and low side to GND. The two MOSFETs are connected to form a bridge. This way, by switching each side on and off, we can control the voltage on the bridge using PWM.
As explained in the motor introduction document, the motor speed is limited by voltage. The faster the motor spins, the more "back EMF" induced in the coils. Once the "back EMF" voltage is equal to the supply voltage, the maximum speed is reached and the only way to accelerate is to increase the voltage. The current draw of the motor is proportional to the motor shaft torque, but the current draw is also limited by voltage, since according to Ohm's law, once the "back EMF" voltage is equal to the supply voltage, there is no voltage gradient and thus current will not flow. So, we can control motor speed by adjusting voltage to the required speed and allowing the motor to consume as much current as it needs, or control the motor torque by controlling current flow through the voltage gradient [(supply voltage - back EMF voltage)/phase resistance].
To slow down the motor, we need to reduce the voltage below the back EMF voltage. This will reverse the voltage gradient and will cause current flow in the opposite direction (from the motor to the driver). For the driver to handle that reverse current, there are a few options. If the driver is powered by a battery, the battery can be recharged using the regenerative current produced by the motor. If the driver is powered by a power supply that can't handle the current, a resistor that dissipates the heat, or a capacitor that absorbs the current and converts it to a voltage spike must be implemented.

!For the first 3 axis I am planning to use a GL60 motor with a 60mm circular PCB with embedded AS5047P sensor. For axis 4,5,6 I will use 3 stacked 50mm wide rectangle PCBs inside the arm tube, with external sensor PCB on the GL40 motors.

## Specs (test board):
- BLDC motor controller, based on arduino framework and Simple FOC library
- STM32H725RGV6 STM32 microcontroller, 550 MHz
- TMC6200 3 half-bridge gate driver with integrated current sense amplifier
- Custome 4/6 layer PCB with dedicated power and ground planes
- Double sided round PCB
- Inline current sensing for all phases
- 24/48V input, max 20A sustained current
- Integrated hall effect sensor (AS5147)
- USB and CAN communication
- 3 low side and 3 high side MOSFETs.
### To add (final board):
- 2 latching 4 pin chained connectors for power and CAN
- additional input for external absolute encoder
- Temperature sensor for motor and board


## Choosing a driver IC:

| Feature  | TMC6200 | TMC6100 with 3x INA240 | DRV8320S with 3x INA240 | DRV8323S |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| Max supply voltage | 60V | 60V | 60V | 60V |
| Current sensing amplifier | Built in* | External | External | Internal (low side)* | 
| Interface | Standalone and SPI | Standalone and SPI | SPI | SPI |
| External voltage regulator | 12V switching for charge pump, 3.3V LDO for amplifiers | 12V switching for charge pump, 3.3V LDO for amplifiers | 3.3V switching | 3.3V switching |

*Less accurate

![Test station](https://github.com/nadavelkabets/Robot-Arm/blob/main/controller/SCR-20230510-wyj.png)

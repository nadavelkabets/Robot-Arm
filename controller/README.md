## Quick introduction to BLDC driver design:
A BLDC (brushless DC) motor consists of 3 phases. For accurate and efficient operation, it is best to implement FOC (field oriented control) in a closed loop sensored system. This way, the phase voltages are controlled precisely based on the angle of the motor.
To operate a 3 phase motor, 3 half-bridges are used. A half-bridge design uses 2 MOSFETs, with a high side MOSFET connected to voltage supply and a low side MOSFET connected to ground. The two MOSFETs are connected to form a bridge. This way, by switching each side on and off, we can control the voltage on the bridge using PWM.
As explained before, the speed of a BLDC motor is limited by voltage. The faster the motor spins, the more "back EMF" induced back in the coils. Once the "back EMF" voltage is equal to the supply voltage, the maximum speed is reached and the only way to accelerate more is to increase the voltage further.
The current draw of a motor is proportional to the torque acting on the motor shaft. Current draw is also limited by voltage, since according to Ohm's law, when the "back EMF" voltage is equal to the supply voltage, there is no voltage gradient in the circuit and thus current will not flow. 
Motor speed can be controlled by adjusting voltage to the required speed and allowing the motor to consume as much current as it needs, or motor torque can be chosen by controlling current flow through the voltage gradient [(supply voltage - back EMF voltage)/phase resistance].
To slow down the motor, the phase voltage must be reduced below the "back EMF" voltage, reversing the voltage gradient and causing current flow in the opposite direction (from the motor to the driver). 

For a motor driver to handle reverse current, there are a few options. If the driver is powered by a battery, the battery can be recharged using the regenerative current produced by the motor. But, when the driver is powered by a power supply that can't handle the current, a resistor that dissipates the heat, or a capacitor that absorbs the current and converts it to a voltage spike must be implemented.

## Initial requirements:
- FOC close loop motor driver
- 10A continuous current (more than enough for the low kv gimbal motors I intend to use)
- 24/48V operation
- CAN and USB suppport
- built in absolute encoder

## Design decisions:
After some research, I landed on the Simple FOC library. The software is robust and can be easily modified to fit my needs, making it a solid base for the project.
I selected the STM32H725RGV6 microcontroller. The STM32 H7 family provides great connectivity and relatively high compute power. This specific model is the smallest package avilable for the 550MHz variation - VFQFPN 68 8x8mm.

To drive the MOSFETs, a gate-driver is required:
| Feature  | Trinamic TMC6200 | Trinamic TMC6100 | TI DRV8320S | TI DRV8323S |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| Max supply voltage | 60V | 60V | 60V | 60V |
| Current sensing amplifier | Internal in-line | External | External | Internal low-side | 
| Interface | Standalone and SPI | Standalone and SPI | SPI | SPI |

TMC6100 or DRV8320s, combined with the Texas Instruments INA240 current sense amp, will be the most accurate, but also complex and expensive. It is too overkill for my low current application.
Most of the commerical driver boards utilize low-side current sensing. While being cheaper and easier to implement it is less accurate than in-line sensing and also not supported currently for the STM32 in Simple FOC.
That leaves me with the TMC6200 from Trinamic.


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




![Test station](https://github.com/nadavelkabets/Robot-Arm/blob/main/controller/SCR-20230510-wyj.png)

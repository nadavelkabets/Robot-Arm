## Specs:
- Custome PCB - STM32 BLDC motor controller, based on arduino framework and Simple FOC library
- Inline current sensing for all phases.
- 24/48V input, max 25A sustained current.
- Integrated hall effect sensor (AS5147), additional input for external absolute encoder. 
- Temperature sensor for motor and board.
- Flexible communication (USB, SPI, CAN). CAN Bus transceiver built in.


- TI DRV8320H 3 half-bridge driver, 3 low side and 3 high side Infineon BSC030N08NS5 MOSFETs, in line current sensing shunts and amplifiers (TI INA240).

## Choosing a driver IC:

| Feature  | TMC6200 | TMC6100 with 3x INA240 | DRV8320S with 3x INA240 |
| ------------- | ------------- | ------------- | ------------- |
| Max supply voltage | 60V | 60V | 60V |
| Current sensing amplifier | Built in* | External | External |
| Interface | Standalone and SPI | Standalone and SPI | SPI |
| Voltage regulator | 12V switching for VSA, 3.3 LDO for amplifiers | 3.3V LDO for amplifiers, 12V switching for VSA| 3.3V LDO for amplifiers |

*Less accurate

## Log:
Once working I will design the STM32 based controller with integrated CAN communication.

Optional - electromagnetic brake support. Round pcb board, double sided.

Open source schematics for reference:
- Dagor ESP32 controller
- TMC6200-EVAL
- ODrive V3.6
- xESC2 mini

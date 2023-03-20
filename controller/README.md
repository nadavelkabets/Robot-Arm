## Specs:
- Custome PCB - STM32 BLDC motor controller, based on arduino framework and Simple FOC library
- TI DRV8320H 3 half-bridge driver, 3 low side and 3 high side Infineon BSC026N08NS MOSFETs, in line current sensing shunts and amplifiers (TI INA240).
- Flexible communication (USB, SPI, CAN). CAN Bus transceiver built in.
- 24/48V input, max 25A sustained current.
- Integrated hall effect sensor (AS5147), additional input for external absolute encoder. 
- Temperature sensor for motor and board.

## Log:
Once working I will design the STM32 based controller with integrated CAN communication.

Optional - electromagnetic brake support. Round pcb board, double sided.

Open source schematics for reference:
- Dagor ESP32 controller
- TMC6200-EVAL
- ODrive V3.6
- xESC2 mini

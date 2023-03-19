## Specs:
- Custome PCB - STM32 based BLDC motor controller, based on arduino framework and Simple FOC library
- Built in motor driver: pre-driver IC (TI DRV8320 or TMC6100), 3 low side and 3 high side mosfets (Infineon?), in line current sensing shunts and amplifiers (TI INA240).
- Flexible communication (USB, SPI, I2C, CAN). CAN Bus transceiver built in.
- 24/48V input, max 25A sustained current.
- Integrated hall effect sensor (AS5600 or AS5047), additional input for external absolute encoder. 
- Temperature sensor for motor and board.

## Log:
The original design used Infineon BSC026N08NS5ATMA1 mosfets. I decided to go with Infineon IPB026N06NATMA1 instead. They are very similar, but this one is easier to solder.
Once working I will design the STM32 based controller with integrated CAN communication.

Optional - electromagnetic brake support. Round pcb board, double sided.

Open source schematics for reference:
- Dagor ESP32 controller
- TMC6200-EVAL
- ODrive V3.6
- xESC2 mini

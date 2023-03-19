## Specs:
- Custome PCB - STM32 based BLDC motor controller, with a 3 half-bridge driver IC, 3 low side and 3 high side mosfets, in line current sensing shunts and amplifiers.
- Trinamic TMC6200, TMC6100 or DRV8323R.
- Running arduino framework with Simple FOC library or VESC.
- Flexible communication (USB, SPI, I2C, CAN). CAN Bus transceiver built in.
- 24/48V input, max 15A sustained current.
- Integrated hall effect sensor (AS5600 or AS5047), additional input for external absolute encoder. 
- Temperature sensor for motor and board.

Trinamic TMC6200 was chosen because it measures phase current in line using built in amplifiers. This approach is more percise than the low side current measurements in Texas Instruments DRV8323.

## Log:
The first prototype is based on the TMC6200-EVAL evaluation board. It will communicate via SPI with external ESP32 module.
The original design used Infineon BSC026N08NS5ATMA1 mosfets. I decided to go with Infineon IPB026N06NATMA1 instead. They are very similar, but this one is easier to solder.
Once working I will design the STM32 based controller with integrated CAN communication.

Optional - electromagnetic brake support. Round pcb board, double sided.

Open source schematics for reference:
- Dagor ESP32 controller
- TMC6200-EVAL
- ODrive V3.6
- xESC2 mini

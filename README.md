< ongoing project >
# Robotic Arm
### The purpose of this project is to create a 6-DOF robotic arm that is fast, accurate and sub $1000.
This robotic arm will be designed after the [Universal Robotics UR5e](https://www.universal-robots.com/products/ur5-robot/). 
The robot will have a reach of 800mm and use 6 actuators with a diameter of ~80-100mm. Each actuator will include 2 encoders (motor and output), a BLDC outrunner motor, and an ambitious 3D printed strain wave reducer. The "Harmonic Drive" gearbox will use a reduction ratio of (1:30-1:50).
The robot will be powered by 3 ODrive FOC controllers runniing on 48V DC power. The robot will be controlled by a Raspberry Pi running linux, calculating the required inverse kinematics.



## Project log
Odrive documentation: https://docs.odriverobotics.com/v/0.5.4/fibre_types/com_odriverobotics_ODrive.html

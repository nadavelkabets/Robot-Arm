< ongoing project > update hackaday strain wave robot actuator
# Robotic Arm
### The purpose of this project is to create a 6-DOF robotic arm that is fast, accurate and sub $1000.
This robotic arm will be designed after the [Universal Robotics UR5e](https://www.universal-robots.com/products/ur5-robot/) and [Kuka LBR/AGILIUS](https://www.kuka.com/en-us/products/robotics-systems/industrial-robots/kr-agilus). 
The robot will have a reach of ~800mm and use 6 actuators with a diameter of ~80-100mm. Each actuator will include 2 encoders (motor and output), a BLDC outrunner motor, and an ambitious 3D printed strain wave reducer. The "Harmonic Drive" gearbox will use a reduction ratio of (1:30-1:50). I would like to attempt a back-drivable strain wave reducer but it is very hard.
The robot will be powered by 3 ODrive FOC controllers runniing on 48V DC power. The robot will be controlled by a Raspberry Pi running linux, calculating the required inverse kinematics.
The robot will be built from ABS, Nylon, Carbon Fiber and Aluminum.

Actuator 2 and 3 will take the most ammount of load (probably around 50nm). They will probably use a powerful 80mm (diameter) brushless 100kv motor.

The following materials will be considered for the strain wave reducer: ABS, nylon, nylon 12CF, TPU95A, iglide I180PF. The bearing ball cages might be manufactured using SLA. (Siraya tech mecha? Tenacious/Blue mix? Phrozen nylon-green?)

## Project log
A test station was constructed to test components and software. 
![Test station](https://github.com/nadavelkabets/Robot-Arm/blob/main/media/IMG_0316.jpg)
Odrive documentation: https://docs.odriverobotics.com/v/0.5.4/fibre_types/com_odriverobotics_ODrive.html

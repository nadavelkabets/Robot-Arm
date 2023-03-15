< ongoing project >
# Robotic Arm
### Project goals and robot specs:
- 6-DOF robotic arm that is fast and accurate (180 deg/s top speed, precision of 1mm or less)
- Reach of 500-800mm
- Payload capacity of 1-3kg
- Custom actuator design with 2 absolute encoders (motor and output), a BLDC motor and a strain wave reducer (harmonic drive)
- Custom FOC BLDC driver for each motor based on SimpleFOC or VESC firmware.
- Calculating the inverse kinematics for the robot (ROS - robot operating system?)

#### TBD:
- Custom 3D printed strain wave reducer with a gear ratio of 1:30-1:50 that is back drivable. The following materials will be considered for the strain wave reducer: ABS, nylon, nylon 12CF, TPU95A, iglide I180PF. The bearing ball cages might be manufactured using SLA. (Siraya tech mecha? Tenacious/Blue mix? Phrozen nylon-green?)
- Custom absolute magnetic ring encoder with hollow shaft
- Electromagnetic brake

#### General design:
This robotic arm will be designed after the [Universal Robotics UR5e](https://www.universal-robots.com/products/ur5-robot/) and [Kuka LBR/AGILIUS](https://www.kuka.com/en-us/products/robotics-systems/industrial-robots/kr-agilus).

## Project log
BLDC motors offer high torque, resolution and speed when driven by field oriented control in a closed loop system.
Outrunner motor design is preferable as it has more torque in the same size. A gimbal motor will perform better because it is able to produce high torque with relatively low current.
Strain wave reducers (Harmonic Drive) are expensive and complex, but offer extremely low backlash, backdrivability and high gear ratio in a small space (I found cheap harmonic drives on taobao).
Back drivable reducers allow for torque measurement for cobot applications.

A test station was constructed to test components and software.
Components: ODrive V3.6, AS5047P encoder and MAD 5010 310KV motor.
![Test station](https://github.com/nadavelkabets/Robot-Arm/blob/main/media/IMG_0316.jpg)

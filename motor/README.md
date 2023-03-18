## Quick introduction to brushless motors:
- Each brushless motor has a KV rating. This value, when multiplied by the voltage supplied to the motor, will result in the motor speed (without load).
- When a brushless motor spins, the magnets induce a force in the coils named "back EMF" which opposes the rotation of the motor.
- The faster the motor spins, the more "back EMF" induced. The motors max speed is achieved when the voltage of the back EMF is equal to the voltage supplied to the coils.
- The difference in voltage, together with the resistance of the copper coils, determines the maximum current that can go through the motor (Ohm's law, I=V/R).
- The torque output of a brushless motor is proportional to the current. The more current supplied, the more torque the motor produces.
- When the motor accelerated, the voltage difference drops and less current can be supplied. For that reason, the faster the motor goes the less torque it is able to produce. The maximal speed could only be achieved without load.
- A brushless motor is usually limited thermally. More current = more heat. 
- We can only control the voltage supplied to a motor. Lower KV motors require less current for the same torque. BUT, lowering KV is done by winding more copper turns. In order for more turns to fit in the same motor, you are required to use thinner wires which have higher resistance and thus output more heat for the same current.
- As I said above, motors are thermally limited. The advantage of using lower KV motors is in the motor driver, which need to handle lower currents. There is no difference in torque.

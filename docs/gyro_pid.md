# GYRO PID Algorithm

Most articles on Lego EV3 PID algorithms use the line follower to describe the algortihm.  This article will use the Gyro because it should be a conceptually simpler starting for a new FLL student to understand.

## Proportional

### variables
* Tp = Target Power
* Kp = the Constant 'K' for the 'p' proportional controller

### Code

```  
Td = 1000 # target distance
top_speed = 900
Kp = 10    
offset = 45
Tp = 500
while (robot.distance() < Td):
   print("distance: " + str(robot.distance())) 
   error = gyro_sensor.angle()
   correction = error * -1  # want robot to travel in opposite direction of angle error
   Turn = Kp * correction                  # the "P term", how much we want to change the motors' power
   powerA = ((Tp + Turn) / top_speed) * 100    # the power level for the A motor, converted to dc range of -100 to 100
   powerB = ((Tp - Turn) / top_speed) * 100    # the power level for the B motor
   print("error " + str(error) + "; turn " + str(Turn) + "; powerA " + str(powerA) + "; powerB " + str(powerB))   

   motorA.dc(powerA)                  # issue the command with the new power level in a MOTOR block
   motorB.dc(powerB)                  # same for the other motor but using the other power level
robot.stop()

```  
--->[try it out](https://fll-pigeons.github.io/gamechangers/simulator/public/)  (copy code and paste it under Python tab)



## Integral

## Derivative

## Tuning









* References
  * J. Sluka's excellent article: [A PID Controller For Lego Mindstorms Robots](http://www.inpharmix.com/jps/PID_Controller_For_Lego_Mindstorms_Robots.html)
  * [PID Line Follower Code by Using MicroPython 2.0](https://thecodingfun.com/2020/06/16/lego-mindstorms-ev3-pid-line-follower-code-by-using-micropython-2-0/)
  * [Pybricks Porportional Line Follower](https://pybricks.github.io/ev3-micropython/examples/robot_educator_line.html)

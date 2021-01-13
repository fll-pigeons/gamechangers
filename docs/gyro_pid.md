# Very DRAFT

# Driving straight using a gyro and PID algorithm

Most articles on Lego EV3 PID algorithms use the line follower to describe it.  This article will use the Gyro because it might be a conceptually simpler starting point for a new FLL student to understand.

## Proportional Controller
For a P (proportional) controller, we use a sensor to measure something that you are trying to control, then convert that measurement to an error.  

If your robot is driving straight, gyro.angle() should return a zero if there is no tracking error on the robot.  If the robot turns left, you should be a negative number, and if it turn right, it should be apositive number.

We want the correction to be the opposite of the number given by the gyro.

However, because of processing delays in getting the reading from the gyro, and the time for the EV3 brick to decide what to do, we need toa add a fudge (scaling) factor to the correction so that the robot will 
For the Drive Straight Using Gyro Algorithm we did that by assigning the gyro sensor angle to an error variable (the gyro.angle() should return a zero if there is no tracking error on the robot). Then we multiply the error by a scaling factor called Kp. The result is a correction for the system. In our line follower example the correction is applied as an increase/decrease in the power level of the motors. The scaling factor Kp is determined using a bit of educated guessing and then fine tuned by trial and error. 

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

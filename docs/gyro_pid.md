# Very DRAFT

# Driving straight using a gyro and PID algorithm

Most articles on Lego EV3 PID algorithms use the line follower (using the Lego Colour sensor) to describe it.  This article will use the Lego Gyro because it might be a conceptually easier for a new FLL student to understand.

## Proportional Controller

### Intro
For a P (proportional) controller, we use a sensor to measure something that you are trying to control, then convert that measurement to an error.  Then we multiply the error by a scaling factor called Kp.  The result is a correction for the system.  The correction in this case is can applied as an increase/decrease in the power level of the motors, or as the angle parameter in the Pybricks robot.drive(speed, angle) method. 

The scaling factor Kp is determined using a bit of educated guessing and then fine tuned by trial and error. 

For getting our robot to drive straight, we are using the gyro sensor to measure, in degrees, the amount the robot is off course (the error).  Then for the robot course correction, we want the robot to turn in the opposite direction of the error then multiply that by a scaling factor called Kp.

### Background: Robot & Gyro
If your robot is driving straight, gyro.angle() should return a zero if there is no tracking error on the robot.  If the robot turns off course, gyro.angle will return a positive or negative number depending on the number of degrees your robot is off course.  For example, if you tell you robot to drive straight, and it turns slightly to the left, gyro.angle() will return a negative value (-1 to -359) corresponding to the number of degrees your robot if off from going in a straight direction.

### Algorithm Overview
We want our robot to turn in the oppposite direction to the error that gyro.angle() returns - we want the correction to be the negative of the number given by the gyro... i.e. if the number returned by the gyro is 3, we want the robot to turn by at least -3 degrees in the opposit direction.

Further, because of processing delays in getting the reading from the gyro, and the time for the EV3 brick to decide what to do, we also need to a add a scaling factor (Kp) to the correction so that the robot will turn in time.

For the Drive Straight Using Gyro Algorithm we did that by assigning the gyro sensor angle to an error variable (the gyro.angle() should return a zero if there is no tracking error on the robot). 

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
   Turn = Kp * error * -1                  # the "P term", how much we want to change the motors' power
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

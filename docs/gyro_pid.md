# Very DRAFT

# Driving straight using a gyro and PID algorithm

Most articles on Lego EV3 PID algorithms use the line follower (using the Lego Colour sensor) to describe it.  This article will use the Lego Gyro because it might be a conceptually easier for a new FLL participant to understand.

## Proportional Controller

### Intro
For a P (proportional) controller, we use a sensor to measure something that you are trying to control, then convert that measurement to an error.  Then we multiply the error by a scaling factor called Kp.  The result is a correction for the system.  The correction in this case can applied as an increase/decrease in the power level of the motors, or as the angle parameter in the Pybricks robot.drive(speed, angle) function.

The scaling factor Kp is first determined using a bit of educated guessing and then is fine tuned by trial and error. 

In this particular case, to get our robot to drive straight, we are using the gyro sensor to measure (in degrees) the amount the robot is off course (the error).  Then for the robot course correction, we want the robot to turn in the opposite direction of the error, then multiply that number by a scaling factor called Kp.

### Background: Robot & Gyro
If your robot is driving straight, gyro.angle() should return zero degrees if there is no tracking error on the robot.  If the robot turns slightly off course, gyro.angle will return a positive or negative number depending on the direction and number of degrees your robot is off course.  For example, if you tell you robot to drive straight, and it turns slightly to the left, gyro.angle() will return a negative value corresponding to the number of degrees your robot is off course.

### Algorithm Overview
We want our robot to turn in the oppposite direction to the error that gyro.angle() returns - we want the correction to be the negative of the number of degrees returns by the gyro.  For example, if the number returned by the gyro is 3 degrees, we want the robot to turn by at least -3 degrees in the opposite direction.

Further, because of processing delays in getting the reading from the gyro, and the time for the EV3 brick to decide what to do, we also need to a add a scaling factor (Kp) to the correction so that the robot.  Otherwise, the robot may occillate (swing back and forth) as it is trying to get back to a straight line of travel.

### Code
#### Using power level of the motors

```  
Td = 1000 # target distance
Kp = 1 #  the Constant 'K' for the 'p' proportional controller
Tp = 80 # Power (also known as 'duty cycle' - percentage between -100.0 to 100).
while (robot.distance() < Td):
   error = gyro_sensor.angle()
   correction = Kp * error * -1   
   
   powerA = Tp + correction
   powerB = Tp - correction   

   motorA.dc(powerA) 
   motorB.dc(powerB) 
   
   print("error " + str(error) + "; correction " + str(correction) + "; powerA " + str(powerA) + "; powerB " + str(powerB))   
   
robot.stop()
```  
--->[try it out](https://fll-pigeons.github.io/gamechangers/simulator/public/)  (copy code and paste it under Python tab)

#### Using drive.straight()
(why use motor power levels rather than drive.straight? because drive.straight use its own internal PID algorithms for angle and distance that may cause subtle bugs with a user implemented PID algorithm - test the algorithm out to make sure it works OK for your purposes)

```  
Td = 1000 # target distance
Kp = 1.2    
Ts = 300 # target speed

while (robot.distance() < Td):
   error = gyro_sensor.angle()
   turn = Kp * error * -1  # the "P term", how much we want to change the robot's direction
   robot.drive(Ts, turn)
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

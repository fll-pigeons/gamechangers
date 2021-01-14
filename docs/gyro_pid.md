# Very DRAFT

# Driving straight using a gyro and PID algorithm

Most articles on Lego EV3 PID algorithms use the line follower (using the Lego Colour sensor) to describe it.  This article will use the Lego Gyro because it might be a conceptually easier for a new FLL participant to understand.

# PID Overview
A PID controller is a Proportional Integral Derivative controller:  It contains:
  * a proportional (P) term that tries to correct the **current error**, 
  * an integral (I) term that tries to correct **past errors**, and 
  * a derivative (D) term that tries to tries to correct errors that hasn't even occurred yet (**future errors**). 

## Proportional Controller - correct current errors

### Intro
For a P (proportional) controller, we use a sensor to measure something that you are trying to control, then convert that measurement to an error.  Then we multiply the error by a scaling factor called Kp.  The result is a correction for the system.  The correction in this case can applied as an increase/decrease in the power level of the motors, or as the angle parameter in the Pybricks robot.drive(speed, angle) function.

The scaling factor Kp is first determined using a bit of educated guessing and then is fine tuned by trial and error. 

In this particular case, to get our robot to drive straight, we are using the gyro sensor to measure (in degrees) the amount the robot is off course (the error).  Then for the robot course correction, we want the robot to turn in the opposite direction of the error, then multiply that number by a scaling factor called Kp.

### Background: Robot & Gyro
If your robot is driving straight, gyro.angle() should return zero degrees if there is no tracking error on the robot.  If the robot turns slightly off course, gyro.angle will return a positive or negative number depending on the direction and number of degrees your robot is off course.  For example, if you tell you robot to drive straight, and it turns slightly to the left, gyro.angle() will return a negative value corresponding to the number of degrees your robot is off course.

### Algorithm Overview
Therefore, the error that our robot makes while attempting to travel straight corresponds to the angle in degrees returned by the gyro sensor:

   error = gyro_sensor.angle()

However, we want our robot to turn in the oppposite direction to the error that gyro.angle() returns - we want the correction to be the negative of the number of degrees returns by the gyro: 

   correction = error * -1 
   
Further, because of processing delays in getting the reading from the gyro, and the time for the EV3 brick to decide what to do, we also need to a add a scaling factor (Kp) to the correction so that the robot.  Otherwise, the robot may occillate (swing back and forth) as it is trying to get back to a straight line of travel:

   correction = Kp * error * -1 

The correction is then applied to increase/decrease in the power level of the motors:

   powerA = Tp + correction
   powerB = Tp - correction 

Or, the correction is used as the angle parameter in the Pybricks robot.drive(speed, angle) function:

   robot.drive(Ts, correction)
  
### Code
#### Using power level of the motors

```  
Td = 1000 # target distance
Tp = 80 # Target power - percentage of max power of motor (power is also known as 'duty cycle' ) 

Kp = 3 #  the Constant 'K' for the 'p' proportional controller

while (robot.distance() < Td):
   error = gyro_sensor.angle() # proportional
   
   correction = Kp * error * -1   
   
   powerA = Tp + correction
   powerB = Tp - correction   

   motorA.dc(powerA) 
   motorB.dc(powerB) 
   
   print("error " + str(error) + "; correction " + str(correction) + "; powerA " + str(powerA) + "; powerB " + str(powerB))   
   wait(10)
   
robot.stop()
```  
--->[try it out](https://fll-pigeons.github.io/gamechangers/simulator/public/)  (copy code and paste it under Python tab)

#### Using robot.drive() 
using Pybrick's [robot.drive(drive_speed, turn_rate)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.drive) function, whic starts driving at the specified speed and turn rate.

(why use motor power levels rather than drive.straight? because Pybrick's drive.straight uses its own internal PID algorithms for angle and distance that may cause subtle bugs with a user implemented PID algorithm - test the algorithm out to make sure it works OK for your purposes)

```  
Td = 1000 # target distance
Ts = 300 # target speed of robot in mm/s

Kp = 5 #  the Constant 'K' for the 'p' proportional controller

while (robot.distance() < Td):
   error = gyro_sensor.angle() # proportional
   
   correction = Kp * error * -1 
   
   robot.drive(Ts, correction)

   print("error " + str(error) + "; correction " + str(correction))   
   wait(10)
   
robot.stop()
```  
--->[try it out](https://fll-pigeons.github.io/gamechangers/simulator/public/)  (copy code and paste it under Python tab)


## Integral Controller - correct past errors

### Intro
To improve the response of our P controller we will add a new term to the equation. This term is called the integral, the "I" in PID.  The integral is simply the running sum of the error. 

### Algorithm Overview

Each time we read the gyro sensor and calculate an error we will add that error to a variable we will call integral:

   integral = integral + error
   
Next, just like the P term, we will multiply the integral by a proportionality constant, that's another K. Since this proportionality constant goes with the integral term we will call it Ki. Just like the proportional term we multiply the integral by the constant (Ki) to get a correction. For our line following robot it is an addition to our correction variable.

   correction = Kp*(error) + **Ki*(integral)**

### Code
#### Using power level of the motors

```  
Td = 1000 # target distance
Tp = 60 # Target power - percentage of max power of motor (power is also known as 'duty cycle' ) 

Kp = 3 #  the Constant 'K' for the 'p' proportional controller

integral = 0 # initialize
Ki = 0.025 #  the Constant 'K' for the 'i' integral term

while (robot.distance() < Td):
   error = gyro_sensor.angle() # proportional
   if (error == 0): # prevent the integral term from 'overshooting'
       integral = 0
   else:
       integral = integral + error 
       
   correction = (Kp*(error) + Ki*(integral)) * -1       

   power_left = Tp + correction
   power_right = Tp - correction   

   left_motor.dc(power_left) 
   right_motor.dc(power_right) 

   print("error " + str(error) + "; correction " + str(correction)  + "; integral " + str(integral)+ "; power_left " + str(power_left) + "; power_right " + str(power_right))   
   wait(10)
   
robot.stop()

```  
--->[try it out](https://fll-pigeons.github.io/gamechangers/simulator/public/)  (copy code and paste it under Python tab)

#### Using robot.drive() 
using Pybrick's [robot.drive(drive_speed, turn_rate)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.drive) function, which starts driving at the specified speed and turn rate.

(why use motor power levels rather than drive.straight? because Pybrick's drive.straight uses its own internal PID algorithms for angle and distance that may cause subtle bugs with a user implemented PID algorithm - test the algorithm out to make sure it works OK for your purposes)

```  
Td = 1000 # target distance
Ts = 150 # target speed of robot in mm/s
Kp = 3 #  the Constant 'K' for the 'p' proportional controller

integral = 0 # initialize
Ki = 0.025 #  the Constant 'K' for the 'i' integral term

while (robot.distance() < Td):
   error = gyro_sensor.angle() # proportional
   if (error == 0): # prevent the integral term from 'overshooting'
       integral = 0
   else:
       integral = integral + error 
       
   correction = (Kp*(error) + Ki*(integral)) * -1
   
   robot.drive(Ts, correction)

   print("error " + str(error) + "; integral " + str(integral) + "; correction " + str(correction)  )    
robot.stop()
```  
--->[try it out](https://fll-pigeons.github.io/gamechangers/simulator/public/)  (copy code and paste it under Python tab)

   
## Derivative Controller - try to correct future errors

### Intro

We can look into the future by assuming that the next change in the error is the same as the last change in the error. 

That means the next error is expected to be the current error plus the change in the error between the two preceding sensor samples. The change in the error between two consecutive points is called the derivative.

### Algorithm

If the current error is 2 degrees and the error before that was 5 degrees. What would be the **next error**?  the change in error is the derivative which is:

(the current error) - (the previous error)

which for our numbers is 2 - 5 = -3. The current derivative therefore is -3. 

To use the derivative to predict the next error we would use

(next error) = (the current error) + ( the current derivative)

which for our numbers is 2 + (-3) = -1. So we predict the next error will be -1. 

   Correction  = Kp*(error) + Ki*(integral) + **Kd*(derivative)**


### Code
#### Using power level of the motors

```  
Td = 10000 # target distance
Tp = 60 # Target power - percentage of max power of motor (power is also known as 'duty cycle' ) 

Kp = 3 #  the Constant 'K' for the 'p' proportional controller

integral = 0 # initialize
Ki = 0.025 #  the Constant 'K' for the 'i' integral term

derivative = 0 # initialize
lastError = 0 # initialize
Kd = 3 #  the Constant 'K' for the 'd' derivative term

while (robot.distance() < Td):
   error = gyro_sensor.angle() # proportional
   if (error == 0):
       integral = 0
   else:
       integral = integral + error 
   derivative = error - lastError  
   
   correction = (Kp*(error) + Ki*(integral) + + Kd*derivative) * -1
   
   power_left = Tp + correction
   power_right = Tp - correction   

   left_motor.dc(power_left) 
   right_motor.dc(power_right) 
     
   lastError = error  
   
   print("error " + str(error) + "; correction " + str(correction)  + "; integral " + str(integral)  + "; derivative " + str(derivative)+ "; power_left " + str(power_left) + "; power_right " + str(power_right))   
   wait(10)
   
robot.stop()

```  
--->[try it out](https://fll-pigeons.github.io/gamechangers/simulator/public/)  (copy code and paste it under Python tab)

#### Using robot.drive() 
using Pybrick's [robot.drive(drive_speed, turn_rate)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.drive) function, whic starts driving at the specified speed and turn rate.

(why use motor power levels rather than drive.straight? because Pybrick's drive.straight uses its own internal PID algorithms for angle and distance that may cause subtle bugs with a user implemented PID algorithm - test the algorithm out to make sure it works OK for your purposes)

```  
Td = 1000 # target distance
Ts = 150 # target speed of robot in mm/s
Kp = 3 #  the Constant 'K' for the 'p' proportional controller

integral = 0 # initialize
Ki = 0.025 #  the Constant 'K' for the 'i' integral term

derivative = 0 # initialize
lastError = 0 # initialize
Kd = 3 #  the Constant 'K' for the 'd' derivative term

while (robot.distance() < Td):
   error = gyro_sensor.angle() # proportional 
   if (error == 0):
       integral = 0
   else:
       integral = integral + error    
   derivative = error - lastError  
   
   correction = (Kp*(error) + Ki*(integral) + Kd*derivative) * -1
   
   robot.drive(Ts, correction)

   lastError = error  
   
   print("error " + str(error) + "; integral " + str(integral) + "; correction " + str(correction)  )    
       
robot.stop()
```  
--->[try it out](https://fll-pigeons.github.io/gamechangers/simulator/public/)  (copy code and paste it under Python tab)





## Tuning

Tuning is the process of finding the best values for Kp, Ki and Kd.






## References
  * J. Sluka's excellent article: [A PID Controller For Lego Mindstorms Robots](http://www.inpharmix.com/jps/PID_Controller_For_Lego_Mindstorms_Robots.html)
  * [PID Line Follower Code by Using MicroPython 2.0](https://thecodingfun.com/2020/06/16/lego-mindstorms-ev3-pid-line-follower-code-by-using-micropython-2-0/)
  * [Pybricks Porportional Line Follower](https://pybricks.github.io/ev3-micropython/examples/robot_educator_line.html)

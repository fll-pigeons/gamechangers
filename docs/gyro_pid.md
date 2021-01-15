# Driving straight using a gyro and PID algorithm

Most articles on Lego EV3 PID algorithms use a line follower example (using the Lego Colour sensor) to describe it.  This article will use the Lego Gyro because it might be a conceptually easier for new FLL participants to understand.

# PID Overview
A PID Controller is a common technique used to control a robot.  The term 'PID' is an acronym for Proportional Integral Derivative.  A complete mathematical description of a PID Controller is fairly complex, but the basics of the approach can be to control Lego EV3 robots.  At its core, each element of a PID controller deals with a specific type of tracking error:
  * the proportional (P) term tries to correct the **current error**, 
  * the integral (I) term that tries to correct **past errors**, and 
  * the derivative (D) term that tries to tries to correct errors that hasn't even occurred yet (**future errors**). 

## Proportional Controller - correct current errors

### Intro
For a P (proportional) controller, we use a sensor to measure something that you are trying to control and then convert that measurement to an **error**.  Then we multiply that error by a **scaling factor** called Kp.  The result is a **correction** for the system.  The correction in this case can applied as an increase/decrease in the power level of the motors, or as the angle parameter in the Pybricks robot.drive(speed, angle) function.

The scaling factor Kp is first determined using a bit of educated guessing and then is **fine tuned by trial and error**. 

In this particular case, to get our robot to drive straight, we are using the gyro sensor to measure (in degrees) the amount the robot is off course (the error).  Then for the robot course correction, we want the robot to turn in the opposite direction of the error, by at least the amount of the error.  However, because of brick processing lag (Lego EV3 bricks are slow to run programs and process data from sensors), we also need to compensate for this by multiplying that correction by the scaling factor (Kp).

### Background: Robot & Gyro
If your robot is driving straight, gyro.angle() should return zero degrees if there is no tracking error on the robot.  If the robot turns slightly off course, gyro.angle will return a positive or negative number depending on the direction and number of degrees your robot is off course.  For example, if you tell you robot to drive straight, and it turns slightly to the left, gyro.angle() will return a negative value corresponding to the number of degrees your robot is off course.

### Algorithm Overview
Therefore, the error that our robot makes while attempting to travel straight corresponds to the angle in degrees returned by the gyro sensor:

   error = gyro_sensor.angle()

However, we want our robot to turn in the oppposite direction to the error that gyro.angle() returns - we want the correction to be the negative of the number of degrees returns by the gyro: 

   correction = error * -1 
   
Further, because of processing delays in getting the reading from the gyro, and the time for the EV3 brick to decide what to do, we also need to a add a scaling factor (Kp) to the correction so that the robot.  Otherwise, the robot may occillate (swing back and forth) wildly as it is trying to get back to a straight line of travel:

   correction = Kp * error * -1 

The correction is then applied to increase/decrease in the power level of the motors:

   powerA = Tp + correction
   powerB = Tp - correction 

Or, if using the Pybricks robot.drive(speed, angle) function, the correction is used as the angle parameter:

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
Using Pybrick's [robot.drive(drive_speed, turn_rate)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.drive) function, which starts driving at the specified speed and turn rate.

(why use motor power levels rather than drive.straight? Because Pybrick's drive.straight uses its own internal PID algorithms for angle and distance that may cause subtle bugs with a user implemented PID algorithm - test the algorithm out to make sure it works for your purposes)

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
   
Next, just like the P term, we will multiply the integral by a proportionality constant, that's another K. Since this proportionality constant goes with the integral term we will call it Ki. Just like the proportional term we multiply the integral by the constant (Ki) to get a correction:

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
using Pybrick's [robot.drive(drive_speed, turn_rate)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.drive) function:

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

We can look into the future by assuming that the next change in the error is the same as the last change in the error.  This change in error is called the derivative.  To use the derivative to predict the next error we would use

   (next error) = (current error) + (current derivative)   

### Algorithm

Each time we read the gyro sensor and calculate an error, we calculate the derivative as the difference between the current error and the last error: 

   derivative = error - lastError
   
Next, just like the P term, we will multiply the derivative by a proportionality constant. Since this proportionality constant goes with the derivative term we will call it Kd. Just like the proportional term we multiply the derivative by the constant (Kd) to get a correction. For our robot it is an addition to our correction variable:

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
using Pybrick's [robot.drive(drive_speed, turn_rate)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.drive) function:

```  
Td = 1000 # target distance
Ts = 300 # target speed of robot in mm/s
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

Tuning a PID algorithm is the process of finding the best values for Kp, Ki and Kd.

### Steps

PID Formula: correction = (Kp*(error) + Ki*(integral) + Kd*(derivative))

1. Makes the PID controller act like a simple P controller by setting the Ki and Kd values to zero

2. Set the Tp (power) term to a smallish one 20% (or Ts (speed) to 50 mm/s)

3. Set the Kp term to a "reasonable" value:
  *  take the maximum value we want to send to the motor's power control (100) and divide by the maximum useable error value (5): 100 / 5 = 20; or
  * set it to 1 and see what happens

4. Run the robot and watch what it does. 

If it can't follow the line and wanders off then increase Kp. If it oscillates wildly then decrease Kp. Keep changing the Kp value until you find one that follows the line and gives noticeable oscillation but not really wild ones. We will call this Kp value "Kc" ("critical gain").

5. Determine how fast it is oscillating (using Kc as your Kp value).

This measurement doesn't have to be accurate. The oscillation period (Pc) is how long it takes the robot to swing from one side of the line to the other then back to the side where it started. For typical Lego Ev3 robots Pc will probably be in the range of about 0.5 seconds to a second or two.

6. Determine how fast the robot cycles through it's control loop. Here is a program that sets the loop to a fixed number of steps and times how long the robot takes to finish.

The time per loop (dT) is the measured time divided by the number of loops. 

* sample program:

```  
start = time.time()
print("Loop start")

Ts = 150 # target speed of robot in mm/s

Kp = 3 #  the Constant 'K' for the 'p' proportional controller

integral = 0 # initialize
Ki = 0.025 #  the Constant 'K' for the 'i' integral term

derivative = 0 # initialize
lastError = 0 # initialize
Kd = 3 #  the Constant 'K' for the 'd' derivative term

count = 0
for count in range(500):    
   error = gyro_sensor.angle() # proportional 
   if (error == 0): # prevent the integral term from 'overshooting'
       integral = 0
   else:
       integral = integral + error    
   derivative = error - lastError  
   
   correction = (Kp*(error) + Ki*(integral) + + Kd*derivative) * -1
   
   robot.drive(Ts, correction)

   lastError = error  
   
   count = count + 1

robot.stop()

end = time.time()
time = end - start
print("Loop time: " + str(time))
print("Loop iterations: " + str(count))
print("time per loop (dT): " + str(time / count))
```  
--->[try it out](https://fll-pigeons.github.io/gamechangers/simulator/public/)  (copy code and paste it under Python tab)

For a full PID controller, written in Lego EV3 Python, the dT will be in the range of 0.020 to 0.030 seconds per loop. 

7. Use the table below to calculate a set of Kp, Ki, and Kc values.

**Ziegler–Nichols method giving K' values**

(loop times considered to be constant and equal to dT)

| Control Type | Kp | Ki | Kd |    
| --- | ---| --- | ---|
| PID | 0.60 * Kc | 2 * Kp * dT / Pc | Kp * Pc / (8 * dT) |

* Sample calculation

  * Inputs from our robot:

    * Kc = 3 # critical gain
    * dT = 0.239 secs # time per loop
    * Pc = 0.5 seconds # oscillation period

  * calculations

    * Kp = 0.6 * 3 = 1.8
    * Ki = 2 * 1.8 * 0.239 / 0.5 = 1.72
    * Kd = 1.8 * 0.5  / (8 * 0.239) = 0.4707

see section [How changes in Kp, Ki, and Kd affect the robots behavior](http://www.inpharmix.com/jps/PID_Controller_For_Lego_Mindstorms_Robots.html) of J. Sluka's excellent PID article for information on how changes to each element affect the robot's movement

* program to calculate PID elements:
(note: you need to update the 'Pc' variable with the actual oscillation period of you robot, and also update the 'Ns' variable to get the loop to run 10000 times when testing an actual robot)

```
start = time.time()
print("Loop start")

Pc = 0.5 # oscillation period from previous run
Ns = 200 # number of steps in loop
Ts = 150 # target speed of robot in mm/s

Kp = 3 #  the Constant 'K' for the 'p' proportional controller

integral = 0 # initialize
Ki = 0.025 #  the Constant 'K' for the 'i' integral term

derivative = 0 # initialize
lastError = 0 # initialize
Kd = 3 #  the Constant 'K' for the 'd' derivative term

count = 0
for count in range(Ns):    
   error = gyro_sensor.angle() # proportional 
   if (error == 0): # prevent the integral term from 'overshooting'
       integral = 0
   else:
       integral = integral + error    
   derivative = error - lastError  
   
   correction = (Kp*(error) + Ki*(integral) + + Kd*derivative) * -1
   
   robot.drive(Ts, correction)

   lastError = error  
   
   count = count + 1

robot.stop()

end = time.time()
time = end - start

Kc = Kp
dT = time / count

print("Loop time: " + str(time))
print("Loop iterations: " + str(count))

Kp = 0.60 * Kc 
Ki =  2 * Kp * dT / Pc
Kd = Kp * Pc / (8 * dT)

print("inputs: Kc=" + str(Kc) + "; dT=" + str(dT) + "; Pc=" + str(Pc))
print("recommended PID parms: Kp=" + str(Kp) + "; Ki=" + str(Ki) + "; Kd=" + str(Kd))
```

* results for our virtual robot:

```
Loop start
Loop time: 5.113999843597412
Loop iterations: 200
time per loop (dT): 0.02556999921798706
inputs: Kc=3; dT=0.02556999921798706; Pc=0.5
recommended PID parms: Kp=1.8; Ki=0.1841039943695068; Kd=4.39968726791601
```

8. Run the robot and see how it behaves.

9. Modify the Kp, Ki and Kd values to improve perfomance. You can start with fairly big tweaks, say 30% then try smaller tweaks to get the acceptable performance.

10. Once you have a good set of K's, increase the robot's straight speed by increasing the Tp value.

11. Modify the K values, or if necessary, go back to step 1 and repeat the entire process for the new Tp value.

12. Keep repeating until the robot's behavior is acceptable. 


## References
  * J. Sluka's excellent article: [A PID Controller For Lego Mindstorms Robots](http://www.inpharmix.com/jps/PID_Controller_For_Lego_Mindstorms_Robots.html)
  * [PID Line Follower Code by Using MicroPython 2.0](https://thecodingfun.com/2020/06/16/lego-mindstorms-ev3-pid-line-follower-code-by-using-micropython-2-0/)
  * [Pybricks Porportional Line Follower](https://pybricks.github.io/ev3-micropython/examples/robot_educator_line.html)
  * Mark Lucking's [MicroPython Tutorial XII](https://marklucking.medium.com/micropython-tutorial-xii-15b1cf4d7a51)
  * Builderdude35's [PID Line Follower for EV3 - The Ultimate Line Follower!](https://www.youtube.com/watch?v=AMBWV_HGYj4)

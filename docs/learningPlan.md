# Learning Plan (Work In Progress)

Goals:
A. Navigation
1. Basic: straight, 90degree turns, maze
2. Faster: straight, gradual turns, maze
3. Accurate: motor and gyro sensors
4. Line Following: 
   * straight, turns and maze using - color sensor
   * squaring on lines - using color sensor and gyro
5. Reliability & attachments
6. Other sensors (touch, ultrasonic, infrared)

-----

# A. Navigation
## LP01 - Basic
* MicroPython: 
  * robot.straight(), robot.turn()
* Drive straight
* Turns: 90degree
* Navigate maze

## LP02a - Faster
* MicroPython: 
  * Fix DriveBase wheel_diameter and axle_track settings ([Measuring and validating the robot dimensions](https://docs.pybricks.com/en/latest/robotics.html#pybricks.robotics.DriveBase.reset))
    * class DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
  * settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)
* Faster
  * Going straight - using robot.settings()
  * Turns - using arc (smooth/swing) turns (gradual) vs spin (point) turns (90deg)
    * [Types of turn](https://www.youtube.com/watch?v=_1r6sVXjClU)
      * spin - rotate on point between wheels (counter-rotating wheels)
      * pivot - one wheel stationary
      * smooth 
        * both wheels turn, one turns faster.
        * rotates about a point outside itself
        * bigger difference in power makes for a sharrper turn
    * [Radius Turns](https://sites.google.com/site/ev3basic/ev3-basic-programming/going-further/writerbot-v1/drawing-arcs)
  * Maze

## LP02b - Faster Turns, Straight using acceleration and deceleration
* MicroPython: 
  * while loop 
  * robot.reset(), robot.distance() and robot.drive()
  * print statements to debug robot.distance()
* Faster2  
  * robot.drive()
    * Turns: swing turns 
  * Navigate maze

## LP02c - Variable Speed Navigation
   * MicroPython: 
     * introduce functions
  * Acceleration and decceleration
    * settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)
    * test: push stacks of legos to a circle
  * robot.drive() without while loop - using 'wait(milliseonds)'

## LP03a - Accurate    
* MicroPython: 
  * robot.angle() - Accumulated angle since last reset
    * update [LearningPlanCode/LP03_squarePerimeter.py](LearningPlanCode/LP03_squarePerimeter.py) with while loop and robot.angle()
  * robot.reset() - Resets the estimated driven distance and angle to 0.
  * functions - replace duplicate code
* Turns
  * 90 degree (point turn - dual wheel counter-rotation; swing turn - outside wheel only turn)
* follow the perimiter of square

## LP03b - Gyro    
* MicroPython: 
  * gyro.angle() - Rotation angle. (with lag)
  * gyro.reset_angle(angle) - Value to which the angle should be reset. 
* Turns
  * 90 degree (swing turn; outside wheel only turn)
  * follow the perimiter of square  [Program Accurate 90 Degree Turns with the EV3 Gyro Sensor](https://www.youtube.com/watch?v=8B1LwzkLKXs)
* Straight line 
  * Micropython 
    * [XI use odometry to figure how much your robot strayed from straight line](https://medium.com/@marklucking/micropython-tutorial-xi-26799f151c65)  
    * [XII fix gyro drift when driving a straight line](https://medium.com/@marklucking/micropython-tutorial-xii-15b1cf4d7a51)
  * EV3-G:
    * [How to Make your Robot Drive Straight with the EV3 Gyro](https://www.youtube.com/watch?v=qPE4YNsTad4)
    * [EV3 Gyro Sensor + PID Algorithm = Extremely Accurate Drive Straight Program](https://www.youtube.com/watch?v=U-LdBQ-vBkg&t=140s)) 
    * [Gyro Following - More Accurately Control your FLL Robot](https://www.youtube.com/watch?v=WR_gy0NIBOs)
* Navigate maze/line maze

## LP03c - Make Gyro More Accurate 
* [Calibration vs Reset](https://www.youtube.com/watch?v=7V16AEW3GG4)
* [lag](https://ev3lessons.com/en/ProgrammingLessons/advanced/GyroTurn.pdf) vs [drift](https://ev3lessons.com/en/ProgrammingLessons/advanced/GyroDrift.pdf)
  * lag = gyro sensor readings lag behind the true value	
  * drift = readings keep changing even when the robot is still (calibrate gyro to fix)


    
## LP04a - Line Following
* MicroPython: 
  * loops and more elaborate conditionals
* Color sensor
  * 2-level & 3-level line follower
    * Straight line
    * Turns
    * Navigate curvy loops
* Basic Line Follower
  * [ev3lessons](https://ev3lessons.com/en/ProgrammingLessons/beginner/BasicLineFollower.pdf)
* Challenge
  * stop after
    * a certain distance
    * touch sensor pressed
    * certain angle has been reached
* Resources  
  * [Line Following Tiles](https://pybricks.github.io/ev3-micropython/_downloads/linefollowtiles.pdf) (pdf)

## LP04b - EV3 Micropython Proportional Algorithm
* Color sensor
  * Proportional line follower
    * Straight line 
    * Turns
    * Navigate line maze    
* Proportional Line Follower
  * ev3lessons
    * [Proportional](https://ev3lessons.com/en/ProgrammingLessons/advanced/ProportionalLineFollower.pdf)
    * [PID](https://ev3lessons.com/en/ProgrammingLessons/advanced/PID.pdf)
    * [Compare](https://ev3lessons.com/en/ProgrammingLessons/advanced/LineFollower.pdf)
  * Builderdude35
    * [Proportional](https://www.youtube.com/watch?v=uPFfevfpMxs&t=1s)
  * Micropython
    * [Pybricks Line Follower](https://pybricks.github.io/ev3-micropython/examples/robot_educator_line.html)
    * [PID Line Follower Code by Using MicroPython 2.0](https://thecodingfun.com/2020/06/16/lego-mindstorms-ev3-pid-line-follower-code-by-using-micropython-2-0/)
  
## LP04c - Squaring on lines
* Color sensor
  * Calibration
  * [Squaring on lines (aligning on a line)](https://ev3lessons.com/en/ProgrammingLessons/advanced/Align.pdf)

## LP04d - combining line following and gyro
* [LAGS Algorithm - Line Assisted Gyro Steering (Brickwolves Waring FLL)](https://www.youtube.com/watch?v=WQH720LQAB0)

## LP05- Reliability and attachments
* Reliability
  * [Robot Design](http://www.highlandersfrc.com/NewsEventPages/FLL%20Programming%20and%20Design.pdf)
  * Motor Calibration
    * Hardware - how to see if there is an issue
      * drive straight for long distance; travel around a square many time in both directions
      * [Calibrate wheels](https://techbrick.com/techbrick/Lego/TechBrick/TechTips/NXTCalibration/)
    * Software 
      * [How to Make your FLL Robot Drive Straight - EV3 Motor Encoders](https://www.youtube.com/watch?v=b2jkjiY-HQA)
* Attachments
  * [Worm gear](https://www.youtube.com/watch?v=TQ9hQ_ZXwmM)
  * [Dog gear](https://www.youtube.com/watch?v=NZbt3tnySyI)
* How to organize your programs on the EV3 for competition
  * master/sequencer program?
  * [Micropython program startup lag](https://github.com/fll-pigeons/gamechangers/issues/6)

## LP06 - Robot Design
* [Our World Record Robot (680 points!) - Brickwolves Waring FLL](https://www.youtube.com/watch?v=9DzS0jlQDBM&feature=youtu.be)

## LP07- Other Sensors
* basic sensors:
  * UltrasonicSensor
  * TouchSensor
* MicroPython: looping & conditionals (while and if statements)
* Touch and Ultrasonic sensor
  * Drive straight
  * Turns
  * Navigate maze
  * Combo navigation: [Ultrasonic to follow wall](https://pybricks.github.io/ev3-micropython/examples/robot_educator_ultrasonic.html#obstacle-avoidance); touch to initiate turn

-------

[learningPlanResearch](learningPlanResearch.md)

--------

# Log
> #### 4 Aug - watched kickoff; read mission rules; started mission M14_health_units 
> #### 30 July - 3-level line following; intro to PID line following; did not work as expected - forgot to update DriveBase parms with new larger wheels 
> #### 28 July - Finish second robot; Basic 2-level line following
> #### 23 July - Review micropython gyro code; continue build of 2d robot
> #### 21 July - Build 2nd robot; review Micropython Navigation
> #### 14 July - [Faster Maze nagivator with smooth turns](https://www.youtube.com/embed/BTB1U915fSM) - [Updated program: LP02_smoothTurns.py]LearningPlanCode/LP02_smoothTurns.py)
> #### 10 July - Basic Movement
> Measured and validated robot dimensions; Drove faster using Micropython's settings() command combined with straight() and turn(); started curved turns with drive() command and introduced Python loops.  Had problems with making while loop conditional on robot.distance() < n, where n was desired distance - did not run reset() command immediately before while loop conditional (otherwise measures distance from start of program).
> #### 2 July - Maze nagivator
> Learned how to navigate robot out and back, and through simple maze, using Micropython's straight() and turn() commands.





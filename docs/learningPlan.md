# Learning Plan (Work In Progress)

Goals:
A. Navigation
1. Basic: straight, 90degree turns, maze
2. Faster: straight, gradual turns, maze
3. Accurate: motor and gyro sensors
4. Line Following: 
   a. straight, turns and maze using - color sensor
   b. squaring on lines - using color sensor and gyro
5. Other sensors (touch, ultrasonic, infrared)

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
  * Turns - using gradual turns ([Types of turn](https://www.youtube.com/watch?v=_1r6sVXjClU))
  * Maze

## LP02b - Faster Turns, Straight using acceleration and deceleration
* MicroPython: 
  * while loop 
  * robot.reset(), robot.distance() and robot.drive()
  * print statements to debug robot.distance()
* Faster2  
  * robot.drive()
    * Turns: Gradual turns turns 
    * acceleration and deceleration
  * Navigate maze

## LP02c - Variable Speed Navigation
  * Acceleration and decceleration
    * settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)
    * where used: push stacks of legos to a circle
  * robot.drive() without while loop - using 'wait(seconds)'
  
## LP03a - Accurate    
* MicroPython: 
  * robot.angle()
* using Motor sensor to introducing looping: robot.angle()  
* Turns
  * 90 degree (spin turn (dual wheel counter-rotation); outside wheel only turn)
* Straight line 
* follow the perimiter of square

## LP03b - Gyro    
* MicroPython: 
  * gyro.angle()
* Turns
  * 90 degree (spin turn; outside wheel only turn)
  * follow the perimiter of square  [Program Accurate 90 Degree Turns with the EV3 Gyro Sensor](https://www.youtube.com/watch?v=8B1LwzkLKXs)
* Straight line 
  * Micropython [XI](https://medium.com/@marklucking/micropython-tutorial-xi-26799f151c65)  [XII fix gyro drift when driving a straight line](https://medium.com/@marklucking/micropython-tutorial-xii-15b1cf4d7a51)
  * EV3-G:
    * [How to Make your Robot Drive Straight with the EV3 Gyro](https://www.youtube.com/watch?v=qPE4YNsTad4)
    * [EV3 Gyro Sensor + PID Algorithm = Extremely Accurate Drive Straight Program](https://www.youtube.com/watch?v=U-LdBQ-vBkg&t=140s))  
* Navigate maze/line maze

## LP03c - Make Gyro More Accurate 
* MicroPython: 
  * gyro.angle()
* Gyro sensor: 
* [Calibration vs Reset](https://www.youtube.com/watch?v=7V16AEW3GG4)
* [lag](https://ev3lessons.com/en/ProgrammingLessons/advanced/GyroTurn.pdf) vs [drift](https://ev3lessons.com/en/ProgrammingLessons/advanced/GyroDrift.pdf)
  * lag = gyro sensor readings lag behind the true value	
  * drift = readings keep changing even when the robot is still (calibrate gyro to fix)
    * [using Odometry](https://medium.com/@marklucking/micropython-tutorial-xi-26799f151c65)

## LP03c - Motor Calibration
  * Hardware
  * Software

## LP04a - Line Following
* MicroPython: 
  * loops and more elaborate conditionals
* Color sensor
  * 2-level & 3-level line follower
    * Straight line
    * Turns
    * Navigate curvy loops
  * [Line Following Tiles](https://pybricks.github.io/ev3-micropython/_downloads/linefollowtiles.pdf)

## LP04b - EV3 Micropython Proportional Algorithm
* Color sensor
  * Proportional line follower
    * Straight line 
    * Turns
    * Navigate line maze    
* Example using Micropython
    * [PID Line Follower Code by Using MicroPython 2.0](https://thecodingfun.com/2020/06/16/lego-mindstorms-ev3-pid-line-follower-code-by-using-micropython-2-0/)
  
## LP04c - Squaring on lines
* Color sensor
  * Calibration
  * [Squaring on lines (aligning on a line)](https://ev3lessons.com/en/ProgrammingLessons/advanced/Align.pdf)

## LP05 - Other Sensors
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
> #### 2 July - Maze nagivator
> Learned how to navigate robot out and back, and through simple maze, using Micropython's straight() and turn() commands.
> #### 10 July - Basic Movement
> Measured and validated robot dimensions; Drove faster using Micropython's settings() command combined with straight() and turn(); started curved turns with drive() command and introduced Python loops.  Had problems with making while loop conditional on robot.distance() < n, where n was desired distance - did not run reset() command immediately before while loop conditional (otherwise measures distance from start of program).
> #### 14 July - [Faster Maze nagivator with smooth turns](https://www.youtube.com/embed/BTB1U915fSM) - [Updated program: LP02_smoothTurns.py](https://github.com/fll-pigeons/gamechangers/blob/master/programs/LP02_smoothTurns.py)


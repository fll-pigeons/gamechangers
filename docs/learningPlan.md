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

#################################################################################################

# A. Navigation
## LP01 - Basic
* MicroPython: straight(), turn()
* Drive straight
* Turns Using DriveBase - using 90degree turns
* Navigate maze

## LP02a - Faster
* MicroPython: 
  * Fix DriveBase settings ([Measuring and validating the robot dimensions](https://docs.pybricks.com/en/latest/robotics.html#pybricks.robotics.DriveBase.reset))
    * wheel_diameter=55.5, 
    * axle_track=104
  * settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)
* Faster
  * Going straight - using settings()
  * Turns - using gradual turns ([Types of turn](https://www.youtube.com/watch?v=_1r6sVXjClU))
  * Maze

## LP02b - Faster Turns, Straight using acceleration and deceleration
* Turns: Gradual turns turns with robot.drive():
  * debug robot.distance() with print statements
  * While loop and robot.reset(), robot.distance() and robot.drive()
* Navigate maze
* using Motor sensor to introducing looping: robot.angle()

## LP03 - Accurate
* Gyro sensor: gyro.angle()
* [Calibration vs Reset](https://www.youtube.com/watch?v=7V16AEW3GG4)
* [lag](https://ev3lessons.com/en/ProgrammingLessons/advanced/GyroTurn.pdf) vs [drift](https://ev3lessons.com/en/ProgrammingLessons/advanced/GyroDrift.pdf)
* Straight line 
  * ( [Use the gyro to correct any drift when driving in a straight line](https://medium.com/@marklucking/micropython-tutorial-xii-15b1cf4d7a51) )
  * [How to Make your Robot Drive Straight with the EV3 Gyro](https://www.youtube.com/watch?v=qPE4YNsTad4)
  * ([EV3 Gyro Sensor + PID Algorithm = Extremely Accurate Drive Straight Program](https://www.youtube.com/watch?v=U-LdBQ-vBkg&t=140s))
* Turns ( [Program Accurate 90 Degree Turns with the EV3 Gyro Sensor](https://www.youtube.com/watch?v=8B1LwzkLKXs) )
  * 90 degree
  * follow the perimiter of square
  * gradual turns
* Navigate maze/line maze

## LP04a - Line Following
* Color sensor
  * 2-level & 3-level line follower
    * Straight line
    * Turns
    * Navigate curvy loops
  * [Line Following Tiles](https://pybricks.github.io/ev3-micropython/_downloads/linefollowtiles.pdf)

## LP04b - Using Built-In EV3 Micropython PID Algorithm - More Accurate Nagivation
* Color sensor
  * Calibration
  * Proportional line follower
    * Straight line 
    * Turns
    * Navigate line maze    
* Examples using Micropython
    * [PID Line Follower Code by Using MicroPython 2.0](https://thecodingfun.com/2020/06/16/lego-mindstorms-ev3-pid-line-follower-code-by-using-micropython-2-0/)
  
## LP04c - Squaring on lines
* [Squaring on lines](https://ev3lessons.com/en/ProgrammingLessons/advanced/Align.pdf)

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

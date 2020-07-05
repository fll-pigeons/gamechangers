# Learning Plan (Work In Progress)

# A. Software

## Basic Navigation: No Feedback - No sensors 
* MicroPython: straight(), turn()
* Drive straight
* Turns Using DriveBase
* Navigate maze

## Basic Navigation: No Feedback - No sensors 
* Math: tables and plotting them on graph
* MicroPython: settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)
* Drive straight - faster
* Turns - [Types of turn](https://www.youtube.com/watch?v=_1r6sVXjClU)
  * Curved turns
* Navigate maze

## Navigation: Using Basic Sensors
* Math: simple functions and plotting them on graph
* ~~Touch sensor~~
* what is a robot?: using feedback and reacting to it
* MicroPython: if statement
* Ultrasonic sensor
  * Drive straight
  * Turns
  * Navigate maze

## Navigation Using Improved Feedback - Color sensor
* Math:  functions and plotting them on graph (and understanding slope)
* MicroPython: Loop statement
* Color sensor
  * 2-level line follower
    * Straight line
    * Turns
    * Navigate line maze
  * 3-level line follower
    * Straight line
    * Turns
    * Navigate line maze

## Navigation - Gyro sensor
* Gyro sensor (think of it as a virtual line follower)
  * Math: functions, slopes and graphs
  * 2-level Logic
    * Straight line
    * Turns
    * Navigate line maze
  * 3-level Logic
    * Straight line
    * Turns
    * Navigate line maze

## Using Simple Algorithm - More Accurate Nagivation
* Color sensor
  * Proportional line follower
    * Straight line ( [EV3-G - How to Make your Robot Drive Straight with the EV3 Gyro using proportional logic](https://www.youtube.com/watch?v=qPE4YNsTad4) )
    * Turns
    * Navigate line maze    
* Gyro sensor
  * Proportional Logic
    * Straight line ( [Use the gyro to correct any drift when driving in a straight line](https://medium.com/@marklucking/micropython-tutorial-xii-15b1cf4d7a51) )
    * Turns ( [Program Accurate 90 Degree Turns with the EV3 Gyro Sensor](https://www.youtube.com/watch?v=8B1LwzkLKXs) )
    * Navigate line maze   
  
## Using Better Algorithms - Most Accurate Nagivation
(see: J. Sluka's [A PID Controller For Lego Mindstorms Robots](http://www.inpharmix.com/jps/PID_Controller_For_Lego_Mindstorms_Robots.html) )

### Color sensor
* Proportional Integral line follower
  * Straight line
  * Turns
  * Navigate line maze   
  
* PID (Proportional Integral Derivative) line follower 
( [Control class - Class to interact with PID controller and settings.](https://pybricks.github.io/ev3-micropython/motors.html) )
  * Straight line
  * Turns
  * Navigate line maze
    
* Examples using Micropython
    * [PID Line Follower Code by Using MicroPython 2.0](https://thecodingfun.com/2020/06/16/lego-mindstorms-ev3-pid-line-follower-code-by-using-micropython-2-0/)
    
* Examples using Lego LabVIEW: 
    * [Finding line on the mat](http://flltutorials.com/translations/en-us/RobotGame/FindingLines.pdf)
    * [Proportional line follower - Builderdude35](https://www.youtube.com/watch?v=uPFfevfpMxs)
    * [PID Line Follower for EV3 - The Ultimate Line Follower!](https://www.youtube.com/watch?v=AMBWV_HGYj4)
    * [What is the Best EV3 Line Follower For You?](https://www.youtube.com/watch?v=P50CE0xwhvo)

### Gyro sensor
  * PID (Proportional Integral Derivative) line follower 
    * Straight line 
      * [How to Make your Robot Drive Straight with the EV3 Gyro](https://www.youtube.com/watch?v=qPE4YNsTad4) 
      * ([EV3 Gyro Sensor + PID Algorithm = Extremely Accurate Drive Straight Program](https://www.youtube.com/watch?v=U-LdBQ-vBkg&t=140s))
    * Turns
    * Navigate line maze

# B. Hardware

### Attachements
* [Worm Gear](https://www.youtube.com/watch?v=TQ9hQ_ZXwmM)
* [Dog Gear](https://www.youtube.com/watch?v=NZbt3tnySyI)



-------------

## Resources    

* [Mark Lucking](https://medium.com/@marklucking/micropython-mix-9012b79e91f3?source=rss-------1) tutorials
* [Line Following Tiles](https://robotsquare.com/2012/11/28/line-following/)




# Log
> #### 2 July - Maze nagivator
> Learned how to navigate robot out and back, and through simple maze, using Micropython's straight() and turn() commands.

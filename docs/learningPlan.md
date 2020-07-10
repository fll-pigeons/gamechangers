# Learning Plan (Work In Progress)

# A. Software

## LP01 - Basic Navigation: No Feedback - No sensors -> done
* MicroPython: straight(), turn()
* Drive straight
* Turns Using DriveBase
* Navigate maze

## LP02a - Basic Navigation: No Feedback - No sensors -> done
* [Measuring and validating the robot dimensions](https://docs.pybricks.com/en/latest/robotics.html#pybricks.robotics.DriveBase.reset)
* MicroPython: 
  * Fix DriveBase settings: 
    * wheel_diameter=55.5, 
    * axle_track=104
  * settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)
* Drive straight - faster
* Curved turns 
  * [Types of turn](https://www.youtube.com/watch?v=_1r6sVXjClU)
* Navigate maze

## LP02b - Basic Navigation: Minimal Feedback - Use wheels as sensors
* Math: tables and plotting them on graph
* what is a robot?: using feedback and reacting to it
* Smooth turns with robot.drive():
  * debug robot.distance() with print statements
  * While loop and robot.reset(), robot.distance() and robot.drive()
* Navigate maze

## LP03 - Navigation: Using Basic Sensors
* Math: tables, simple functions and plotting them on graph
* basic sensors:
  * UltrasonicSensor
  * TouchSensor
* MicroPython: looping & conditionals (while and if statements)
* Touch and Ultrasonic sensor
  * Drive straight
  * Turns
  * Navigate maze
  * Combo navigation: [Ultrasonic to follow wall](https://pybricks.github.io/ev3-micropython/examples/robot_educator_ultrasonic.html#obstacle-avoidance); touch to initiate turn

## LP04 - Navigation Using Improved Feedback - Color sensor
* Math: functions and plotting them on graph (and understanding slope)
* MicroPython: looping & conditionals (while and if statements)
* Color sensor
  * 2-level & 3-level line follower
    * Straight line
    * Turns
    * Navigate curvy loops
  * [Line Following Tiles](https://robotsquare.com/2012/11/28/line-following/)

## LP06 - Using Simple Algorithm - More Accurate Nagivation
* Math: explain Proportional follower using functions, slopes and graphs
* Color sensor
  * Proportional line follower
    * Straight line 
    * Turns
    * Navigate line maze    

## LP07 - Navigation - Gyro sensor
* Gyro sensor
  * Math: functions, graphs and slope 
  * 2-level and 3-level Logic
    * Move straight
    * Turns
    * Navigate board maze
  * Proportional Logic
    * [EV3-G - How to Make your Robot Drive Straight with the EV3 Gyro using proportional logic](https://www.youtube.com/watch?v=qPE4YNsTad4)
    * Straight line ( [Use the gyro to correct any drift when driving in a straight line](https://medium.com/@marklucking/micropython-tutorial-xii-15b1cf4d7a51) )
    * Turns ( [Program Accurate 90 Degree Turns with the EV3 Gyro Sensor](https://www.youtube.com/watch?v=8B1LwzkLKXs) )
    * Navigate line maze   


## LP08 - Understanding PyBrick MicroPython PID algorithm - Most Accurate Nagivation
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
> #### 10 July - Basic Movement
> Measured and validated robot dimensions; Drove faster using Micropython's settings() command combined with straight() and turn(); started curved turns with drive() command and introduced Python loops.  Had problems with making while loop conditional on robot.distance() < n, where n was desired distance - did not run reset() command immediately before while loop conditional (otherwise measures distance from start of program).

# Learning Plan

## 1. Basic Movement
### No Feedback -No sensors 
 
* Drive straight
* Turns; [Types of turn](https://www.youtube.com/watch?v=_1r6sVXjClU)
  * using individual motor control - experiment with different power ratios
  * using DriveBase
* Navigate maze
     
### With Rudimentary Feedback - Using Basic Sensors
 
* Touch sensor
  * Drive straight
  * Turns
  * Navigate maze    

* Ultrasonic sensor
  * Drive straight
  * Turns
  * Navigate maze

## 2. Using Improved Feedback - More Accurate Movement Using Sensors

### Simple programming

* Color sensor
  * 2-level line follower
    * Straight line
    * Turns
    * Navigate line maze

  * 3-level line follower
    * Straight line
    * Turns
    * Navigate line maze
    
  * Proportional line follower
    * Straight line ( [EV3-G - How to Make your Robot Drive Straight with the EV3 Gyro using proportional logic](https://www.youtube.com/watch?v=qPE4YNsTad4) )
    * Turns
    * Navigate line maze    
    
* Gyro sensor
  * Proportional Logic
    * Straight line ( [Use the gyro to correct any drift when driving in a straight line](https://medium.com/@marklucking/micropython-tutorial-xii-15b1cf4d7a51) )
    * Turns ( [Program Accurate 90 Degree Turns with the EV3 Gyro Sensor](https://www.youtube.com/watch?v=8B1LwzkLKXs) )
    * Navigate line maze   
  
## 3. Using Algorithm And Sensors - Most Accurate Nagivation
(see: J. Sluka's [A PID Controller For Lego Mindstorms Robots](http://www.inpharmix.com/jps/PID_Controller_For_Lego_Mindstorms_Robots.html) )

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
    * [EV3 Gyro Sensor + PID Algorithm = Extremely Accurate Drive Straight Program](https://www.youtube.com/watch?v=U-LdBQ-vBkg&t=140s)

## Resources    

* ([Mark Lucking](https://medium.com/@marklucking/micropython-mix-9012b79e91f3?source=rss-------1) tutorials)
* [Line Following Tiles](https://robotsquare.com/2012/11/28/line-following/)




# Log
> #### 2 July - Maze nagivator
> Learned how to navigate robot out and back, and through simple maze, using Micropython's straight() and turn() commands.

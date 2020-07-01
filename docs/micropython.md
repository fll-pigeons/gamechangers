# MicroPython - Cheat sheet (Work in progess)

### Documentation

  * [LEGO® MINDSTORMS Education EV3 MicroPython](https://pybricks.github.io/ev3-micropython/index.html) (pybricks github.io documentation)
    * Specific to EV3
    * Many sample programs
      * [ROBOT EDUCATOR PROGRAMS](https://pybricks.github.io/ev3-micropython/index.html)
        * [Basic Movement](https://pybricks.github.io/ev3-micropython/examples/robot_educator_basic.html)
        * [Obstacle Avoidance](https://pybricks.github.io/ev3-micropython/examples/robot_educator_ultrasonic.html)
        * [Line Following](https://pybricks.github.io/ev3-micropython/examples/robot_educator_line.html)
      * [CORE SET PROGRAMS](https://pybricks.github.io/ev3-micropython/index.html)
      * [EXPANSION SET PROGRAMS](https://pybricks.github.io/ev3-micropython/index.html)
  * ~~[Pybricks](https://docs.pybricks.com/en/latest/index.html) (pybricks.com documentation)~~
    *  ~~not just for EV3 - Docs for [Lego Technics Power Up](https://racingbrick.com/lego-powered-up-summary/) - beta only! (this is *not* support for Lego's new [Mindstorms Robot Inventor](https://www.lego.com/en-us/aboutus/news/2020/june/lego-mindstorms-robot-inventor/) kit, which is scheduled for release Aug 2020)~~
 
# MicroPython Motor Commands:
  * [robotics module:](https://docs.pybricks.com/en/latest/robotics.html)
    * [DriveBase class](https://docs.pybricks.com/en/latest/robotics.html)
        *  Driving for a given distance or by an angle
           * [straight(distance)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.straight)
           * turn(angle)
           * settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)
        * Drive forever
            * drive(drive_speed, turn_rate)
            * stop()
        * Advanced Settings
            * distance_controlheading_control
            * heading_control
  * [ev3devices module:](https://pybricks.github.io/ev3-micropython/ev3devices.html#motors)
    * [Motor class - control motors with built-in rotation sensors](https://pybricks.github.io/ev3-micropython/ev3devices.html#motors)
   
   
# PID - Advanced   
   * [Control class - Class to interact with PID controller and settings.](https://pybricks.github.io/ev3-micropython/motors.html) 

## what is PID?:

  * PID = Proportional-Integral-Derivative feedback control
  * Examples using Lego LabVIEW: 
      * Finding line on the mat: [Tutorial](http://flltutorials.com/translations/en-us/RobotGame/FindingLines.pdf)
      * [Proportional line follower - Builderdude35](https://www.youtube.com/watch?v=uPFfevfpMxs)
      * [PID Line Follower for EV3 - The Ultimate Line Follower!](https://www.youtube.com/watch?v=AMBWV_HGYj4)
      * [What is the Best EV3 Line Follower For You?](https://www.youtube.com/watch?v=P50CE0xwhvo)

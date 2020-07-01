# MicroPython - Cheat sheet (Work in progess)

### Documentation

  * [LEGO® MINDSTORMS Education EV3 MicroPython](https://pybricks.github.io/ev3-micropython/index.html) (pybricks github.io documentation)
    * Specific to EV3
    * Many sample programs
      * ROBOT EDUCATOR PROGRAMS
        * [Basic Movement](https://pybricks.github.io/ev3-micropython/examples/robot_educator_basic.html)
        * [Obstacle Avoidance](https://pybricks.github.io/ev3-micropython/examples/robot_educator_ultrasonic.html)
        * [Line Following](https://pybricks.github.io/ev3-micropython/examples/robot_educator_line.html)
      * CORE SET PROGRAMS
      * EXPANSION SET PROGRAMS
  * [Pybricks](https://docs.pybricks.com/en/latest/index.html) (pybricks.com documentation)
    *  not just for EV3 - Docs for [Lego Technics Power Up](https://racingbrick.com/lego-powered-up-summary/) - beta only! (this is not support for [Lego's Mindstorms Robot Inventor](https://www.lego.com/en-us/aboutus/news/2020/june/lego-mindstorms-robot-inventor/) kit)
 
* MicroPython Motor Commands:
   * [DriveBase class - Driving for a given distance or by an angle](https://docs.pybricks.com/en/latest/robotics.html) (uses two PIDs controllers: one to control the heading and one to control the traveled distance.)
   * [Motor class - PID control to accurately track your commanded target angles](https://pybricks.github.io/ev3-micropython/ev3devices.html#motors)
   * [Control class - Class to interact with PID controller and settings.](https://pybricks.github.io/ev3-micropython/motors.html) 

### what is PID?:

  * PID = Proportional-Integral-Derivative feedback control
  * Examples using Lego LabVIEW: 
      * Finding line on the mat: [Tutorial](http://flltutorials.com/translations/en-us/RobotGame/FindingLines.pdf)
      * [Proportional line follower - Builderdude35](https://www.youtube.com/watch?v=uPFfevfpMxs)
      * [PID Line Follower for EV3 - The Ultimate Line Follower!](https://www.youtube.com/watch?v=AMBWV_HGYj4)
      * [What is the Best EV3 Line Follower For You?](https://www.youtube.com/watch?v=P50CE0xwhvo)

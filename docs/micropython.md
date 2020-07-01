# MicroPython - Cheat sheet

## Documentation

  * [LEGO® MINDSTORMS Education EV3 MicroPython](https://pybricks.github.io/ev3-micropython/index.html)
 
## Motors:
  * [robotics module:](https://docs.pybricks.com/en/latest/robotics.html)
    * [DriveBase class](https://docs.pybricks.com/en/latest/robotics.html) - for driving the robot
        *  Driving for a given distance or by an angle
           * [straight(distance)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.straight)
           * [turn(angle)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.turn)
           * [settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.settings)
        * Drive forever
            * [drive(drive_speed, turn_rate)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.drive)
            * [stop()](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.stop)
  * [ev3devices module:](https://pybricks.github.io/ev3-micropython/ev3devices.html#motors)
    * [Motor class](https://pybricks.github.io/ev3-micropython/ev3devices.html#motors) - for accurate control of attachment motor
        * control motors with built-in rotation sensors
            * Stopping
               * [stop()](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.stop)
               * [brake()](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.brake)
               * [hold()](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.hold)
            * Action
                * [run(speed)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.run)
                * [run_time(speed, time, then=Stop.HOLD, wait=True)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.run_time)
                * [run_angle(speed, rotation_angle, then=Stop.HOLD, wait=True)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.run_angle)
                * [run_target(speed, target_angle, then=Stop.HOLD, wait=True)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.run_target)
                * [run_until_stalled(speed, then=Stop.COAST, duty_limit=None)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.run_until_stalled)

## Sensors
  * [ev3devices module:](https://pybricks.github.io/ev3-micropython/ev3devices.html#motors)
    * [classColorSensor(port)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.ColorSensor)
    * [classInfraredSensor(port)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.InfraredSensor)
    * [classUltrasonicSensor(port)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.UltrasonicSensor)
    * [classGyroSensor(port, positive_direction=Direction.CLOCKWISE)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.GyroSensor)
       * [Gyro Following - More Accurately Control your FLL Robot](https://www.youtube.com/watch?v=WR_gy0NIBOs)
       * [Program Accurate 90 Degree Turns with the EV3 Gyro Sensor](https://www.youtube.com/watch?v=8B1LwzkLKXs)

## Sample programs
  * [ROBOT EDUCATOR PROGRAMS](https://pybricks.github.io/ev3-micropython/index.html)
    * [Basic Movement](https://pybricks.github.io/ev3-micropython/examples/robot_educator_basic.html)
    * [Obstacle Avoidance](https://pybricks.github.io/ev3-micropython/examples/robot_educator_ultrasonic.html)
    * [Line Following](https://pybricks.github.io/ev3-micropython/examples/robot_educator_line.html)
  * [CORE SET PROGRAMS](https://pybricks.github.io/ev3-micropython/examples/color_sorter.html)
  * [EXPANSION SET PROGRAMS](https://pybricks.github.io/ev3-micropython/examples/elephant.html)
      
## Advanced   
  * PID = Proportional-Integral-Derivative feedback control - more accurate travel or line following
     * [Control class - Class to interact with PID controller and settings.](https://pybricks.github.io/ev3-micropython/motors.html) 
  * Examples using Lego LabVIEW: 
      * [Finding line on the mat](http://flltutorials.com/translations/en-us/RobotGame/FindingLines.pdf)
      * [Proportional line follower - Builderdude35](https://www.youtube.com/watch?v=uPFfevfpMxs)
      * [PID Line Follower for EV3 - The Ultimate Line Follower!](https://www.youtube.com/watch?v=AMBWV_HGYj4)
      * [What is the Best EV3 Line Follower For You?](https://www.youtube.com/watch?v=P50CE0xwhvo)
      * [EV3 Gyro Sensor + PID Algorithm = Extremely Accurate Drive Straight Program](https://www.youtube.com/watch?v=U-LdBQ-vBkg&t=140s)

## other
  * ~~[Pybricks](https://docs.pybricks.com/en/latest/index.html) (pybricks.com documentation)~~
    *  ~~not just for EV3 - Docs for [Lego Technics Power Up](https://racingbrick.com/lego-powered-up-summary/) - beta only! (this is *not* support for Lego's new [Mindstorms Robot Inventor](https://www.lego.com/en-us/aboutus/news/2020/june/lego-mindstorms-robot-inventor/) kit, which is scheduled for release Aug 2020)~~

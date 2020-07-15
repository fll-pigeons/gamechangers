# Pybricks (MicroPython for EV3) - Cheat sheet

## Documentation

  * [LEGO® MINDSTORMS Education EV3 MicroPython](https://pybricks.github.io/ev3-micropython/index.html)
  * see also: [pybricks cheatsheet By FLL TechTacos](https://cheatography.com/flltech2019/cheat-sheets/pybricks-cheatsheet-by-fll-techtacos-sugarland/pdf/)
 
## Motors:

### [robotics module:](https://pybricks.github.io/ev3-micropython/robotics.html)

* Driving the Robot - Dual Motor Control ([DriveBase class](https://pybricks.github.io/ev3-micropython/robotics.html))

    *  Driving for a given distance or by an angle, and then stop
       * [straight(distance)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.straight) (blocking)
       * [turn(angle)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.turn) (blocking)
       * [settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.settings)
    * Drive forever (until a stop() or another drive() command, or until program ends)
        * [drive(drive_speed, turn_rate)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.drive) (to be used in a [loop](https://pybricks.github.io/ev3-micropython/examples/robot_educator_ultrasonic.html)) (non-blocking)
        * [stop()](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.stop) 

### [ev3devices module:](https://pybricks.github.io/ev3-micropython/ev3devices.html#motors)

* Single Motor/Attachment motor control ([Motor class](https://pybricks.github.io/ev3-micropython/ev3devices.html#motors))

  * control motors with built-in rotation sensors
    * Action
        * [run(speed)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.run)
        * [run_time(speed, time, then=Stop.HOLD, wait=True)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.run_time)
        * [run_angle(speed, rotation_angle, then=Stop.HOLD, wait=True)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.run_angle)
          * moves the wheels X degrees relative to their current angle.
        * [ run_target(speed, target_angle, then=Stop.HOLD, wait=True)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.run_target) 
          * moves the wheels X degrees until they reach an absolute angle you specify.       
    * Stopping
       * [stop()](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.stop)
       * [brake()](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.brake)
       * [hold()](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.hold)
/ev3devices.html#pybricks.ev3devices.Motor.run_angle)

## Sensors

* [ev3devices module:](https://pybricks.github.io/ev3-micropython/ev3devices.html#motors)
  * Basic:
    * [classTouchSensor(port)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.TouchSensor)
    * ([nxtdevices module](https://pybricks.github.io/ev3-micropython/nxtdevices.html)) [class UltrasonicSensor(port)](https://pybricks.github.io/ev3-micropython/nxtdevices.html#nxt-ultrasonic-sensor) 
    * [classInfraredSensor(port)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.InfraredSensor)
  * More accurate
    * [classColorSensor(port)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.ColorSensor)
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
      


## other
* ~~[Pybricks](https://pybricks.github.io/ev3-micropython/index.html) (pybricks.com documentation)~~
  *  ~~not just for EV3 - Docs for [Lego Technics Power Up](https://racingbrick.com/lego-powered-up-summary/) - beta only! (this is *not* support for Lego's new [Mindstorms Robot Inventor](https://www.lego.com/en-us/aboutus/news/2020/june/lego-mindstorms-robot-inventor/) kit, which is scheduled for release Aug 2020)~~

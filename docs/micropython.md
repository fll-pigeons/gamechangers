# Pybricks (MicroPython for Lego EV3) - Cheat sheet

## Documentation

  * [LEGO® MINDSTORMS Education EV3 MicroPython](https://pybricks.github.io/ev3-micropython/index.html)
  * see also: [pybricks cheatsheet By FLL TechTacos](https://cheatography.com/flltech2019/cheat-sheets/pybricks-cheatsheet-by-fll-techtacos-sugarland/pdf/)
 
## Motors:

### Driving the Robot - Dual Motor Control ([DriveBase class](https://pybricks.github.io/ev3-micropython/robotics.html))
* Drive straight then stop
  * [settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.settings) (modifies next straight() command)
  * [straight(distance)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.straight) (blocking - waits for command to complete before going to next command)
  * Turn in place, then stop   
    * [turn(angle)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.turn) - turn in place (blocking)
    
* Drive forever (until a stop() or another drive() command, or until program ends)
  * [drive(drive_speed, turn_rate)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.drive)  (non-blocking - goes to next command without waiting for this one to complete)
  * How to call drive:
    * drive then [wait(milliseconds)](https://pybricks.github.io/ev3-micropython/tools.html?highlight=wait#pybricks.tools.wait)
    * call drive many times inside [while loop](https://pybricks.github.io/ev3-micropython/examples/robot_educator_ultrasonic.html)
      * while ([distance()](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.distance < n or [angle()](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.angle) < 90):
        drive()
  * [reset()](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.reset) - remember reset distance and angle before testing in while loop  
    * [stop()](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.stop) 
    
----- 

# Single Motor/Attachment motor control ([Motor class](https://pybricks.github.io/ev3-micropython/ev3devices.html#motors))
* control motors with built-in rotation sensors
* Action
  * [run(speed)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.run)
    * Runs the motor at a constant speed, no stopping
  * [run_angle(speed, rotation_angle, then=Stop.HOLD, wait=True)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.run_angle)
    * moves the wheels X degrees relative to their current angle.
  * [run_target(speed, target_angle, then=Stop.HOLD, wait=True)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.run_target) 
    * moves the wheels X degrees until they reach an absolute angle you specify.       

* Stopping
  * [stop()](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.stop) - glide to a stop
  * [brake()](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.brake) - motor friction stop
   * [hold()](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.hold) - stop motor rotation and actively hold
* [reset_angle()](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.reset_angle) - Value to which the angle should be reset

----- 

# Sensors

* Basic:
  * [classTouchSensor(port)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.TouchSensor)
  * [class UltrasonicSensor(port)](https://pybricks.github.io/ev3-micropython/nxtdevices.html#nxt-ultrasonic-sensor) (from [nxtdevices module](https://pybricks.github.io/ev3-micropython/nxtdevices.html))
  * [classInfraredSensor(port)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.InfraredSensor)

* More accurate
  * [classColorSensor(port)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.ColorSensor)
  * [classGyroSensor(port, positive_direction=Direction.CLOCKWISE)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.GyroSensor)
    * [reset_angle()](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.reset_angle) - Value to which the angle should be reset
    * Gyro must be plugged to EV3 before power up.  Make sure brick does not move on power up.  Never plug in gyro to an already powered up EV3 brick - it messes up the calibration.

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

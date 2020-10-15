# Pybricks (MicroPython for Lego EV3) - Cheat sheet

## Documentation

  * [LEGO® MINDSTORMS Education EV3 MicroPython](https://pybricks.github.io/ev3-micropython/index.html)
  * see also: [pybricks cheatsheet By FLL TechTacos](https://cheatography.com/flltech2019/cheat-sheets/pybricks-cheatsheet-by-fll-techtacos-sugarland/pdf/)
 
## Motors:

### Driving the Robot - Dual Motor Control ([DriveBase class](https://pybricks.github.io/ev3-micropython/robotics.html))
* Drive straight or turn in place - then stop
  * [settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.settings) (modifies next straight or turn command)
  * [straight(distance)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.straight)
  * [turn(angle)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.turn) in place, then stop   
    
* Drive straight or turn - forever (until a stop() or another drive() command, or until program ends)
  * [drive(drive_speed, turn_rate)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.drive)
  * How to call drive:
    * drive() then [wait(milliseconds)](https://pybricks.github.io/ev3-micropython/tools.html?highlight=wait#pybricks.tools.wait), then [stop()](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.stop) 
    
    ```  
    robot.drive(300, 0) # drive at 300mm/sec, in straight line (because turn_rate=0)
    wait(1000) # wait one second
    robot.stop() # not required if program ends after wait command 
    ```  
      [try it out in Pybricks Gears](https://kendmaclean.github.io/gears_pybricks/public/)  (copy code and paste in under Python tab)
    
    * call drive() many times inside [while loop](https://pybricks.github.io/ev3-micropython/examples/robot_educator_ultrasonic.html) using [distance()](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.distance) or [angle()](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.angle):
     
      ```
        robot.reset()
        # keep driving until either robot has travelled 100cm or turned 45degrees
        while robot.distance() < 1000 and robot.angle() < 180:
            robot.drive(300,30) # drive for 300mm/s, while turning left at 30deg/sec 
            wait(10) # wait for a short time or do something else
        robot.stop()
      ```
      
  * [reset()](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.reset) - distance is calculated from start of program, so reset() it before using distance in a while loop

    
----- 

### Single Motor/Attachment motor control ([Motor class](https://pybricks.github.io/ev3-micropython/ev3devices.html#motors))
* control motors with built-in rotation sensors
* Action
  * [run(speed)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.run)
    * Runs the motor at a constant speed, no stopping.  If it is the only command, make sure you use a wait 
      command, otherwise the program will end before run command can execute:
      
     ```
        left_motor = Motor(Port.B)
        lift_motorA.run(500)
        wait(2000) # run the lift motor command for 2 seconds
     ```
     
  * [run_angle(speed, rotation_angle, then=Stop.HOLD, wait=True)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.run_angle)
    * moves the wheels X degrees relative to their current angle.
  * [run_target(speed, target_angle, then=Stop.HOLD, wait=True)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.run_target) 
    * moves the wheels X degrees until they reach an absolute angle you specify.       

* Stopping
  * [stop()](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.stop) - glide to a stop
  * [brake()](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.brake) - motor friction stop
  * [hold()](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.hold) - stop motor rotation and actively hold

----- 

## Sensors

* Basic:
  * [classTouchSensor(port)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.TouchSensor)
  * [class UltrasonicSensor(port)](https://pybricks.github.io/ev3-micropython/nxtdevices.html#nxt-ultrasonic-sensor) (from [nxtdevices module](https://pybricks.github.io/ev3-micropython/nxtdevices.html))
  * [classInfraredSensor(port)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.InfraredSensor)

* More accurate
  * [classColorSensor(port)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.ColorSensor)
    * [3-level line follower using color sensor](https://github.com/fll-pigeons/gamechangers/blob/master/programs/LP04a_lineFollowerBasic):
    
    ```
        line_sensor = ColorSensor(Port.S1)    

        while True:
           if line_sensor.reflection()  > 80: # white
               robot.drive(speed=75, turn_rate=-40)
           else: 
               if line_sensor.reflection()  < 15: # black
                   robot.drive(speed=75, turn_rate=40)
               else: #straight
                   robot.drive(speed=75, turn_rate=0)
    ```
    
     * [Proportional line follower](https://pybricks.github.io/ev3-micropython/examples/robot_educator_line.html)
     
  * [classGyroSensor(port, positive_direction=Direction.CLOCKWISE)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.GyroSensor)
    * How to drive straight using gyro.angle:
  
    ```
        gyro_sensor = GyroSensor(Port.S3)
        
        robot.reset() # reset robot.distance counter
        gyro_sensor.reset_angle(0) # reset angle to zero
        while robot.distance() < 1000: # robot to travell 1000mm
          angle_correction = -1 * gyro_sensor.angle() # calculate angle to turn robot in opposite direction of robot deviation from zero angle
          robot.drive(drive_speed=200, turn_rate=angle_correction) # plug in angle_correction to turn rate so robot drive opposite direction of angle error
        robot.stop() # tell robot to stop, otherwise it will continue to drive until program stops
    ```  
    
    * [How to turn using gyro.angle](https://github.com/fll-pigeons/gamechangers/blob/master/programs/LP03b_squareGyroDriveLoop.py):
  
    ```
        gyro_sensor = GyroSensor(Port.S3)

        gyro_sensor.reset_angle(0)
        while gyro_sensor.angle() < 45:
          robot.drive(drive_speed=200, turn_rate=90)
        robot.stop()          
    ```
  
    * [reset_angle(0)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.reset_angle) - reset gyro angle before using it as a test in a loop
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

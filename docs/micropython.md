#  LEGO® EV3 MicroPython (Pybricks) Cheat sheet
 
## Drive the Robot (Control two motors at same time)
* **Move then stop** (drive straight or spin turn)
  * [settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.settings) (modifies next straight or turn command)
  * [straight(distance)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.straight), then stop 
  * [turn(angle)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.turn) in place, then stop   
    
* **Move forever** (straight or turn until a stop() or another drive() command, or until program ends)
  * [drive(drive_speed, turn_rate)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.drive)
  * How to call drive:
    * drive() then [wait(milliseconds)](https://pybricks.github.io/ev3-micropython/tools.html?highlight=wait#pybricks.tools.wait), then [stop()](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.stop) 

      ```  
      robot.drive(300, 0) # drive at 300mm/sec, in straight line (because turn_rate=0)
      wait(1000) # wait one second
      robot.stop() # not required if program ends after wait command 
      ```  
      --->[try it out](https://fll-pigeons.github.io/gamechangers/simulator/public/)  (copy code and paste it under Python tab)
    
    * call drive() many times inside [while loop](https://pybricks.github.io/ev3-micropython/examples/robot_educator_ultrasonic.html) using [distance()](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.distance) or [angle()](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.angle):
     
      ```
      robot.reset()
      # keep driving until either robot has travelled 100cm or turned 45degrees
      while robot.distance() < 1000 and robot.angle() < 120:
          robot.drive(300,30) # drive for 300mm/s, while turning left at 30deg/sec 
          wait(10) # wait for a short time or do something else
      robot.stop()
      ```
      --->[try it out](https://fll-pigeons.github.io/gamechangers/simulator/public/)  (copy code and paste it under Python tab)
    
  * [reset()](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.reset) - distance is calculated from start of program, so reset() it before using distance in a while loop

    
----- 

## Single motor control (for Attachments)
* Action
  * [run(speed)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.run)
    * Runs the motor at a constant speed, no stopping.  If it is the only command, make sure you use a wait 
      command, otherwise the program will end before run command can execute:
      
      ```
      motorC.run(200)
      wait(500) # run the lift motor command for half a second
      motorC.stop()
      ```
      --->[try it out](https://fll-pigeons.github.io/gamechangers/simulator/public/)  (use Tow Truck robot)
    
  * [run_angle(speed, rotation_angle, then=Stop.HOLD, wait=True)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.run_angle)
    * rotates motor X degrees relative to its current angle.
  * [run_target(speed, target_angle, then=Stop.HOLD, wait=True)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.run_target) 
    * rotates motor X degrees until they reach the absolute angle you specify.       

* Stopping
  * [stop()](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.stop) - glide to a stop
  * [brake()](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.brake) - motor friction stop
  * [hold()](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.hold) - stop motor rotation and actively hold

----- 

## Sensors

* [classGyroSensor(port, positive_direction=Direction.CLOCKWISE)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.GyroSensor)
  * Drive Straight Using Gyro:
    ```
    gyro_sensor = GyroSensor(Port.S3)

    distance = 1000 # millimetres

    robot.reset() 
    gyro_sensor.reset_angle(0)
    PROPORTIONAL_GAIN = 1.1    
    while robot.distance() < distance:
      angle_correction = -1 * PROPORTIONAL_GAIN * gyro_sensor.angle()
      robot.drive(drive_speed=200, turn_rate=angle_correction) 
      wait(10)
    robot.stop()
    ``` 
    --->[try it out](https://fll-pigeons.github.io/gamechangers/simulator/public/)  (use Single Sensor Line Robot and select Gyro Challenges from Worlds under the Simulator tab)
    * Note: if running your motors counter counterclockwise, remember to set your gyro with it too: gyro_sensor = GyroSensor(Port.S3, Direction.COUNTERCLOCKWISE)
 
  * Spin Turn Using Gyro

    ```
    gyro_sensor = GyroSensor(Port.S3)

    angle = 45 # degrees
    speed = 150 # mm/s
    
    if angle < 0: # reverse direction of motors if turning counter clockwise
        speed = -speed
        
    gyro_sensor.reset_angle(0)
    while abs(gyro_sensor.angle()) < abs(angle):
      motorA.run(speed=speed)
      motorB.run(speed=(-1 * speed))
      wait(10)
    motorA.brake()
    motorB.brake()      
    ```
    --->[try it out](https://fll-pigeons.github.io/gamechangers/simulator/public/)  (copy code and paste in under Python tab)
    * Note: abs turns a negative number into a positive, and doesn't change a positive number
    
  * Gradual Turn Using Gyro:

    ```
    gyro_sensor = GyroSensor(Port.S3)

    angle = 90 # degrees
    rotational_speed = 90 # degrees per second
    speed = 150 # mm/s

    gyro_sensor.reset_angle(0)
    while gyro_sensor.angle() < angle:
      robot.drive(drive_speed=speed, turn_rate=rotational_speed)
    robot.stop()       
    ```
    --->[try it out](https://fll-pigeons.github.io/gamechangers/simulator/public/)  (copy code and paste in under Python tab)

  * Notes:
    * [reset_angle(0)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.reset_angle) - remember to reset gyro angle before using it as a test in a loop
    * Gyro must be plugged to EV3 before power up.  Make sure brick does not move on power up.  Never plug in gyro to an already powered up EV3 brick - it messes up the calibration.
    
* [classColorSensor(port)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.ColorSensor)
  * 3-level line follower using color sensor:
    
  ```
  color_sensor_in1 = ColorSensor(Port.S1)    

  while True:
      if color_sensor_in1.reflection()  > 95: # white
          robot.drive(drive_speed=75, turn_rate=-60)
      else: 
          if color_sensor_in1.reflection()  < 10: # black
              robot.drive(drive_speed=75, turn_rate=60)
          else: #straight
              robot.drive(drive_speed=75, turn_rate=0)
  ```
  --->[try it out](https://fll-pigeons.github.io/gamechangers/simulator/public/) (use Single Sensor Line Robot and select Line Following Challenges from Worlds, under the Simulator tab)

  * [Proportional line follower](https://pybricks.github.io/ev3-micropython/examples/robot_educator_line.html)

    ```
    color_sensor_in1 = ColorSensor(Port.S1)

    BLACK = 10
    WHITE = 95
    threshold = (BLACK + WHITE) / 2
    PROPORTIONAL_GAIN = 1.5
    while True:
        deviation = color_sensor_in1.reflection() - threshold
        angle_correction = PROPORTIONAL_GAIN * deviation
        robot.drive(drive_speed=100, turn_rate=angle_correction)
        wait(10)     
    ```
    --->[try it out](https://fll-pigeons.github.io/gamechangers/simulator/public/) (use Single Sensor Line Robot and select Line Following Challenges from Worlds, under the Simulator tab) 

## Sample programs

* [ROBOT EDUCATOR PROGRAMS](https://pybricks.github.io/ev3-micropython/index.html)
  * [Basic Movement](https://pybricks.github.io/ev3-micropython/examples/robot_educator_basic.html)
  * [Obstacle Avoidance](https://pybricks.github.io/ev3-micropython/examples/robot_educator_ultrasonic.html)
  * [Line Following](https://pybricks.github.io/ev3-micropython/examples/robot_educator_line.html)
 
## Documentation
* [LEGO® MINDSTORMS Education EV3 MicroPython](https://pybricks.github.io/ev3-micropython/index.html)
* see also: [pybricks cheatsheet By FLL TechTacos](https://cheatography.com/flltech2019/cheat-sheets/pybricks-cheatsheet-by-fll-techtacos-sugarland/pdf/)


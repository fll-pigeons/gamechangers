#  LEGO® EV3 Python (Pybricks) Cheat sheet
 
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
      robot.drive(150, 0) # drive at 150mm/sec, in straight line (because turn_rate=0)
      wait(1000) # wait one second
      robot.stop() # not required if program ends after wait command 
      ```  
      --->[try it out](https://fll-pigeons.github.io/gamechangers/simulator/public/)  (copy code and paste it under Python tab)
      * Note: at faster speeds, the robot will not accurately drive in a straight line - you will need to use a sensor to fix this (e.g. gyro)
    
    * call drive() many times inside [while loop](https://pybricks.github.io/ev3-micropython/examples/robot_educator_ultrasonic.html) using [distance()](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.distance) or [angle()](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.angle):
     
      ```
      robot.reset()
      # keep driving until either robot has travelled 100cm or turned 120degrees
      while robot.distance() < 1000 and robot.angle() < 120:
          robot.drive(150,30) # drive for 150mm/s, while turning left at 30deg/sec 
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
  * **Drive Straight Using Gyro - Forward:** (Proportional algorithm)
  
    ```
    gyro_sensor = GyroSensor(Port.S3) # Assumes gyro is connected to port 3

    distance = 1000 # millimetres
    robotSpeed = 150 # mm/sec
    
    robot.reset() 
    gyro_sensor.reset_angle(0)
    
    PROPORTIONAL_GAIN = 1.1    
    while robot.distance() < distance:
      angle_correction = -1 * PROPORTIONAL_GAIN * gyro_sensor.angle()
      robot.drive(robotSpeed, angle_correction) 
      wait(10)
    robot.stop()
    ``` 
    --->[try it out](https://fll-pigeons.github.io/gamechangers/simulator/public/)  (use Single Sensor Line Robot and select Gyro Challenges from Worlds under the Simulator tab)
    * Notes: 
      * Remember to call robot.reset() before using robot.distance() as a test in a loop    
      * If your gyro is attached backwards on your robot, use Direction.COUNTERCLOCKWISE when setting up GyroSensor
      * Distance must be far enough so that Gyro code can make correction (e.g. 20mm distance is too short)

   * **Drive Straight Using Gyro - Forward or Backwards:** (Proportional algorithm)

     ```
     gyro_sensor = GyroSensor(Port.S3) # Assumes gyro is connected to port 3    

     distance = -1000 # millimetres
     robotSpeed = 150 # mm/sec    

     robot.reset() 
     gyro_sensor.reset_angle(0)

     PROPORTIONAL_GAIN = 1.1
     if distance < 0: # move backwards
         while robot.distance() > distance:
             reverseSpeed = -1 * robotSpeed        
             angle_correction = -1 * PROPORTIONAL_GAIN * gyro_sensor.angle()
             robot.drive(reverseSpeed, angle_correction) 
             wait(10)
     elif distance > 0: # move forwards             
         while robot.distance() < distance:
             angle_correction = -1 * PROPORTIONAL_GAIN * gyro_sensor.angle()
             robot.drive(robotSpeed, angle_correction) 
             wait(10)            
     robot.stop()
     ``` 
    --->[try it out](https://fll-pigeons.github.io/gamechangers/simulator/public/)  (use Single Sensor Line Robot and select Gyro Challenges from Worlds under the Simulator tab)

   * See also: [Driving straight using a gyro and PID algorithm](gyro_pid.md)
    
    
   * **Spin Turn Using Gyro - Right Turn Only**

     ```
     gyro_sensor = GyroSensor(Port.S3)    

     angle = 90 # degrees
     speed = 150 # mm/s

     gyro_sensor.reset_angle(0)
     while gyro_sensor.angle() < angle:
         motorA.run(speed=speed)
         motorB.run(speed=(-1 * speed))
         wait(10)  

     motorA.brake()
     motorB.brake()    
     ```
    --->[try it out](https://fll-pigeons.github.io/gamechangers/simulator/public/)  (copy code and paste in under Python tab)
    
  * **Spin Turn Using Gyro - Either Direction**

    ```
    gyro_sensor = GyroSensor(Port.S3)    
    
    angle = -90 # degrees
    speed = 150 # mm/s

    gyro_sensor.reset_angle(0)
    if angle < 0:
        while gyro_sensor.angle() > angle:
            motorA.run(speed=(-1 * speed))
            motorB.run(speed=speed)
            wait(10)
    elif angle > 0:  
        while gyro_sensor.angle() < angle:
            motorA.run(speed=speed)
            motorB.run(speed=(-1 * speed))
            wait(10)  
    else:
        print("Error: no angle chosen")

    motorA.brake()
    motorB.brake()    
    ``` 
    --->[try it out](https://fll-pigeons.github.io/gamechangers/simulator/public/)  (copy code and paste in under Python tab)
    
  * Notes:
    * [reset_angle(0)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.Motor.reset_angle) - remember to reset gyro angle before using it as a test in a loop
    * Gyro must be plugged to EV3 before power up.  Make sure brick does not move on power up.  Never plug in gyro to an already powered up EV3 brick - it messes up the calibration.
    
* [classColorSensor(port)](https://pybricks.github.io/ev3-micropython/ev3devices.html#pybricks.ev3devices.ColorSensor)
  * **3-level line follower using color sensor:**
    * (not very accurate)
    
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

  * **[Proportional line follower](https://pybricks.github.io/ev3-micropython/examples/robot_educator_line.html)**

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


#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------
This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3
Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
left_motor.reset_angle(0)
right_motor.reset_angle(0)

# Initialize gyro.
gyro = GyroSensor(Port.S3)
gyro.reset_angle(0)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=54.6, axle_track=104.1)

#################################################################################
# straight (if run motor faster, must adjust distance)
# turn (if run motor faster, must adjust angle)

ev3.screen.draw_text(50, 60, "Pigeons!")

## 1.
### straight
robot.reset()   
while robot.distance() < 250:
    robot.drive(200 ,0)

### turn
gyro.reset_angle(0)
while abs(gyro.angle()) < 66:
    robot.drive(200 ,150)

## 2. 
### straight
robot.reset()   
while robot.distance() < 250:
    robot.drive(200 ,0)

### turn
gyro.reset_angle(0)
while abs(gyro.angle()) < 66:
    robot.drive(200 ,150)
   
## 3.   
### straight
robot.reset()   
while robot.distance() < 250:
    robot.drive(200 ,0)

### turn
gyro.reset_angle(0)
while abs(gyro.angle()) < 66:
    robot.drive(200 ,150)

## 4. 
### straight
robot.reset()   
while robot.distance() < 250:
    robot.drive(200 ,0)

### turn
gyro.reset_angle(0)
while abs(gyro.angle()) < 66:
    robot.drive(200 ,150)    

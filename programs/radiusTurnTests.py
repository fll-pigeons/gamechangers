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
import math

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=54.6, axle_track=104.1)

# Functions
# drive straight, no stopping
def driveStraight(distance, drive_speed = 200):
    robot.reset()    
    print ("driveStraight: distance: " + str(distance) + " drive_speed " + str(drive_speed))  
    while robot.distance() < distance:
        robot.drive(drive_speed, 0)

# radius in mm
# drive with turn, no stopping
def driveRadiusTurn(radius, drive_speed = 200):
    robot.reset()       
    print ("driveRadiusTurn: radius: " + str(radius) + " drive_speed " + str(drive_speed))  
    turn_rate = radius / ((drive_speed * 2 * math.pi ) * 360)
    print ("driveRadiusTurn: turn_rate: " + str(turn_rate))  

    #while abs(robot.angle()) < 180:
    #    print ("angle: " + str(abs(robot.angle())))        
    #    robot.drive(drive_speed, turn_rate)
    robot.drive(drive_speed, turn_rate)
    wait(2000) # for debugging, will use a loop in prod...

#################################################################################

ev3.screen.draw_text(50, 60, "Pigeons!")

driveStraight(50)
driveRadiusTurn(1000)

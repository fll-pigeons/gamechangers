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
    print ("driveStraight: distance: " + str(distance/10) + "cm;  drive_speed " + str(drive_speed/10) + "cm/s")  
    while robot.distance() < distance:
        robot.drive(drive_speed, 0)

# radius in mm
# drive with turn, no stopping
# see: https://www.w3resource.com/python-exercises/math/python-math-exercise-7.php
def driveRadiusDriveTurn(radius, drive_speed = 200):
    robot.reset()       
    arc_angle = (180 * drive_speed) / (radius * math.pi)

    arc_angle_str = str(round(arc_angle, 2)) + " deg/s"      
    print ("driveRadiusTurn: arc_angle: " + arc_angle_str)  

    turn_rate = arc_angle
    while abs(robot.angle()) < 180:
        #print ("angle: " + str(abs(robot.angle())))        
        robot.drive(drive_speed, turn_rate)
 
def driveRadiusStraightTurn(radius, drive_speed = 200):
    robot.reset()       
    arc_angle = (180 * drive_speed) / (radius * math.pi)
    diameter = radius * 2
    arc_length = (math.pi * diameter) * (arc_angle / 360)

    arc_angle_str = str(round(arc_angle, 2)) + " deg/s"    
    print ("               arc_length: " + arc_angle_str + "; arc_length" + str(arc_length/10) + "cm")      

    robot.stop()
    turn_rate = arc_angle
    robot.settings(drive_speed, drive_speed, turn_rate, drive_speed)
    robot.straight(arc_length)

#################################################################################

ev3.screen.draw_text(50, 60, "Pigeons!")

driveStraight(150)

ev3.speaker.beep()
radius = 200
print("radius " + str(radius))
# driveRadiusDriveTurn(radius) # works
driveRadiusStraightTurn(radius)
ev3.speaker.beep()

driveStraight(300)

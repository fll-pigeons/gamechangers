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
robot = DriveBase(left_motor, right_motor, wheel_diameter=68.8, axle_track=110)

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
def driveRadiusTurnWithMotorAngle(radius, drive_speed = 200):
    robot.reset()       
    arc_angle = (180 * drive_speed) / (radius * math.pi)
    arc_angle_str = str(round(arc_angle, 2)) + " deg/s"      
    print ("driveRadiusTurn: arc_angle: " + arc_angle_str)  

    turn_rate = arc_angle
    # less than 180deg because of measurement lag
    while abs(robot.angle()) < 150: 
        #print ("angle: " + str(abs(robot.angle())))        
        robot.drive(drive_speed, turn_rate)

def driveRadiusDriveTurn2(radius, drive_speed = 200, turn_angle=180):
    arc_angle = (180 * drive_speed) / (radius * math.pi)
    arc_angle_str = str(round(arc_angle, 2)) + " deg/s"      
    print ("driveRadiusTurn: arc_angle: " + arc_angle_str)  

    arc_length = 2 * math.pi * radius * (turn_angle / 360)
    print ("                 arc_length: " + str(arc_length/10) + "cm")  

    turn_rate = arc_angle
    robot.reset()      
    while robot.distance() < arc_length:
   
        robot.drive(drive_speed, turn_rate)



#################################################################################

ev3.screen.draw_text(50, 60, "Pigeons!")
distance = 300
speed = 300
driveStraight(10, speed)

ev3.speaker.beep()

radius = 100
print("radius " + str(radius))
#driveRadiusTurnWithMotorAngle(radius, speed) # works
driveRadiusDriveTurn2(radius, speed, 90)
ev3.speaker.beep()

driveStraight(distance, speed)

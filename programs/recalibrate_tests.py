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
from pybricks.ev3devices import Motor
from pybricks.ev3devices import GyroSensor
from pybricks.parameters import Direction
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)


# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=54.6, axle_track=104.1)
gyro = GyroSensor(Port.S1)



#################################################################################
# this should be a separate program to run at beginning of competition
# https://ev3lessons.com/en/ProgrammingLessons/advanced/Gyro.pdf
# Gyro returns NaN until calibrated
def recalibrateGyro():
    ev3.speaker.beep()
    # recalibrate gyro
    gyro.speed()
    wait(3)

    # need to wait until angle set to zero, then recalibrated
    # have not tested this...
    while abs(gyro.angle()) != 0
        gyro.reset_angle(0)

    ev3.speaker.beep()
    ev3.speaker.beep()
    
#################################################################################

ev3.screen.draw_text(50, 60, "Pigeons!")
recalibrateGyro()

while robot.distance() < 500:
    robot.drive(1000, 0)

robot.reset()
gyro.reset_angle(0)
angle = gyro.angle()
print (  "gyro1 " + str(angle) )
while abs(angle) < 160:
    print (  "gyro2 " + str(angle) )
    print (  "drive " + str(robot.angle() ) )    
    robot.drive(10, -180)
    angle = gyro.angle()

robot.reset()
while robot.distance() < 500:
    robot.drive(1000, 0)

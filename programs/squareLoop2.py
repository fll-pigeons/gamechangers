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



#################################################################################

ev3.screen.draw_text(50, 60, "Pigeons!")



x=0
while x < 8:
    # straight (if run motor faster, must adjust distance)
    robot.reset()
    while robot.distance() < 250:
        robot.drive(200 ,0)

    # turn (if run motor faster, must adjust angle)
    robot.reset()
    while robot.angle() < 75:
        print ("angle: " + str(robot.angle()))
        robot.drive(200 ,150)
    x = x + 1
robot.stop()

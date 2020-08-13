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

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
lift_motor = Motor(Port.A)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=94.2, axle_track=110)

robot.settings (300, 620, 620, 300)
ev3.screen.draw_text(50, 60, "Pigeons!")
ev3.speaker.beep()


robot.straight(669)
robot.straight(-270)
robot.turn (30)
robot.straight(200)
robot.turn (-30)
robot.straight(400)
robot.turn(-90)
robot.straight(400)
robot.turn(-30)
robot.straight(300)

robot.straight(50)
robot.straight(-50)
robot.straight(50)
robot.straight(-50)
robot.straight(50)
robot.straight(-50)
robot.straight(50)
robot.straight(-50)
robot.straight(50)
robot.straight(-50)
robot.straight(50)
robot.straight(-50)
robot.straight(50)
robot.straight(-50)



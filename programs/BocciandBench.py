#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B,  positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C,  positive_direction=Direction.COUNTERCLOCKWISE)
lift_motor = Motor(Port.A)

robot = DriveBase(left_motor, right_motor, wheel_diameter=94.2, axle_track=94)
robot.settings(straight_speed=150 , straight_acceleration=50, turn_rate=150, turn_acceleration=200)

ev3.screen.draw_text(50, 60, "Pigeons!")
ev3.speaker.beep()

robot.straight(600)
robot.turn(-30)
robot.turn(30)
robot.straight(200)
robot.turn(-35)

ev3.speaker.beep()


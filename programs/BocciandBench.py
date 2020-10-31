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
forklift_motor = Motor(Port.D)

robot = DriveBase(left_motor, right_motor, wheel_diameter=94.2, axle_track=94)
robot.settings(straight_speed=200 , straight_acceleration=50, turn_rate=150, turn_acceleration=200)
ev3.screen.draw_text(50, 60, "robot go brrrr")
ev3.speaker.beep()

robot.straight(422)
robot.turn(-88)
robot.straight(490)
forklift_motor.run_angle(speed=100, rotation_angle=150)
robot.straight(-149)
forklift_motor.run_angle(speed=280, rotation_angle=-150)
robot.turn(-58)
robot.straight(149)
forklift_motor.run_angle(speed=100, rotation_angle=650)
forklift_motor.run_angle(speed=100, rotation_angle=-650)
#robot.turn(-70)
#robot.straight(20)
#robot.turn(-40)
#robot.straight(100)
ev3.speaker.beep()


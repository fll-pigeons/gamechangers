#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
forklift_motor = Motor(Port.D,  positive_direction=Direction.COUNTERCLOCKWISE) 

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=94.2, axle_track=94)

ev3.screen.draw_text(50, 60,"Testing!")

ev3.speaker.beep()
#forklift_motor.run_angle(speed=5005, rotation_angle=2*360)
forklift_motor.run_angle(speed=5005, rotation_angle=-2*360)
#owen is a loser


#forklift_motor.run_angle(speed=25198, rotation_angle=10000)
#forklift_motor.run_angle(speed=25198, rotation_angle=-8500)

ev3.speaker.beep()

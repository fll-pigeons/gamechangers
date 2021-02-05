#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B,  positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C,  positive_direction=Direction.COUNTERCLOCKWISE)
lift_motor = Motor(Port.A)
forklift_motor = Motor(Port.D,  positive_direction=Direction.COUNTERCLOCKWISE)

robot = DriveBase(left_motor, right_motor, wheel_diameter=94.2, axle_track=94)
robot.settings(straight_speed=200 , straight_acceleration=50, turn_rate=150, turn_acceleration=200)
ev3.screen.draw_text(50, 60, "noot noot")
ev3.speaker.beep()

gyro_sensor = GyroSensor(Port.S2, Direction.COUNTERCLOCKWISE)

def gyro_turn(angle, speed=150):
    gyro_sensor.reset_angle(0)
    if angle < 0:
        while gyro_sensor.angle() > angle:
            left_motor.run(speed=(-1 * speed))
            right_motor.run(speed=speed)
            wait(10)
    elif angle > 0:  
        while gyro_sensor.angle() < angle:
            left_motor.run(speed=speed)
            right_motor.run(speed=(-1 * speed))
            wait(10)  
    else:
        print("Error: no angle chosen")

    left_motor.brake()
    right_motor.brake() 

def gyro_straight(distance, robotSpeed=150):
    robot.reset() 
    gyro_sensor.reset_angle(0)

    PROPORTIONAL_GAIN = 1.1
    if distance < 0: # move backwards
        while robot.distance() > distance:
            reverseSpeed = -1 * robotSpeed        
            angle_correction = -1 * PROPORTIONAL_GAIN * gyro_sensor.angle()
            robot.drive(reverseSpeed, angle_correction) 
            wait(10)
    elif distance > 0: # move forwards             
        while robot.distance() < distance:
            angle_correction = -1 * PROPORTIONAL_GAIN * gyro_sensor.angle()
            robot.drive(robotSpeed, angle_correction) 
            wait(10)            
    robot.stop()


# Go to boccia
gyro_straight(460, 100)
gyro_turn(-87, 100)
gyro_straight(575, 100)
forklift_motor.run_angle(speed=1000, rotation_angle=160)
gyro_straight(-10, 100)
# Move to basket
forklift_motor.run_angle(speed=1000, rotation_angle=-160)
gyro_straight(-30, 100)
gyro_turn(-40, 100)
gyro_straight(65, 100)
forklift_motor.run_angle(speed=1000, rotation_angle=1.5*360)
forklift_motor.run_angle(speed=1000, rotation_angle=-1.5*300)
# Move to bench
gyro_straight(-70, 100)
gyro_turn(-70, 100)
gyro_straight(220, 200)
# Go back to home base
gyro_straight(-43, 100)
gyro_turn(-45, 100)
gyro_straight(705, 150)


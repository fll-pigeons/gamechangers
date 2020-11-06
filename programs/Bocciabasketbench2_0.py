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
forklift_motor = Motor(Port.D) 

robot = DriveBase(left_motor, right_motor, wheel_diameter=94.2, axle_track=94)
robot.settings(straight_speed=200 , straight_acceleration=50, turn_rate=150, turn_acceleration=200)
ev3.screen.draw_text(50, 60, "robot go brrrr")
ev3.speaker.beep()

gyro_sensor = GyroSensor(Port.S2, Direction.COUNTERCLOCKWISE)

def gyro_straight(distance, robotSpeed):
    robot.reset() 
    print("=====================================")
    print("gyro_straight: distance: " + str(distance) + " robotSpeed: " + str(robotSpeed))    
    gyro_sensor.reset_angle(0)
    print("gyro reset" + str(gyro_sensor.angle()))        
    PROPORTIONAL_GAIN = 1.3    
    while robot.distance() < distance:
        angle_correction = -1 * PROPORTIONAL_GAIN * gyro_sensor.angle()
        robot.drive(speed=robotSpeed, turn_rate=angle_correction) 
        print("gyro: " + str(gyro_sensor.angle()) + " angle_correction: " + str(angle_correction) )        
        wait(10)
    robot.stop()

def gyro_turn(angle, speed):
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


gyro_straight(50, 100)
gyro_turn(15, 100)
gyro_straight(620, 100)
gyro_turn(-7, 100)
wait(100)
gyro_straight(280, 100)
forklift_motor.run_angle(speed=100, rotation_angle=150)
forklift_motor.run_angle(speed=280, rotation_angle=-150)
gyro_straight(-80, 100)
#forklift_motor.run_angle(speed=100, rotation_angle=650)
#forklift_motor.run_angle(speed=100, rotation_angle=-650)

ev3.speaker.beep()

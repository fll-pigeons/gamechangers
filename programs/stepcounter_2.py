#!/usr/bin/env python3

# Import the necessary libraries
import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick

ev3 = EV3Brick()
motorA = Motor(Port.A)
motorB = Motor(Port.B)
left_motor = motorA
right_motor = motorB
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=152)
robot.settings(straight_speed=200, straight_acceleration=100, turn_rate=100)

color_sensor_in1 = ColorSensor(Port.S1)
obstacle_sensor = UltrasonicSensor(Port.S2)
gyro_sensor= GyroSensor(Port.S3)

motorC = Motor(Port.C) # Magnet

# Here is where your code starts
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

def gyro_straight(distance, robotSpeed):
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
    
gyro_straight(15, 50)
gyro_turn(100, 100)
gyro_straight(300, 100)
gyro_turn(-10, 100)
gyro_straight(450, 100)
gyro_straight(150, 50)
gyro_straight(-950, 300)

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
         
    count =0
    while robot.distance() < distance:
        angle = gyro_sensor.angle()
        correction = -1.3 * angle
        print(str(count) + " angle: "+ str(angle) + " correction: "+ str(correction))
        print(robot.heading_control.limits() )
        print(str(robot.heading_control.pid()))
        robot.drive(robotSpeed, correction) 
        count += count        
        wait(10)            
    robot.stop()

#gyro_offset = calibrate()
#print("gyro_offset" + str(gyro_offset))
#gyro_straight(890, 100)
#robot.straight(890)

#see: https://marklucking.medium.com/micropython-tutorial-xii-15b1cf4d7a51

speed = 100
angle = 0
targetAG = 0
Kp = 1.1 #  Kp on 1.0 
Ki = 0.005 #  Ki on 0.0005 
Kd = 0.2 #  Kd of 0.01 
error = 0
lastError = 0
intergral = 0
deriative = 0
while True:
    angle = gyro_sensor.angle()
    error = (targetAG - angle)
    direct = error * Kp
    intergral = (intergral + error) * Ki
    deriative = (error - lastError) * Kd
    turn = direct + intergral + deriative    
    print("A",gyro_sensor.angle(),"direct",direct,"Integral",intergral,"D",deriative, "sum",turn)    
    lastError = error    
    robot.drive(150,turn)
    wait(10)      

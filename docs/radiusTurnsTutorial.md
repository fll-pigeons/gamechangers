## Problem Statement: 

Wanted a function that lets you tell the robot to turn using just the radius of a circle.

The function would then calculates the turning rate (or angle of turn) and the arc length to get the robot around 
a wall or object.  All you do is get the robot to the point of turning, give the distance to 
the object you want to avoid, and it travels in a half circle using the distance given as the radius of an circle.

This is conceptually simpler for kids to understand once they understand radius, arc_angle and arc_length in a circles 
and has less trial and error when trying to measure the angle and distance for a turn.

Hoping that this function can automatically adjust turn rate if speed changes - faster turns usually mean more lag in the
turn, so a smaller angle is required.

## Solution:
(big thank you to Liam MacLean, FRC alumnus, [team 5483 GD-Bots](https://github.com/Team-5483) for this information)

The solution requires simple arc math with the [drive(drive_speed, turn_rate)](https://pybricks.github.io/ev3-micropython/robotics.html#pybricks.robotics.DriveBase.drive) function,

given velocity v and turn rate Δθ (delta theta)

arc_length = v * time
arc_angle = Δθ * time

circumference = arc_length * (360/arc_angle)  #For example, if arc_angle is 360, then the circumference of the circle is just arc_length

radius = circumference/ 2*pi

therefore

radius = ((v * time) * (360/( Δθ * time)) ) / 2*pi

cancel out time

radius = 360v / ( Δθ * 2 * pi)

which can be rearranged as

v = (r *  Δθ * 2 * pi) / 360

or

Δθ = 360v / r * 2 pi


so you can make a function that takes as input 2 of either speed, radius, degrees/second and spits out the other one
I assume you would want to input speed and radius and receive turning rate, so use the last equation

# function that we created:

```
def radiusTurnMotorDistance(radius, drive_speed = 200, turn_angle=180):
    arc_angle = (180 * drive_speed) / (radius * math.pi)
    arc_angle_str = str(round(arc_angle, 2)) + " deg/s"    
    arc_length = 2 * math.pi * radius * (turn_angle / 360)

    print ("driveRadiusTurn: arc_angle: " + arc_angle_str)  
    print ("                 arc_length: " + str(arc_length/10) + "cm")  

    turn_rate = arc_angle
    robot.reset()      
    while robot.distance() < arc_length:
        robot.drive(drive_speed, turn_rate)
```

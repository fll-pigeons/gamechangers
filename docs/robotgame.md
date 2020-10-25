# Robot Game

# 0. Programs saved on Github
[Our MicroPython programs](https://github.com/tobedetermined123/gamechangers/tree/master/programs)

# 1. Missions
* Robot game rules
  * [RePLAY Rule Book](https://firstinspiresst01.blob.core.windows.net/first-game-changers/fll-challenge/FLL-Challenge-RGR-Final-ONA.pdf)
  * [RePLAY Challenge Updates](https://firstinspiresst01.blob.core.windows.net/first-game-changers/fll-challenge/replay-challenge-updates.pdf)

* FLLTutorial resources
  * [RePLAY Strategy Planner](https://flltutorials.com/Resources/2020/drawplan/index.html)
  * [FLLTutorials - Worksheets](https://docs.google.com/presentation/d/1PnNn2YYXbGBRo8o1VmTJxActQOz501SqhTqJsjvCo5c/edit#slide=id.p10)

* Points Calculators
  * [komurobo](http://komurobo.com/projets/fll/replay/)
  * [FLL RePLAY Scorer](https://flltutorials.com/Resources/2020/scorer/index.html?lang=en)
  
* Last Year
  * [Strategy Sheet - 2019](CityShaperStrategySheet.pdf)

### Mission Examples

* Wordynerd48
  * [215 points](https://www.youtube.com/watch?v=2juRHtQFIrA)
  * [510 points](https://www.youtube.com/watch?v=BmS7GUrksZs)

<br/>

# 2. Robot
### Robot Design
* [First Lego League Tutorials](http://flltutorials.com/RobotGame.html)
* [EV3 Lessons](http://ev3lessons.com/en/RobotDesigns.html)
* [highlandersfrc - robot design](http://www.highlandersfrc.com/NewsEventPages/FLL%20Programming%20and%20Design.pdf)
  * [Calibrating motors](https://techbrick.com/techbrick/Lego/TechBrick/TechTips/NXTCalibration/)
* [MOC - Super Small Box Robot by FLL Team Moscow](https://rebrickable.com/mocs/MOC-10638/DLuders/super-small-box-robot-by-fll-team-moscow/#comments)

<br/>

# 3. Programing
### [Lego EV3 MicroPython Cheat Sheet](micropython.md)
### [Lego EV3 Micropython (Pybricks) simulator](/simulator/public/) 

### Docs

* [Lego's Documentation - html](https://pybricks.github.io/ev3-micropython/index.html)
* [PyBrick's MicroPython Documentation - pdf](https://docs.pybricks.com/_/downloads/en/latest/pdf/)
* [Lego EV3 Programming Language research](AltProgLangs.md)

<br/>

# 4. [Learning Plan](learningPlan.md)

<br/>

# 5. [Hardware](hardware.md)
* [ev3dev.org device drivers](http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/ev3.html)

<br/>

# 6. Build/Programming Resources
* [Builderdude35](https://www.youtube.com/channel/UCuXq-jiU0ANeBcF_Tvq1D7g)
* [LEGORobotics Mr. Hino - YouTube](https://www.youtube.com/channel/UCvuw_UluXNRPKhqK5GU8SrQ)
* [FLL resources](https://techbrick.com/fll-resources/fll2019)
* [Other Links](links.md)

--------
# Log
> #### 22 & 24, 25 Oct - Finally figured out basketball hoop lift issue
The basketball hoop was getting caught at junction between blue vertical beam and black vertical beam.  There were many, many varied attempts/modifications to correct the robot fork lift attachment, when it was the mission design/construction that was the problem.  Good lesson learned: make sure all mission pieces fit snuggly after every attempt at trying the mission.
> #### 16 & 18 Oct - fixed problems which caused robot to drive erratically
incorporated Challenge set wheels to even out robot height (old wheels were too tall causing the robot to lean forward); fixed cabling issues: cables were rubbing on wheels causing random direction changes, this coupled with some loose fittings made for a very erratic robot - seemed like we went backward in terms of robot development.  But once these issues were resolved, robot ran cleanly and kids started working on missions once again.
> #### 10 Oct - testing new robot with old programs; No meeting on Oct 11 - Thanksgiving
Not enough to just change axle sizes, need to reprogram.  Drivebase class makes it seem like you only need to change axle sizes it you build new robot without changing you programs, not the case for us.  Change of direction of motors and changing settings speed parameters to negative numbers should  be the only required change... maybe we are missing something.
Confirmed with First re:strategy of attaching the health units to our innovation project - no equipment rule only applies to pull-up bar, so our strategy OK as long as health unit 'touching'  RePLAY logo - i.e. on bottom of our innovation project 
> #### 3 & 4 Oct - working on forklift attachment
> #### 26 & 27 Sept - working on box robot
> #### 19 & 20 Sept - moved to shorter Sat/Sun meetings; started working on box robot
> #### 12 Sept - School started - moved to Saturday meetings; more trial and error with robot
> #### 1 & 3 Sept - working on 3rd iteration of robot so that the wheels are more rigid and swapping attachments is easier.
> #### 27 Aug - First test run of 3 Mission groups
M00 Inspection Bonus (20);
M02_step_counter.py (15);
M04_M08_bench_boccia.py: M08 Bocci (15); Bench (10);
M01_M14_M06_M07.py: M01 Innovation (20), M14 Healt Units (3 x 5=15), M06 under pull up bar (15), M07 Robot Dance (20);
M15 Precision (60).
For a total *190* points in 2 min.
> #### 25 Aug - working on combined M08 Boccia & M04 Bench
Confirmed with First that for mission M01 Innovation Project, we can attach the 3 'home' health units to our 
innovation project and have the robot move this as one object to the RePLAY logo, so this will also count for 
3 M14 Health Unit points.  
Their response: "Great idea, and since the Units do not require that they not touch equipment and since the 
innovation project does not require it to be standalone, this combination would work and earn points for both 
missions at the same time."
> #### 20 Aug - experimented with using robot.drive() and wait() on mission M02_step_counter; 
team discovered that this approach not the best because if you change the speed of the robot, need to also change the running time - good learning experience.  Reverted to using odometryPerfo in robot.straight() for distance calculations.  Did run through of M02 mission and combined M01_M14_M06_M07 missions.
> #### 18 Aug - started mission M02_step_counter; wifi works like a dream.
> #### 13 Aug - working on combined M01_M14_M06_M07 missions; lots of problems with BlueTooth
> #### 11 Aug - working on combined M01_innovation_project, M14_health_units, M06_pull_up_bar, M07_tobot_dance
> #### 6 Aug - continued on mission M14_health_units and combined with M06_pull_up_bar
> #### 4 Aug - watched kickoff; read mission rules; started mission M14_health_units 

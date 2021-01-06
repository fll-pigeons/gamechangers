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
### Lego EV3 Python (Pybricks)
* #### [Cheat Sheet](micropython.md)
* #### [Virtual Robot Simulator](https://fll-pigeons.github.io/gamechangers/simulator/public/) 

* [Simulator Tutorial Videos](tutorial/simulatorIntro.md) (work in progress)
    
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
> #### 5 Jan, 2021 - troubleshooting reliability issues with 1_benchbocciabasket.py
Trying to figure out why robot seems to jiggle as it makes its way to the basketball mission, sometimes missing the mission altogether... Tried to ramp-up to target speed, also tried tweeks to the robot movement code.  It does not seem to be a problem with the gyro_straight parameters or the starting angle of the robot (though a jig make sure that this is not the problem...)  Best solution seems to be to adjust the PROPORTIONAL_GAIN field in the gyro_straight function from 1.1 to 1,2 - need to experiment more with this.
> #### Dec - break
> #### 28 Nov - FLL Challenge Practice Event - 3 submissions
Robot not working the same as on Thursday - off just enough to cause problems with missions.  Possible cause: Batteries from different manufacturers - we use rechargeable batteries from two different manufacturers: Duracell and Eveready.  Everything worked fine on Thursday with the Duracells, after making minor tweaks to the programming.  Saturday a.m. switched to the Evereadys (since they were fully charged), and since they have sightly higher baseline voltage, it seemed like we were consistently overshooting our missions.  Going forward we are going to stick with same batteries, and recharge after every session.  No going back and forth.  Would like to order an EV3 battery pack, but the charger is no longer in stock.  In addition, because we were able to record as many sessions as we wanted within a 6 hour window, we cycled through many mission attempts.   The problem is that the removal of our forklift and bucket attachments was not always clean and this caused problems with reassembly and hurt our ability to reliably perfom the basketball/bocci/bench and bocci bucket missions.
Feedback from judge: our M01 Innovation Project did not count because we have it on top of our health units (so they can be touching the logo) because it is not also touching logo.
> #### 26 Nov - Getting routine down for recording our 3 submissions
Ran through the process of recording our mission runs.  Worked on the intro and running the actual missions and review of results.  We managed to get 250 points on one run.  Question asked to FLL Support re putting robot on its side for M00 Inspection... they said: You can actually position your equipment any way you would like and even use your hands to hold stuff in place. As long as this fits in that volume (however you manage it), it would be allowed!
> #### 24 Nov - First complete run of all missions: 260 points
Potential to make 275 if everythig works as planned (Inspection Area, M01-Innovation Project & M14-Health Units, M02-Step Counter, M04-Bench, M06-Pullup bar, M07-Robot Dance, M08-Boccia, M14-Health Units, M15-Precision.)  Boccia scoring update - can score the 25 points for sending either a red or a blue cube from the share model, **but not both**.
> #### 22 Nov - Bocci/Basketball/Bench issues fixed
Simplified program so that it now uses fewer turns - less chance of misalignment.  Not perfect, but better than before
> #### 21 Nov - Basketball mission issues - infinite tweaking of forklift and code to work with Bocci, Basketball and bench missions
Still not working correctly - no clear where the problem is.  Trying new program from scratch with fewer turns, and making sure any gyro_straight commands are for long enough distances for gyro to make corrections (e.g. 20mm distance is too short and gyro cannot make correction fast enough).  Finally figured out that hand tightening all the pieces on the forklift before every run, along with tightening the box portion of the robot is required for repeatable runs.
> #### 19 Nov - Rewriting missions created with old robot design for use with new one - easier than adapting old code
> #### 12 & 14 Nov - more work on Forklift
> #### 5 & 7 Nov - Forklift and gyro code fix
Finished rebuild of forklist attachment; fixed gyro_straight() bug so that robot can now use gyro when going backwards in straight line. Robot more accurate on turns and travelling straight.
> #### 29 & 31 Oct, 1 Nov - Fix old forklist attachment; start using Gyro sensor and Python functions
Trying to get old forklift attachment to work since it seems more stable; also worked on trying to stabilize current fork lift attachment - will pick whichever one works best.  Started on a new gyro_straight function - our gyro was reversed, took a while to figure out that we need to set our gyro with reverse direction (to fix angle error measurements were the opposite of what one would expect).
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
team discovered that this approach not the best because if you change the speed of the robot, need to also change the running time - good learning experience.  Reverted to using odometry in robot.straight() for distance calculations.  Did run through of M02 mission and combined M01_M14_M06_M07 missions.
> #### 18 Aug - started mission M02_step_counter; wifi works like a dream.
> #### 13 Aug - working on combined M01_M14_M06_M07 missions; lots of problems with BlueTooth
> #### 11 Aug - working on combined M01_innovation_project, M14_health_units, M06_pull_up_bar, M07_tobot_dance
> #### 6 Aug - continued on mission M14_health_units and combined with M06_pull_up_bar
> #### 4 Aug, 2020 - watched kickoff; read mission rules; started mission M14_health_units 

# Lego EV3 Brick Programming Language Research
## Requirements
### First FLL Competition Must Haves:
* Program must be able to run autonomously on EV3 (cannot have program run on laptop or tablet that sends individual commands to robot)
* no Bluetooth allowed
* Assume no Wifi available 
   * Some Browser based IDE can work without access to Internet(e.g. MakeCode)
   
### Must Have:
* Easy to learn and use
* IDE environment
* Debugging
* Program EV3 directly from IDE (no copy and pasting code from IDE to EV3)
* Performant - program runs on EV3 (not on a client which then sends commands to EV3)
* Free or very low cost

### Nice to have:
* Virtual Robot Simulator
* Block Based with simple translation to text based language (e.g. Blockly code that generates MicroPython)
* Introduce kids to programming a real language
* integration with Github (for version control)

## Pigeons' selection:
* [LEGO EV3 MicroPython](https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3) install on bootable SD card on EV3 brick.
* [Visual Studio Code](https://code.visualstudio.com/) and the [LEGO® MINDSTORMS® EV3 MicroPython](https://marketplace.visualstudio.com/items?itemName=lego-education.ev3-micropython) extension 
* [Lego EV3 Micropython (Pybricks) simulator](https://fll-pigeons.github.io/gamechangers/simulator/public/) (fork of QuirkyCort's [gearsbot](https://gears.aposteriori.com.sg/) )
* Edimax N150 - WiFi Nano USB Adapter - for direct download from laptop to brick

-------------------
# Research
## A. Official Lego EV3 programming environments
### for Home/Retail Sets
* [LEGO MINDSTORMS Retail EV3](https://www.lego.com/en-ca/themes/mindstorms/downloads) ([LabVIEW](https://www.ni.com/en-ca/shop/labview.html) dialect with simplified UI, running on the Lego EV3-G OS)
  * [EV3 Software PC - Windows](https://go.api.education.lego.com/v1/lms-ev3_en-us_win32#noUrlRewrite)
  * [EV3 Programmer Apps](https://play.google.com/store/apps/details?id=com.lego.mindstorms.ev3programmer)
  
### for Education Sets (but can be used with Home version)
* [EV3 Classroom App](https://education.lego.com/en-us/downloads/mindstorms-ev3/software)
  * coding language based on Scratch
  * MacOS, Windows, Android, Ipad
  * called:
    * EV3 Classroom (education) - includes teacher resources
    * [Mindstorms Home (home set)](https://www.lego.com/en-ca/themes/mindstorms/downloads)

* [LEGO EV3 MicroPython](https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3)
Visual Studio Code version 1.31 or above with EV3 MicroPython extension installed
SD Card for EV3 Brick: Micro SDHC (min. 4GB, max. 32GB) with Application Performance Class A1
  * Uses the [Pybricks](https://pybricks.com/) dialect of [MicroPython](https://micropython.org/) for EV3.  [MicroPython](https://micropython.org/) is a subset of [Python](https://www.python.org) used in [microcontrollers](https://en.wikipedia.org/wiki/Microcontroller).
  * LEGO Education has tested and approved version 2.0 of [Pybricks MicroPython](https://pybricks.com/)  as the official EV3 MicroPython application.   
  * [Pybricks MicroPython](https://pybricks.com/) is a runtime and library (called Brickman on the EV3), and is also included with [EV3dev](http://www.ev3dev.org/). 
  * It also comes with a dedicated Visual Studio Code extension that includes project templates and documentation to get started. 
  * Includes debugging
  * [EV3dev startup lag?](https://github.com/fll-pigeons/gamechangers/issues/6)

* Deprecated (superseded by newer code)
  * [LEGO MINDSTORMS Education EV3](https://education.lego.com/en-us/downloads/mindstorms-ev3/software) ([LabVIEW](https://www.ni.com/en-ca/shop/labview.html) dialect with simplified UI, running on the Lego EV3-G OS)

## B. 3rd party EV3 programming environments/languages
* [MakeCode](https://makecode.mindstorms.com) - Microsoft MakeCode is an online block programming platform that can control the EV3 and others.  
  * [Documentation](https://makecode.mindstorms.com/about)
  * USB cable only, downloads directly to EV3; experimental support for Bluetooth
  * [can be used offline](https://makecode.mindstorms.com/offline)
  * Supports [Javascript](https://makecode.mindstorms.com/javascript) on EV3 and and non-EV3 version of MakeCode supports a subset of [Python](https://makecode.mindstorms.com/python) (not MicroPython), therefore No Python on EV3 version of Makecode... yet!
  * [How to Run Microsoft MakeCode in the Virtual Robotics Toolkit](https://www.youtube.com/watch?v=VOQLvFCIAdI)
  * powered by [Microsoft PXT](https://github.com/Microsoft/pxt)

* [EV3dev](http://www.ev3dev.org/) - debian Linux on EV3, bootable from SD card
    * [Demo - Programming Lego Mindstorms robots with Python](https://www.youtube.com/watch?v=kyfbYv6eZQQ) ([Jupyter Notebook on github](https://github.com/sshopov/pyconau2017)) - running Python directly on EV3 brick running Debian; creates Jupiter server on brick that is accessible from client browser on laptop)
  * [EV3DEV Python v2](https://sites.google.com/site/ev3devpython/) 
    * uses Microsoft's Visual Studio Code (VS Code) with the EV3 extension (uses EV3DEV code on SD Card without having to reflash firmware)
    * This is a full Python - not a subset of Python like [LEGO EV3 MicroPython](https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3)
  * ~~[EV3Python - version 1 - deprecated](https://sites.google.com/site/ev3python/)~~
  * ~~[EV3 BASIC](https://sites.google.com/site/ev3basic/) - Windows only - developer of this recommends using EV3 Python~~
    * ~~EV3 Basic is a textual programming language.~~

* [BluPants Robot](https://www.hackster.io/blupantsrobot/coding-with-lego-ev3-and-blupants-e70c3d) (based on EV3Dev)
  * [BluPants Studio](http://blupants.org/) - 3 levels of codeing: basic movement blocks, blockly type programming blocks and python.  requires a robot to be connected - no virtual environment.

* [LabVIEW for LEGO MINDSTORMS ](https://www.ni.com/en-ca/support/downloads/software-products/download.labview-for-lego-mindstorms.html)
LabVIEW for LEGO MINDSTORMS (LVLM) and LabVIEW for Education (LV4E) are visual programming environments. 
The EV3 Software was built in LabVIEW, LVLM is the base software and is much more powerful.

* [ROBOTC for LEGO MINDSTORMS 4.x](http://www.robotc.net) ($49USD/year/seat; $149USD/year/6seats) - by [Robomatter](https://www.robomatter.com/)
  * RobotC is a C-based programming language with a fully integrated software debugger that supports a range of different hardware platforms. 
  * Has an entry level block-level programming version of RobotC. 
  * Lots of documentation and online support. 
  * requires variable declarations and is thus wordier than MicroPython  
  * Can be used with [Robot Virtual Worlds (RVW)](http://www.robotvirtualworlds.com/) (at additional cost of $49USD/seat/year; $149USD/6seats/year)
    * License cost depends on whether you run RobotC in virtual vs physical EV3.  If only use RVW, then can use RobotC with no need for additional RobotC license, but if want to run code on a physical EV3, then need a Physical RobotC license.

* [Java with leJOS](http://www.lejos.org/ev3.php)
Tiny Java Virtual Machine that supports Java. 

* [C4EV3](https://c4ev3.github.io/) 
Native C/C++ Programming for the LEGO® EV3

### browser-based block programming IDE
  * [Browser-based IDE Disadvantages](https://thecodingfun.com/2020/05/28/is-it-a-good-alternative-to-use-microsoft-makecode-to-program-lego-mindstorms-ev3-part-2/) (browser based languages may make debugging more difficult)
  
* [gearsbot](https://gears.aposteriori.com.sg/) - Blockly to Python-evedev &  PyBricks support soon

* [Lego EV3 Micropython (Pybricks) simulator](/simulator/public/) (fork of QuirkyCort's [gearsbot](https://gears.aposteriori.com.sg/) )

* [OpenRoberta](https://lab.open-roberta.org/)
  * Open Roberta is a free, drag and drop, cloud-based platform for programming LEGO EV3 and NXT robots. 
  * have an in browser 2d virtual environment
  * block-based programming that translates to EV3Python

* [VEXcode VR](https://vr.vex.com/)
  * Block-based and Python IDE programming
  * 3D virtual environment
  * lots of activities and examples
  * good option to expose student to programmatic/algorithmic thinking
  * cons: 
    * VEX centric robot
    * no pybricks micropython    

* [CoderZ](https://gocoderz.com/) ($6.25USD/month/paid yearly)
CoderZ is a 3D simulated robot environment using virtual robots that are similar to the EV3 robot.
Programming can be done with either Blockly or Java programming languages. 
For CoderZ to work with LEGO® MINDSTORMS® EV3 You will need to install [leJOS](http://www.lejos.org/ev3.php) on your EV3 Brick.

* ~~[Scratch](https://scratch.mit.edu/)~~
  * ~~Bluetooth only - can't use in competition~~
  * ~~Visual programming environment. need Scratch link to support the EV3.~~

## C. Alternative Brick Operating Systems
* two different approaches: replace the Lego EV3 firware with a 3rd party version or boot another O/S from SD card

### 3rd Party Firmware for the EV3 Brick (Flash Brick with new firmware)
* [leJOS](http://www.lejos.org/ev3.php)
  * tiny Java Virtual Machine that supports Java. 
* [c4ev3](https://c4ev3.github.io/) is a software package for programming stock-firmware LEGO® Mindstorms® EV3 in C/C++. 

### 3rd Party Virtual Machine installable from SD card on EV3 brick (boot from SD Card Linux image)
* [Pybricks](https://pybricks.com/) Pybricks builds on [MicroPython](http://www.micropython.org/), which is a super-efficient version of Python that can run on the microcontrollers inside smart hubs like Lego's EV3.  
  * It runs on top of  [EV3dev](http://www.ev3dev.org/).
  * Your code runs on the EV3 brick, so it runs as fast as Legos EV3 Labview (As opposed to other software where the robot is essentially remote controlled from a tablet or PC).  
  * It can run programs autonomously.

* [EV3dev](http://www.ev3dev.org/) - debian Linux on EV3, bootable from SD card
EV3dev isn’t actually a programming language, but rather a Debian Linux-based operating system that can run almost all languages that any other linux distribution can run, including C++, Node.js, and Python. 

* [ROBOTC for LEGO MINDSTORMS 4.x](http://www.robotc.net):
  * need to install ROBOTC Virtual Machine (VM) on an updated EV3 Linux Kernel/firmware, to enable you to program your EV3 with ROBOTC. 

* [C-STEM Studio](https://c-stem.ucdavis.edu/studio/)

## D. Simulation Environments
### free/browser-based
#### 3D simulators
* [gearsbot](https://gears.aposteriori.com.sg/) - Blockly to Python-evedev &  PyBricks support soon

* [Lego EV3 Micropython (Pybricks) simulator](https://fll-pigeons.github.io/gamechangers/simulator/public/) (fork of QuirkyCort's [gearsbot](https://gears.aposteriori.com.sg/) )

* [robocatz](https://www.robocatz.com/simulation-launcher.htm) - Browser based RobotC simulator

#### 2D simulators
* [Ev3devSim](https://www.aposteriori.com.sg/Ev3devSim/index.html) - Browser-based Simulator for EV3DEV (uses [Skulpt](https://skulpt.org/) for in browser python)

* [OpenRoberta](https://lab.open-roberta.org/) 2D in browser virtual environment

* [QEV3Bot Simulator](https://sites.google.com/site/qev3bot/qev3bot-simulator) - educational, real-time Windows based graphical simulator that accurately models a QEV3Bot running any RobotC program 

* [roboblockly](https://www.roboblockly.org/about.php) - C/C++ interpreter

* [TRIK Studio](https://trikset.com/en#ts) - supports EV3 ([on Github](https://github.com/trikset/trik-studio))
  * uses graphical block environment to program and downloads standard VM bytecode to EV3 (ASM like language) ([paper](https://www.researchgate.net/publication/320662310_TRIK_studio_Technical_introduction))

* [Google's Blockly Games](https://blockly.games/?lang=en)

* [Roboblockly](https://www.roboblockly.org)

* [ev3dev2simulator](https://github.com/ev3dev-python-tools/ev3dev2simulator)

* [reeborg](https://reeborg.ca/reeborg.html) - 2D browser environment (Python/Javascript)

### Paid/browser-based
* [CoderZ](https://gocoderz.com/) ($6.25USD/month/paid yearly)
  
### Desktop-based/paid
#### 3D simulators - desktop
* [Virtual Robotics Toolkit (VRT)](https://www.virtualroboticstoolkit.com/) - 3D Simulator (uses Unity) - by [Cogmation Robotics](https://cogmation.com/)
  * [First Robotics Canada VRT free license](https://www.firstroboticscanada.org/cancode/vrt/) 
    * use Lego EV3 LabView natively - open both programs and LabView communicates with VRT as if were a real lego robot.
    * can import LDD student designed robots into VRT
    * is finicky to set up
    * graphics intensive - sluggish on slower computers

* [Robot Virtual Worlds (RVW)](http://www.robotvirtualworlds.com/) ($49USD/seat/year; $149USD/6seats/year) - by [Robomatter](https://www.robomatter.com/)
  * Includes RobotC IDE at no additional cost.  
  * If want to run RobotC on a physical EV3, need to pay for an additional RobotC license ($49USD/seat/year; $149USD/6seats/year)!
  * [Virtual Brick for MINDSTORMS - EV3 simulator](http://www.robotvirtualworlds.com/virtualbrick/) - using RobotC
  
--------

# [Developer Notes](developerNotes.md)


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

## Official Lego EV3 programming environments
### for Home/Retail Sets
* [LEGO MINDSTORMS Retail EV3](https://www.lego.com/en-ca/themes/mindstorms/downloads) ([LabVIEW](https://www.ni.com/en-ca/shop/labview.html) dialect with simplified UI, running on the Lego EV3-G OS)

### for Education Sets (but can be used with Home version)
* [LEGO MINDSTORMS Education EV3](https://education.lego.com/en-us/downloads/mindstorms-ev3/software) ([LabVIEW](https://www.ni.com/en-ca/shop/labview.html) dialect with simplified UI, running on the Lego EV3-G OS)

* [LEGO EV3 MicroPython](https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3)
Visual Studio Code version 1.31 or above with EV3 MicroPython extension installed
SD Card for EV3 Brick: Micro SDHC (min. 4GB, max. 32GB) with Application Performance Class A1
  * uses new [Pybricks MicroPython](https://pybricks.com/) runtime and library (called Brickman on the EV3).  LEGO Education has tested and approved version 2.0 of [Pybricks MicroPython](https://pybricks.com/)  as the official EV3 MicroPython application. 
  * [Pybricks MicroPython](https://pybricks.com/) is a program included with [EV3dev](http://www.ev3dev.org/) virtual machine/runtime 
  * It also comes with a dedicated Visual Studio Code extension that includes project templates and documentation to get started. 
  * Includes debugging
  * Documentation
    * [Getting started with LEGO® MINDSTORMS Education EV3 MicroPython](https://pybricks.github.io/ev3-micropython/index.html) (pybricks github.io documentation)
    * [Pybricks (not just for EV3)](https://docs.pybricks.com/en/latest/index.html) (pybricks.com documentation)

* [MakeCode](https://makecode.mindstorms.com) - Microsoft MakeCode is an online block programming platform that can control the EV3 and others.  
  * [Documentation](https://makecode.mindstorms.com/about)
  * USB cable only, downloads directly to EV3; experimental support for Bluetooth
  * [can be used offline](https://makecode.mindstorms.com/offline)
  * Supports [Javascript](https://makecode.mindstorms.com/javascript) and a subset of [Python](https://makecode.mindstorms.com/python) (not MicroPython).
  * [How to Run Microsoft MakeCode in the Virtual Robotics Toolkit](https://www.youtube.com/watch?v=VOQLvFCIAdI)
  * powered by [Microsoft PXT](https://github.com/Microsoft/pxt)

## 3rd party EV3 programming environments/languages
* [EV3dev](http://www.ev3dev.org/) - debian Linux on EV3, bootable from SD card
    * [Demo - Programming Lego Mindstorms robots with Python](https://www.youtube.com/watch?v=kyfbYv6eZQQ) ([Jupyter Notebook on github](https://github.com/sshopov/pyconau2017)) - running Python directly on EV3 brick running Debian; creates Jupiter server on brick that is accessible from client browser on laptop)
  * [EV3DEV Python v2](https://sites.google.com/site/ev3devpython/) 
    * uses Microsoft's Visual Studio Code (VS Code) with the EV3 extension (uses EV3DEV code on SD Card without having to reflash firmware)
    * This is a full Python - not a subset of Python like [LEGO EV3 MicroPython](https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3)
  * ~~[EV3Python - version 1 - deprecated](https://sites.google.com/site/ev3python/)~~
  * ~~[EV3 BASIC](https://sites.google.com/site/ev3basic/) - Windows only - developer of this recommends using EV3 Python~~
    * ~~EV3 Basic is a textual programming language.~~
  * [Ev3devSim](https://www.aposteriori.com.sg/Ev3devSim/index.html) - Browser-based Simulator for EV3DEV - 2D only

* [LabVIEW for LEGO MINDSTORMS ](https://www.ni.com/en-ca/support/downloads/software-products/download.labview-for-lego-mindstorms.html)
LabVIEW for LEGO MINDSTORMS (LVLM) and LabVIEW for Education (LV4E) are visual programming environments. 
The EV3 Software was built in LabVIEW, LVLM is the base software and is much more powerful.

* [ROBOTC for LEGO MINDSTORMS 4.x](http://www.robotc.net) ($49USD/year/seat; $149USD/year/6seats)
  * RobotC is a C-based programming language with a fully integrated software debugger that supports a range of different hardware platforms. 
  * Has an entry level block-level programming version of RobotC. 
  * Lots of documentation and online support. 
  * requires variable declarations and is thus wordier than MicroPython  
  * Can be used with [Robot Virtual Worlds (RVW)](http://www.robotvirtualworlds.com/) ($49USD/seat/year; $149USD/6seats/year - not clear if separate license required or if ROBOTC license includes RVW)

* [Java with leJOS](http://www.lejos.org/ev3.php)
Tiny Java Virtual Machine that supports Java. 

### browser-based block programming IDE
  * [Browser-based IDE Disadvantages](https://thecodingfun.com/2020/05/28/is-it-a-good-alternative-to-use-microsoft-makecode-to-program-lego-mindstorms-ev3-part-2/) (browser based languages make debugging more difficult)


  
* [Ev3devSim](https://www.aposteriori.com.sg/Ev3devSim/index.html) - Browser-based EV3DEv Python IDE with 2D Virtual Robot Simulator

* [OpenRoberta](https://lab.open-roberta.org/)
  * Open Roberta is a free, drag and drop, cloud-based platform for programming LEGO EV3 and NXT robots. 
  * have an in browser 2d virtual environment
  * block-based programming that translates to EV3Python

* [CoderZ](https://gocoderz.com/) ($6.25USD/month/year)
CoderZ is a 3D simulated robot environment using virtual robots that are similar to the EV3 robot.
Programming can be done with either Blockly or Java programming languages. 
For CoderZ to work with LEGO® MINDSTORMS® EV3 You will need to install [leJOS](http://www.lejos.org/ev3.php) on your EV3 Brick.

* ~~[Scratch](https://scratch.mit.edu/)~~
  * ~~Bluetooth only - can't use in competition~~
  * ~~Visual programming environment. need Scratch link to support the EV3.~~
  
### 3rd Party Firmware for the EV3 Brick
* [leJOS](http://www.lejos.org/ev3.php)
LeJOS (pronounced like the Spanish word “lejos” for “far”) is a tiny Java Virtual Machine that supports Java. 
* [c4ev3](https://c4ev3.github.io/) is a software package for programming stock-firmware LEGO® Mindstorms® EV3 in C/C++. 

### 3rd Party Virtual Machine installable from SD card on EV3 brick (boot from SD Card Linux image)
* [Pybricks](https://pybricks.com/) Pybricks builds on [MicroPython](http://www.micropython.org/), which is a super-efficient version of Python that can run on the microcontrollers inside smart hubs like Logo's EV3.  
  * It runs on top of  [EV3dev](http://www.ev3dev.org/).
  * Your code runs on the EV3 brick, so it runs as fast as Legos EV3 Labview (As opposed to other software where the robot is essentially remote controlled from a tablet or PC).  
  * It can run programs autonomously.

* [EV3dev](http://www.ev3dev.org/) - debian Linux on EV3, bootable from SD card
EV3dev isn’t actually a programming language, but rather a Debian Linux-based operating system that can run almost all languages that any other linux distribution can run, including C++, Node.js, and Python. 

* [ROBOTC for LEGO MINDSTORMS 4.x](http://www.robotc.net):
  * need to install ROBOTC Virtual Machine (VM) on an updated EV3 Linux Kernel/firmware, to enable you to program your EV3 with ROBOTC. 

# Virtual Environments
### Free
* [Virtual Robotics Toolkit (VRT)](https://www.virtualroboticstoolkit.com/) - 3D Simulator (uses Unity)
  * [First Robotics Canada VRT free license](https://www.firstroboticscanada.org/cancode/vrt/) 
    * use Lego EV3 LabView natively - open both programs and LabView communicates with VRT as if were a real lego robot.
    * is finicky to set up
    * graphics intensive - sluggish on slower computers

* [Ev3devSim](https://www.aposteriori.com.sg/Ev3devSim/index.html) - 2D Browser-based Simulator for EV3DEV (uses [Skulpt](https://skulpt.org/) for in browser python)

* [OpenRoberta](https://lab.open-roberta.org/) 2D in browser virtual environment

* [QEV3Bot Simulator](https://sites.google.com/site/qev3bot/qev3bot-simulator) - 2D educational, real-time WindowsTM based graphical simulator that accurately models a QEV3Bot running any RobotC program 

### Paid
* [CoderZ](https://gocoderz.com/) ($6.25USD/month) - best Web-based simulator

* [Robot Virtual Worlds (RVW)](http://www.robotvirtualworlds.com/) - RobotC 
  * [Virtual Brick - EV3 simulator](http://www.robotvirtualworlds.com/virtualbrick/) ($49USD/seat/year; $149USD/6seats/year)

# Other software
* [Lego Digital Designer](https://www.lego.com/en-us/ldd)

# Developer Notes

### EV3 C programming environment
* [c4ev3](https://c4ev3.github.io/) programming stock-firmware LEGO® Mindstorms® EV3 in C/C++. 

### Visual Editor Toolkits
* [Google Blockly](https://developers.google.com/blockly) A JavaScript library for building visual programming editors.
  * can generate Javscript, Python code
  * Sample implementations
     * [blockpy](https://blog.ouseful.info/2016/02/18/blockpy-python-blockly-environment/)
     * [Microsoft's PXT](https://github.com/Microsoft/pxt)
     
* [Microsoft Programming Experience Toolkit (PXT)](https://github.com/Microsoft/pxt), PXT is a framework for creating special-purpose programming experiences for beginners, especially focused on computer science education. 
   * [Blockly](https://developers.google.com/blockly)-based code editor along with converter to the text format
   * [Monaco code](https://microsoft.github.io/monaco-editor/) editor that powers [VS Code](https://github.com/Microsoft/vscode),
 
* [Droplet](https://github.com/PencilCode/droplet) The graphical programming editor that powers [Pencil Code](https://guide.pencilcode.net/home/) - 
  * teaches programming in Coffeescript

* [Snap](https://snap.berkeley.edu/) Viual Block Editor - no code generation
  * A Scratch-inspired graphical programming language, it's not a library but is instead a full app with an integrated execution environment.

* [Project BIPES - Integrating Blockly, Micropython, WebREPL, much more!](http://www.bipes.net.br/)
  * Browser-based Block Integrated Platform for Embedded Systems.
  * Server Micropython compilation server
  * should work with EV3 - needs testers
  * based on [Blopy](https://github.com/mnoriaki/Blopy)
  
## Arduino
* [ardublockly-micropython](https://github.com/immakermatty/ardublockly-micropython)

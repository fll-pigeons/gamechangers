# Hardware - EV3 Brick

## Bluetooth - Win10 -> Ev3

### 2 steps to set up Bluetooth for EV3

#### A. One time setup - Bluetooteh Pairing - Windows 10 pairs with EV3 brick

Setup to pair ev3dev with Windows 10 using bluetooth.

on EV3:

    Wireless and Networks
      > Bluetooth
         > Powered X
         > Visible  X
         > Devices kmaclean-laptop

on Windows: 

    Settings
      > Bluetooth & Other Devices
        > Bluetooth On

#### B. Network Connection - each time you want to use your device in Visual Studio

EV3 still does not show up  Visual Studio Code (VSCode), need to 'Connect' EV3 with computer each time you restart VSCode.

On EV3:

    Wireless and Networks 
      > All Network Connections 
        > {PC-Name} 
           > Connect on the brick.

(Going to Bluetooth device and connecting does not work... need to go to All Network Connections to reconnect)

In VSCode

    EV3DEV Device Browser
      > reconnect
EV3 should now show up in VSCode.

see: https://github.com/ev3dev/vscode-ev3dev-browser/issues/85


# Troubleshooting

### 1. replace batteries

### 2. When all else failes... remove Bluetooth pairing on Windows and Ev3dev
*  Windows > System Settings > Bluetooth & other devices
   * delete pairing
   * turn off Bluetooth

* EV3 > Wireless Networks > Bluetooth > delete laptop device

* Restart Windows and Ev3dev

* re-pair devices
  * Windows  > System Settings > Bluetooth & other devices
    * Bluetooth On
  * EV3 > Wireless Networks > Bluetooth
    * Visible - on
    * scan start
  * Windows  > System Settings > Bluetooth & other devices
    * Add a Device
      * ev3dev - select
      *   connecting
      * Press Connct if the PIB on the ev3dec matches this one
  * EV3 > Wireless Networks > Bluetooth
    * Accept PIN
  * Windows  > System Settings > Bluetooth & other devices
    * Connect
      * Setting up device
      * Device is ready
      * Done

* Bluetooth connect
  * EV3 > Wireless Networks > Bluetooth
    * laptop (whatever name of you Win device is)
    
* Windows > Visual Studio > EV3Dev Device Browser > connect
  * select ev3dev Bluetooth Netowrk connection2
  


# EV3's successor

[LEGO reveals new Mindstorms 51515 Robot Inventor](https://www.brothers-brick.com/2020/06/12/lego-reveals-new-mindstorms-51515-robot-inventor-a-5-in-1-robotics-and-coding-set-news/)

the Robot Inventor, LEGO has now fully transitioned to what he called the LPF 2.0 (LEGO Power Functions 2.0) system which features the same interface across [Powered Up components](https://www.brothers-brick.com/2020/05/30/three-new-powered-up-technic-hubs-and-motors-will-be-available-from-lego-in-june-news/), Control+ app, [Boost](https://www.brothers-brick.com/2018/02/16/lego-boost-17101-creative-toolbox-review/), [SPIKE Prime](https://www.brothers-brick.com/2020/01/17/a-new-lease-on-learning-with-lego-education-set-45678-spike-prime-review/) and now Mindstorms. He said that the new LPF 2.0 hardware is not backwards compatible with the EV3, though the Powered Up app now supports some control of past Power Functions components.

Robot Inventor coding app uses a visual drag-and-drop coding language based on Scratch and supports Python for more advanced coders.

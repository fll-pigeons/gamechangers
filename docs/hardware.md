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

go to Wireless and Networks 
  > All Network Connections 
    > {PC-Name} 
       > Connect on the brick.

EV3 should now show up in VSCode.

see: https://github.com/ev3dev/vscode-ev3dev-browser/issues/85

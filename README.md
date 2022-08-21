
# xbox-controller-tool
A real time input test for your gamepad.

## Install requirements
To install all the requierements you need to execute this command line:
>pip3 install -r requirements.txt

## Execute the program
You can check the state of the buttons, triggers and joysticks with a real time console panel executing this command line:
>python3 gamepadtest.py

## Test to scan for gamepads
If you only want to test if there is any gamepad connected to your PC, then run the following command
> python3 gamepadtest.py -t

If the program has detected any controller will display a message like this:
`Detected gamepad --> <Your controller's name>`
Otherwise the message is:
`No gamepad found`

## Help
There is a help panel. You can display it by executing this command line:
>python3 gamepadtest.py -h

The program supports USB and Wireless connections.
Note: The program can scan any kind of gamepad like Dualshock 4, but the buttons names are from Xbox 

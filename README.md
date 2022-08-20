
# xbox-controller-tool
A tool for xbox controllers.

## Install requirements
To install all the requierements you need to execute this command line:
>pip3 install -r requirements.txt

## Execute the program to test your controller
> python3 xbox_input.py -t

If the program has detected any controller will display a message like this:
`Detected gamepad --> <Your controller's name>`
Otherwise the message is:
`No gamepad found`

## Buttons and joysticks test
You can check the state of the buttons, triggers and joysticks with a real time console panel executing this command line:
>python3 xbox_input.py -rt

## Help
There is a help panel. You can display it by executing this command line:
>python3 xbox_input.py -h

The program supports USB and Wireless connections.
Note: The program can scan other types of gamepad like Dualshock 4, but the buttons names are from Xbox 

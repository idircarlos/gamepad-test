import controller
from sys import argv

if argv.__contains__("-h") or argv.__contains__("--help") :
    print("Usage: python3 gamepadtest.py [mode]")
    print("Check the state of your xbox controller with a real time input display\n")
    print("This is the list of available modes:")
    print("\t-h, --help\t\tdisplay this help and exit")
    print("\t-t, --test\t\tcheck if any controller is connected")
    exit(0)

def scan_gamepad():
    cont = controller.Controller()
    if cont.gamepad == None:
        print("No gamepad found")
        exit(1)
    else:
        print("Detected gamepad -->",controller.gamepads[-1].get_name())
    return cont

if argv.__contains__("-t") or argv.__contains__("--test") :
    scan_gamepad()
    exit(0)

cont = scan_gamepad()
cont.rt_input()
import controller
from sys import argv

def scan_gamepad():
    cont = controller.Controller()
    if cont.joystick == None:
        print("No gamepad founded")
        exit(1)
    else:
        print("Detected gamepad -->",controller.joysticks[-1].get_name())
    return cont

if argv.__contains__("-t") or argv.__contains__("--test") :
    scan_gamepad()
    exit(0)

if argv.__contains__("-rt") or argv.__contains__("--real-time") :
    cont = scan_gamepad()
    cont.rt_input()
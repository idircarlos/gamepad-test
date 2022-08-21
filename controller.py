import signal
import cursor
import button as btn
import gamepad as gp
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

pygame.init()
gamepads = []
UP = "\x1B[21A" # Moves up 21 times for \r
CLR = "\x1B[0K" # Clears
UP_REDO = "\x1B[2A"

def signal_handler(sig, frame):
    cursor.show()
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

def create_underline(len):
    res = ""
    for i in range (0,len):
        res = res + "-"
    return res
    
class Controller:
    
    def printf_coords(self,joy):
        coords = self.gamepad.get_button(joy).coords
        _x = round(coords[0],2)
        _y = round(coords[1],2)
        return str("(" + str(_x) + "," + str(_y) + ")")
    
    def refresh(self):
        for event in pygame.event.get():
            dict = event.__dict__
            button_id = dict.get("button")
            value_val = dict.get("value")
            axis_val = dict.get("axis")
            if button_id is not None and button_id >= btn.BT_A and button_id <= btn.BT_RS:
                self.gamepad.get_button(button_id).action()
            elif axis_val == 0:
                self.gamepad.get_button(btn.BT_JL).enable_joy_x(value_val)
            elif axis_val == 1:
                self.gamepad.get_button(btn.BT_JL).enable_joy_y(value_val)
            elif axis_val == 2:
                self.gamepad.get_button(btn.BT_JR).enable_joy_x(value_val)
            elif axis_val == 3:
                self.gamepad.get_button(btn.BT_JR).enable_joy_y(value_val)
            elif axis_val == 4:
                self.gamepad.get_button(btn.BT_LT).enable_trigger(value_val)
            elif axis_val == 5:
                self.gamepad.get_button(btn.BT_RT).enable_trigger(value_val)
            elif type(value_val) is tuple:
                if value_val == (0,1):
                    self.gamepad.get_button(btn.BT_DOWN).disable()
                    self.gamepad.get_button(btn.BT_LEFT).disable()
                    self.gamepad.get_button(btn.BT_RIGHT).disable()
                    self.gamepad.get_button(btn.BT_UP).enable()
                elif value_val == (1,0):
                    self.gamepad.get_button(btn.BT_RIGHT).enable()
                    self.gamepad.get_button(btn.BT_LEFT).disable()
                    self.gamepad.get_button(btn.BT_UP).disable()
                    self.gamepad.get_button(btn.BT_DOWN).disable()  
                elif value_val == (0,-1):
                    self.gamepad.get_button(btn.BT_UP).disable()
                    self.gamepad.get_button(btn.BT_LEFT).disable()
                    self.gamepad.get_button(btn.BT_RIGHT).disable()
                    self.gamepad.get_button(btn.BT_DOWN).enable()
                elif value_val == (-1,0):
                    self.gamepad.get_button(btn.BT_LEFT).enable()
                    self.gamepad.get_button(btn.BT_RIGHT).disable()
                    self.gamepad.get_button(btn.BT_UP).disable()
                    self.gamepad.get_button(btn.BT_DOWN).disable()
                elif value_val == (1,1):
                    self.gamepad.get_button(btn.BT_RIGHT).enable()
                    self.gamepad.get_button(btn.BT_UP).enable()
                elif value_val == (-1,-1):
                    self.gamepad.get_button(btn.BT_LEFT).enable()
                    self.gamepad.get_button(btn.BT_DOWN).enable()
                elif value_val == (-1,1):
                    self.gamepad.get_button(btn.BT_LEFT).enable()
                    self.gamepad.get_button(btn.BT_UP).enable()
                elif value_val == (1,-1):
                    self.gamepad.get_button(btn.BT_RIGHT).enable()
                    self.gamepad.get_button(btn.BT_DOWN).enable()
                elif value_val == (0,0):
                    self.gamepad.get_button(btn.BT_UP).disable()
                    self.gamepad.get_button(btn.BT_RIGHT).disable()
                    self.gamepad.get_button(btn.BT_DOWN).disable()
                    self.gamepad.get_button(btn.BT_LEFT).disable()
            
    def A(self):
        self.refresh()
        return self.gamepad.get_button(btn.BT_A).pressed

    def B(self):
        self.refresh()
        return self.gamepad.get_button(btn.BT_B).pressed
    
    def X(self):
        self.refresh()
        return self.gamepad.get_button(btn.BT_X).pressed

    def Y(self):
        self.refresh()
        return self.gamepad.get_button(btn.BT_Y).pressed
    
    def L(self):
        self.refresh()
        return self.gamepad.get_button(btn.BT_L).pressed

    def R(self):
        self.refresh()
        return self.gamepad.get_button(btn.BT_R).pressed
    
    def LS(self):
        self.refresh()
        return self.gamepad.get_button(btn.BT_LS).pressed

    def RS(self):
        self.refresh()
        return self.gamepad.get_button(btn.BT_RS).pressed
    
    def Select(self):
        self.refresh()
        return self.gamepad.get_button(btn.BT_SELECT).pressed

    def Start(self):
        self.refresh()
        return self.gamepad.get_button(btn.BT_START).pressed
    
    def rt_input(self):
        cursor.hide()
        os.system("clear")
        print("\n\n")
        controller_test_len = len(gamepads[-1].get_name() +  "Testing -> ")
        underline = create_underline(controller_test_len)
        while self.keep_rt:
            self.refresh()
            print(f"{UP}Testing -> {gamepads[-1].get_name()}{CLR}\n" + 
                  f"{underline}{CLR}\n" +
                  f"A: {self.gamepad.get_button(btn.BT_A).pressed}{CLR}\nB: {self.gamepad.get_button(btn.BT_B).pressed}{CLR}\n"+
                  f"X: {self.gamepad.get_button(btn.BT_X).pressed}{CLR}\nY: {self.gamepad.get_button(btn.BT_Y).pressed}{CLR}\n" + 
                  f"L: {self.gamepad.get_button(btn.BT_L).pressed}{CLR}\nR: {self.gamepad.get_button(btn.BT_R).pressed}{CLR}\n" +
                  f"Select: {self.gamepad.get_button(btn.BT_SELECT).pressed}{CLR}\nStart: {self.gamepad.get_button(btn.BT_START).pressed}{CLR}\n" +
                  f"LS: {self.gamepad.get_button(btn.BT_LS).pressed}{CLR}\nRS: {self.gamepad.get_button(btn.BT_RS).pressed}{CLR}\n" +
                  f"Up: {self.gamepad.get_button(btn.BT_UP).pressed}{CLR}\nRight: {self.gamepad.get_button(btn.BT_RIGHT).pressed}{CLR}\n" +
                  f"Down: {self.gamepad.get_button(btn.BT_DOWN).pressed}{CLR}\nLeft: {self.gamepad.get_button(btn.BT_LEFT).pressed}{CLR}\n" +
                  f"LT: {round(self.gamepad.get_button(btn.BT_LT).value,2)}{CLR}\nRT: {round(self.gamepad.get_button(btn.BT_RT).value,2)}{CLR}\n" +
                  f"L3: {self.printf_coords(btn.BT_JL)}{CLR}\nR3: {self.printf_coords(btn.BT_JR)}{CLR}\n")
        print(UP_REDO)
        cursor.show()
                
    def __init__(self):
        n_gamepads = pygame.joystick.get_count()
        if n_gamepads == 0:
            self.gamepad = None
        for i in range(0, n_gamepads):
            # create an gamepad object in our list
            gamepads.append(pygame.joystick.Joystick(i))
            # initialize them all (-1 means loop forever)
            gamepads[-1].init()
            self.gamepad = gp.Gamepad()
            self.keep_rt = True
            
    def __str__(self):
        buttons_str = ""
        for i in range(0,btn.N_BUTTONS):
            button = self.gamepad.get_button(i)
            buttons_str = buttons_str + str(self.gamepad.get_button(i)) + " " + str(button.pressed) + "\n"
        return buttons_str
    

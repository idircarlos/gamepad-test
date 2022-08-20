# Buttons constants
N_BUTTONS = 18
BT_A = 0
BT_B = 1
BT_X = 2
BT_Y = 3
BT_L = 4
BT_R = 5
BT_SELECT = 6
BT_START = 7
BT_LS = 8
BT_RS = 9
BT_UP = 10
BT_RIGHT = 11
BT_DOWN = 12
BT_LEFT = 13
BT_LT = 14
BT_RT = 15
BT_JL = 16
BT_JR = 17

class Button:
    
    def __init__(self, id):
        self.id = id
        self.pressed = False
        self.value = -1.00
        # If is a joystick, then creates a pair of coords
        if (id == BT_JL or id == BT_JR):
            self.coords = [0,0]
    
    def __repr__(self):
        return str(self)
    
    def action(self):
        if self.id >= BT_A and self.id <= BT_RS:
            self.pressed = not self.pressed
    
    def enable(self):
        self.pressed = True
    
    def disable(self):
        self.pressed = False
        
    def enable(self):
        self.pressed = True
        
    def enable_trigger(self,value):
        self.pressed = True
        self.value = value
    
    def disable_trigger(self):
        self.pressed = False
        self.value = -1.00
        
    def enable_joy_x(self,x):
        self.pressed = False
        self.coords[0] = x
        
    def enable_joy_y(self,y):
        self.pressed = False
        if y < 0:
            new_y = abs(y)
            y = y + 2*new_y
        else:
            y = y - 2*y
        self.coords[1] = y
    
    def __str__(self):
        if self.id == BT_A:
            return 'A'
        if self.id == BT_B:
            return 'B'
        if self.id == BT_X:
            return 'X'
        if self.id == BT_Y:
            return 'Y'
        if self.id == BT_L:
            return 'L'
        if self.id == BT_R:
            return 'R'
        if self.id == BT_SELECT:
            return 'Select'
        if self.id == BT_START:
            return 'Start'
        if self.id == BT_LS:
            return 'LS'
        if self.id == BT_RS:
            return 'RS'
        if self.id == BT_UP:
            return 'Up'
        if self.id == BT_RIGHT:
            return 'Right'
        if self.id == BT_DOWN:
            return 'Down'
        if self.id == BT_LEFT:
            return 'Left'
        if self.id == BT_LT:
            return 'LT'
        if self.id == BT_RT:
            return 'RT'
        
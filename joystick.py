import button as btn

N_BUTTONS = 18

class Joystick:
    
    def __init__(self):
        self.__buttons = []
        for i in range (0,N_BUTTONS):
            self.__buttons.append(btn.Button(i))
            
    def __str__(self) -> str:
        return str(self.__buttons)
    
    def __repr__(self):
        return str(self)
    
    def get_buttons(self):
        return self.__buttons
    
    def get_button(self,i) -> btn.Button:
        return self.__buttons[i]
    
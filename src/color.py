from enum import IntEnum

__color_enable = True

class ConsoleBaseColor(IntEnum):
    BLACK = 0
    RED = 1
    GREEN = 2
    ORANGE = 3
    CYAN = 4
    PURPLE = 5
    BLUEGREEN = 6
    WHITE = 7
    
    def fore(self):
        return f"\033[38;5;{int(self)}m"
    
    def back(self):
        return f"\033[48;5;{int(self)}m"

    def paint(self, text: str):
        if not __color_enable:
            return text
        return self.fore() + text + "\033[m"

def bold(text: str):
    if not __color_enable:
        return text

    return f"\033[1m{text}\033[m"

def disable_color():
    global __color_enable
    __color_enable = False


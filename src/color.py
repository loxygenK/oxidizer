from enum import IntEnum

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
        return self.fore() + text + "\033[m"

def bold(text: str):
    return f"\033[1m{text}\033[m"


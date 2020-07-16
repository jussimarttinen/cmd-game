import keyboard as kb

class Player:

    def __init__(self, x, y):
        # Location of player character
        self.x = x
        self.y = y
        self.symbol = "@"
        self.colour = "green"
    
    def update_position(self, dx, dy):
        self.x += dx
        self.y += dy
        
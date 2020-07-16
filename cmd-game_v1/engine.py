import msvcrt
import graphics_v2 as graphics
from time import sleep
import Player

class Game():
    
    def __init__(self):
    
        self.display = graphics.Display()
        starting_x = self.display.w_width // 2
        starting_y = self.display.w_height // 2
        self.player = Player.Player(starting_x, starting_y)
        # msvcrt symbols for the arrow keys
        self.arrows = {"K": (-1, 0), "M": (1, 0), "H": (0, -1), "P": (0, 1)}
    

    def main_loop(self):
        running = True
        while running:
            sleep(1/15)
            self.display.display_picture(self.player.symbol, colour=self.player.colour, x=self.player.x, y=self.player.y)
            print("")
            self.display.update_dimensions()
            # registers key presses
            if msvcrt.kbhit():
                key = msvcrt.getwch()
                # signifies a special key (in this case arrow)
                # this clause may be redundant but I'm not going to remove it now just in case
                if key == "\xe0":
                    key = msvcrt.getwch()
                if key in self.arrows.keys():
                    # updates player position
                    self.player.update_position(self.arrows[key][0], self.arrows[key][1])

if __name__ == "__main__":
    game = Game()
    game.main_loop()


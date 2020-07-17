import msvcrt
import graphics_v2 as graphics
from time import sleep
import Player
import Frame
import Entities
from random import randint

class Game():
    
    def __init__(self):
    
        self.display = graphics.Display()
        starting_x = self.display.w_width // 2
        starting_y = self.display.w_height // 2

        self.frame = Frame.Frame(self.display.w_width, self.display.w_height)
        
        self.fps = 60

        # list of available skins
        self.player_skins = ["@", "O", "*", "¤"]
        # index of the current player skin
        self.player_skin_index = 0
        self.player_weapons = [[">", "<"], ["~;", ";~"]]
        # creates the player
        self.player = Player.Player(starting_x, starting_y, self.player_skins[self.player_skin_index], weapon_sprites=self.player_weapons[1])
        # creates an instance of tree
        # broken for some reason
        self.tree = Entities.Tree(randint(0,self.display.w_width - 1), randint(0,self.display.w_height - 1))
        
        

        # msvcrt symbols for the arrow keys
        self.arrows = {"K": (-1, 0), "M": (1, 0), "H": (0, -1), "P": (0, 1)}
        
    def get_player_input(self):
        """Checks if the player has pressed a button"""
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
            elif key == "h":
                # adds 1 to the index (loops back to start if necessary)
                self.player_skin_index = (self.player_skin_index + 1) % len(self.player_skins)
                self.player.change_symbol(self.player_skins[self.player_skin_index], ovrwrte_plr_smbl=True)

    def main_loop(self):
        running = True
        while running:
            frame = self.frame.compose_frame(player = self.player.data, tree = self.tree.data)
            self.display.display_picture(frame, colour=self.player.colour)
            self.frame.update_dimensions(self.display.w_width, self.display.w_height)
            print("")
            self.display.update_dimensions()
            # stabilises animation
            sleep(1/self.fps)
            self.display.clear_screen(3*self.display.w_height)

            self.get_player_input()
            

if __name__ == "__main__":
    game = Game()
    game.main_loop()


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
        self.player_skins = ["@", "O", "*", "¤", "o\nO"]
        # index of the current player skin
        self.player_skin_index = 0
        self.player_weapons = [["==;", ";=="], ["~;", ";~"]]
        # creates the player
        self.player = Player.Player(starting_x, starting_y, self.player_skins[self.player_skin_index], weapon_sprites=self.player_weapons[0])
        # creates an instance of tree
        # broken for some reason
        self.tree = Entities.Tree(randint(0,self.display.w_width - 1), randint(0,self.display.w_height - 1))
        
        # for testing purposes
        #self.top_border = Entities.Border(True,"*",self.display)
        #self.bottom_border = Entities.Border(False, "*", self.display)
        self.objects = [self.player, self.tree] #, self.top_border, self.bottom_border]

        # msvcrt symbols for the arrow keys
        self.arrows = {75: (-1, 0), 77: (1, 0), 72: (0, -1), 80: (0, 1)}
        self.logf = open("logs.txt", "w")
        
    def get_player_input(self):
        """Checks if the player has pressed a button"""
        # registers key presses
        if msvcrt.kbhit():
            key = ord(msvcrt.getch())
            # signifies a special key (in this case arrow)
            if key == 224:
                key = ord(msvcrt.getch())
            if key in self.arrows.keys():
                # updates player position
                self.player.update_position(self.arrows[key][0], self.arrows[key][1])
            # 'h'
            elif key == 104:
                # adds 1 to the index (loops back to start if necessary)
                self.player_skin_index = (self.player_skin_index + 1) % len(self.player_skins)
                self.player.change_symbol(self.player_skins[self.player_skin_index], ovrwrte_plr_smbl=True)
            # Escape
            elif key == 27:
                # waits until user presses esc
                self.pause_program()
                

    def main_loop(self):
        try:
            running = True
            while running:
                # creates frame
                frame = self.frame.compose_frame(self.objects)
                self.display.display_picture(frame, colour=self.player.colour)
                self.get_player_input()
                self.frame.update_dimensions(self.display.w_width, self.display.w_height)
                self.display.update_dimensions()
                # stabilises animation
                sleep(1/self.fps)
                #print()
                #self.display.clear_screen(self.display.w_height)
        
        # logs error message
        except Exception as e:
            self.logf.write("Error: " + str(e))
            raise e

    def pause_program(self):    
        paused = True
        # writes a pause message
        pause_message = Entities.Text(self.display.w_width//2, 2*self.display.w_height//3, "Press Esc to continue")
        pause_message.center_text(self.display, horizontal=True)
        frame = self.frame.compose_frame(self.objects + [pause_message])
        self.display.display_picture(frame, colour=self.player.colour)
        while paused:
            # checks if Esc has been pressed
            if msvcrt.kbhit() and ord(msvcrt.getch()) == 27:
                paused = False

if __name__ == "__main__":
    game = Game()
    game.main_loop()


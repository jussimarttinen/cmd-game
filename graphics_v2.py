from shutil import get_terminal_size
from time import sleep
import Colours
from math import ceil

modules = ["colorama"]
try: 
    from colorama import Style, Fore, init
except ModuleNotFoundError:
    print("It seems like you haven't installed a module yet. Please install the necessary modules \
    with the command 'pip install <module name>'")
    print("Possible missing modules:")
    print(module for module in modules)
    raise
    



class Display():
    """Represents the cmd window and handles the graphics"""

    def __init__(self):
        # Initialises Colorama (required for colour support)
        init()
        # terminal dimensions in characters
        self.w_width, self.w_height = get_terminal_size()
        # scales the dimensions to even numbers to make drawing easier
        self.w_width -= self.w_width % 2
        self.w_height -= self.w_height % 2
        # refresh rate will be automatically calculated depending on 
        # screen size and rendering time
        # (to be implemented)
        self.refresh_rate = None

    def update_dimensions(self):
        """Updates the w_width and w_height parameters to account for 
        window resizing."""
        # stores the old screen height for cleaning the screen
        old_w_height = self.w_height

        self.w_width, self.w_height = get_terminal_size()
        # see __init__
        self.w_width -= self.w_width % 2
        self.w_height -= self.w_height % 2

        if old_w_height != self.w_height:
            self.clear_screen(old_w_height)
        
    
    def clear_screen(self, w_height):
        """Clears the screen by printing heigth * linebreak.
        The optional parameter w_height shouldn't be necessary,
        as it's only used when called by update_dimensions()"""

        print("\n"*w_height)

    
    def display_picture(self, picture, colour="white", x=0, y=0):
        """Displays the given picture
        Optional parameter colour determines the text colour

        x and y are the coordinates of the top left corner of the picture 
        (defaults to top left)
        """
        
        # splits the picture into a list
        picture = [Colours.BG_COLS[colour] + line + Colours.BG_COLS["reset"] for line in picture.split("\n")]
        # fixes a bug where the picture is taller than the frame
        # (removes the last item if the string ended in "\n")
        if picture[-1] == Colours.BG_COLS[colour] + Colours.BG_COLS["reset"]:
            picture.pop(-1)

        # calculates the longest line in the picture
        # needed when printing whitespace around it
        # removes the length of the colour codes because this caused a bug
        picture_length = max(len(line) for line in picture) - len(Colours.BG_COLS[colour] + Colours.BG_COLS["reset"])
        # the minimum whitespace that any line has around it

        # prints the horizontal empty rows
        print(y*"\n", end="")

        # prints rest of picture
        for line in picture:
            
            length_difference = picture_length - len(line)
            print((length_difference + x) * " ", end="")
            
            print(line)

        # prints the whitespace under the picture
        print((self.w_height - len(picture) - y) * "\n", end="")



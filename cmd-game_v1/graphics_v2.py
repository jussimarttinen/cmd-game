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

        # calculates the longest line in the picture
        # needed when printing whitespace around it
        picture_length = max(len(line) for line in picture)
        # the minimum whitespace that any line has around it

        # prints the horizontal empty rows
        print(y*"\n")

        # prints rest of picture
        for line in picture:
            
            length_difference = picture_length - len(line)
            print((length_difference + x) * " ", end="")
            
            print(line)

        # prints the whitespace under the picture
        print((self.w_height - len(picture) - y) * "\n")



if __name__ == "__main__":
    
    # creates the display
    display = Display()

    dvd_logo = "\
    `:::::::::::::`      ,,,,,,,,,-     \n\
    VQQBBB@@@@@@@@g    ~Q@@BQQQQB@@@gi  \n\
   :888?   r@@@##@@| `K@@0V888!   r@@@V \n\
   b@@#`  'w@@@w~@@#n#@Q^ Q@@B   -o@@@^ \n\
  ,@@@#%EB@#0z!  n@@@#i  ^@@@#6RB@@Qz_  \n\
  _^^^<~:_`       R#]`   ,<<<<<>=-      \n\
    -=^rv}nzwhmPUwpHXPPmhwzn}i?^=_      \n\
 =8@@@@@@@@@@#i_     `=K@@@@@@@@@@@B*   \n\
   _~rxczhGZdED$$E6OD0$DE6ZSatnxr~*'    \n\
     x``v  r' _v>*`  l^~_  !r^?.        \n\
     :6W,  d= ^Z,wn `@zx: -8!,sn        \n\
      .`   '  `__`   ___`   _\"`         "
    
    # picture colour
    COLOUR = "green"
    # picture
    PICTURE = dvd_logo
    # starting coordinates
    X_CORD = 1
    Y_CORD = 1
    # how much the picture moves
    dx = 1
    dy = 1

    display.update_dimensions()
    sleep(1/2)
    
    frame = 0

    while True:
        sleep(1/30)
        display.update_dimensions()
        display.display_picture(PICTURE, colour=COLOUR, x=X_CORD, y=Y_CORD)
        if frame % 3 == 0:
            X_CORD += dx
            Y_CORD += dy

            # picture is touching left/right edge
            if X_CORD + max(len(line) for line in PICTURE.split("\n")) > display.w_width - 1 or X_CORD < 1:
                dx *= -1
            
            # picture is touching bottom/top edge
            if Y_CORD + len(PICTURE.split("\n")) > display.w_height - 1 or Y_CORD < 2:
                dy *= -1
        frame += 1
    
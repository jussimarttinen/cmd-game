from shutil import get_terminal_size
from time import sleep
import Colours

modules = ["colorama"]
try: 
    from colorama import Style, Fore, init
except ModuleNotFoundError:
    print("It seems like you haven't installed a module yet. Please install the necessary modules \
    with the command 'pip install <module name>'")
    print("Possible missing modules:")
    print(module for module in modules)
    raise
    
# NOTE: This program was a quick reassembly of my other, more generalised cmd animation tool,
# so there are a few unnecessary methods that I'm too lazy to remove




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

        # no need to clear screen if window size hasn't changed
        if old_w_height != self.w_height:
            self.clear_screen(old_w_height)
        
    
    def clear_screen(self, w_height):
        """Clears the screen by printing heigth * linebreak.
        The optional parameter w_height shouldn't be necessary,
        as it's only used when called by update_dimensions()"""

        print("\n"*(w_height))

    
    def display_picture(self, picture, x=0, y=0):
        """Displays the given picture
        Optional parameter colour determines the text colour

        x and y are the coordinates of the top left corner of the picture 
        (defaults to top left)
        """
        
        # splits the picture into a list
        picture = picture.split("\n") 

        # calculates the longest line in the picture
        # needed when printing whitespace around it
        picture_length = max(len(line) for line in picture)
        # the minimum whitespace that any line has around it

        # prints the horizontal empty rows
        print(y*"\n")

        # prints rest of picture
        for line in picture:
            
            # how much whitespace needs to be added in addition to the whitespace
            # that every line has
            length_difference = picture_length - len(line)
            print((length_difference + x) * " ", end="")
            
            print(line)
        

        # prints the whitespace under the picture
        print((self.w_height - len(picture) - y) * "\n", end="")



if __name__ == "__main__":

    # just change this picture to any other string and it should work all the same
    DVD_LOGO = "\
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
    # starting coordinates
    X_CORD = 1
    Y_CORD = 1
    # how much the picture moves
    DX = 1
    DY = 1
    # how many frames are drawn per second
    FPS = 60
    # for how many frames the same picture is repeated
    # doesn't really affect performance, but the animation
    # is imo too fast if set to 1
    REPEATED_FRAMES = 2

    


    # makes the picture coloured
    picture = Colours.BG_COLS[COLOUR] + DVD_LOGO + Colours.BG_COLS["reset"]
    
    # creates the display
    display = Display()
    
    sleep(1/2)
    
    # keeps track of total frames
    frame = 0

    while True:
        # prints the frame
        display.display_picture(picture, x=X_CORD, y=Y_CORD)
        # stabilises the animation
        sleep(1/FPS)

        # clears the screen to prevent picture from lagging
        display.clear_screen(display.w_height)

        # detects if window size has changed
        # this could obviously be done once in every x frames
        # but it shouldn't have a big performance effect
        display.update_dimensions()
        

        # only moves every few frames to not be too fast
        if frame % REPEATED_FRAMES == 0:
            X_CORD += DX
            Y_CORD += DY

            # changes direction if picture is near edge
            # picture is touching left/right edge
            if X_CORD + max(len(line) for line in picture.split("\n")) > display.w_width - abs(DX) or X_CORD < abs(DX):
                DX *= -1
            
            # picture is touching bottom/top edge
            if Y_CORD + len(picture.split("\n")) > display.w_height + abs(DY) or Y_CORD < abs(DY):
                DY *= -1

        frame += 1
    
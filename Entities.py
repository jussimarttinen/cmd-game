class Entity():

    def __init__(self, x, y, sprite=None, colour="white"):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.colour = colour


class Tree(Entity):

    def __init__(self, x, y):
        """For testing purposes only"""
        super().__init__(x, y)
        self.sprite = "^\n" + chr(581)
        self.colour = "green"

class Text(Entity):

    def __init__(self, x, y, text, colour="white"):
        """Prints text. If either centered is true, the text will be automatically 
        centered on that axis"""
        super().__init__(x,y, text, colour)
    
    def center_text(self, display, horizontal=False, vertical=False):
        """Centers the text around chosen axis (or axes). Requires the Display as input"""
        
        formatted_text = self.sprite.split("\n")
        
        if horizontal:
            self.x = (display.w_width - max(len(line) for line in formatted_text)) // 2
        if vertical:
            self.y = (display.w_height - len(formatted_text)) // 2
        
class Border(Entity):

    def __init__(self, is_top_border, symbol, display):
        line = symbol*display.w_width
        if is_top_border:
            y = 0
        else:
            y = display.w_height - 1
        super().__init__(0, y, line)




class Frame():
    
    def __init__(self, w_width, w_height):
        """This class composes the frame from a set of pictures
        w_width: width of frame in symbols
        w_height: height of frame in symbols"""
        self.w_width = w_width
        self.w_height = w_height


    def update_dimensions(self, w_width, w_height):
        self.w_width = w_width
        self.w_height = w_height


    def compose_frame(self, objects):
        """Composes the frame from given objects.
        objects is a list of Entities.Entity or a subclass
        e.g. "player" = Player("@",1,2), "obstacle_1" = Rock("*",3,4)
        Returns the frame as a string
        """

        # NOTE: I know this method is spaghetti, I'll fix
        # it sometime in the future 

        self.frame = ""
        for line in range(self.w_height):
            rendered_line = [" " for x in range(self.w_width)]
            line_objects = dict()  # the data on the line will be added here

            for obj in objects:
                # turns the object's sprite into a list
                sprite = obj.sprite.split("\n")
                # the height of the lowest line of the obj
                lowest_line = obj.y + len(sprite) - 1

                # checks if the object has something that needs to be
                # printed on the line
                if obj.y <= line & lowest_line >= line:

                    sprite_line = sprite[line - obj.y]
                    # matches the x coordinates with the symbols that
                    # appear at that coordinate
                    for x in range(len(sprite_line)):
                        rendered_line[x + obj.x] = sprite_line[x]
            
            # == if rendered line only contains space
            if len(set(rendered_line)) == 1:
                # adds whitespace if whole line is empty
                self.frame += str(line) + "\n"
                continue
            
            # loops through non_whitespace keys
            """for index in line_objects.keys():
                # places characters in their places
                 = line_objects[index]"""
            # removes unnecessary trailing whitespace
            rendered_line = "".join(rendered_line)
            rendered_line.rstrip()
            # adds line to frame
            self.frame += rendered_line + "\n"
        return self.frame
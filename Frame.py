

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
        
    @staticmethod
    def take_first(elem):
        return elem[0]

    def compose_frame(self, **objects):
        """Composes the frame from given objects.
        **objects is of the form name = (picture,x,y)
        e.g. "player" = ("@",1,2), "obstacle_1" = ("|_|",3,4)
        Returns the frame as a string
        """

        # NOTE: I know this method is spaghetti, I promise I'll fix
        # it sometime in the future 

        self.frame = ""
        for line in range(self.w_height):
            rendered_line = ""
            line_objs = []  # the data on the line will be added here, not in order

            for obj in objects.keys():
                # turns the object into a list
                obj_list = objects[obj][0].split("\n")
                # the height of the lowest line of the obj
                lowest_line = objects[obj][2] + len(obj_list) - 1

                # checks if the object has something that needs to be
                # rendered on the line
                if objects[obj][2] <= line & lowest_line >= line:
                    line_height = lowest_line - objects[obj][2]
                    # adds [cord_x, picture] to the list 
                    line_objs.append([objects[obj][1], obj_list[line_height]])
            
            if len(line_objs) == 0:
                # adds whitespace if line is empty
                self.frame += "\n"
                continue
            # sorts the list in order of horizontal coordinate
            sorted_line_objs = sorted(line_objs, key=self.take_first)
            for obj in sorted_line_objs:
                # adds whitespace
                rendered_line += (obj[0] - len(rendered_line))*" "
                # adds object
                rendered_line += obj[1]
            # adds line to frame
            self.frame += rendered_line + "\n"
        return self.frame
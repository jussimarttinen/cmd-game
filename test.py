import Frame
import Colours
import graphics_v2 as graphics


display = graphics.Display()
frame = Frame.Frame(display.w_width, display.w_height)
frame.compose_frame(player = ("@", 2, 3), obstacle = ("T", 20, 0))

display.display_picture(frame.frame)
input()
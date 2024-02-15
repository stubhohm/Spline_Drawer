from Constants.CONSTANTS import *
from Classes.window import Window
from Classes.segments import Segment
from Classes.spline import Spline
from Classes.user_input import UserInput
from Classes.input_object import InputObject
from Classes.enums import EditMode, SelectionMode
from Fonts.FONTS import init_fonts

def init(pygame):
    pygame.font.init()
    init_fonts(pygame)
    pygame.mouse.set_visible(True)
    clock = pygame.time.Clock()
    run = True
    user_input = UserInput(EditMode.Select, SelectionMode.control_points, None, InputObject(), InputObject())
    splines = []
    window = Window()
    print(window.width)
    window.draw_window()
    pygame.display.set_caption("Spline Drawer")
    demo_segment = Segment([150,200],[150,300], [450,600],[450,500])
    demo_spline = Spline()
    demo_spline.segments.append(demo_segment)
    splines.append(demo_spline)
    return clock, run, user_input, window, splines

def main():
    init()  

if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: init"
    )
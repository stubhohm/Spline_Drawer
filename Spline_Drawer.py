import pygame
import math
from Constants.CONSTANTS import *
from Services.init import init
from Services.handle_user_input import handle_user_input
from Services.get_user_input import get_user_input
from Services.render_window import render_window


def main():
    pygame.init()
    clock, run, user_input, window, splines = init(pygame)
    while run:
        clock.tick(FPS)
        user_input.current_input, run = get_user_input(pygame)  
        handle_user_input(pygame, user_input, window, splines, math)
        render_window(pygame, window, splines, user_input)


if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Spline_drawer"
    )

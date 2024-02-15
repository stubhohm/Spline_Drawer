from Constants.CONSTANTS import *
import pygame

class Window:
    def __init__(self,
            display = None,
            height = INIT_WINDOW_HEIGHT,
            width = INIT_WINDOW_WIDTH,
            background_color = INIT_BACKGROUND_COLOR,
            hot_keys = True
            ):
        self.height = height
        self.width = width
        self.background_color = background_color
        self.display = display
        self.hot_keys = hot_keys

    def draw_window(self):
        self.display = pygame.display.set_mode((self.width, self.height))
        self.display.fill(self.background_color)

def main():
    print('window class')

if __name__ == '__main__':
    main()
    print(
        'this main only runs if this file is ran, not if another program executes it: window class'
    )
from Constants.CONSTANTS import *
def get_user_input(pygame):
    run = True
    key_released = None
    key_pressed = None
    
    # handles user quit
    for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                key_released = event.key
            if event.type == pygame.QUIT or key_released == pygame.K_ESCAPE:
                run = False

    key_pressed = pygame.key.get_pressed()
    cursor_pos = pygame.mouse.get_pos()
    cursor_pressed = pygame.mouse.get_pressed(3)

    current_input = {
        "key pressed" : key_pressed,
        "key released" : key_released,
        "cursor position" : cursor_pos,
        "cursor click" : cursor_pressed
    }
    return current_input, run

def main():
    a = 0

if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: get_user_input"
    )
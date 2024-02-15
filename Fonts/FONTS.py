text_font = None
menu_font = None
event_font = None

def init_fonts(pygame):
    global text_font
    global menu_font
    global event_font
    text_font = pygame.font.Font("Fonts//Quinquefive-ALoRM.ttf", 15)
    menu_font = pygame.font.Font("Fonts//Quinquefive-ALoRM.ttf", 10)
    event_font = pygame.font.Font("Fonts//Quinquefive-ALoRM.ttf", 6)

def get_menu_font():
    global menu_font
    return menu_font

def get_event_font():
    global event_font
    return event_font

def get_text_font():
    global text_font
    return text_font

def main():
    a = 0

if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Fonts"
    )
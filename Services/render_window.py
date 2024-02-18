from Classes.window import Window
from Classes.spline import Spline
from Classes.segments import Segment
from Classes.enums import EditMode, SelectionMode, PrintMode
from Fonts.FONTS import get_text_font, get_menu_font, get_event_font
from Constants.CONSTANTS import *

def draw_text(display, text, font, color, h_align, v_align, x, y):
    img = font.render(text, True, color)
    text_size = img.get_size()
    if h_align == "centered":
        a = text_size[0] / 2
    elif h_align == "right":
        a = text_size[0]
    else:
        a = 0
    if v_align == "centered":
        b = text_size[1] / 2
    elif h_align == "bottom":
        b = text_size[1]
    else:
        b = 0
    display.blit(img, (x - a, y - b))

def display_edit_mode(user_input, font, Window):
    text = "Edit Mode:"
    color = WHITE
    if user_input.edit_mode == EditMode.Add:
        text += " Add"
        color = BLUE
    if user_input.edit_mode == EditMode.Select:
        text += " Selection"
        color = WHITE
    if user_input.edit_mode == EditMode.Delete:
        text += " Delete"
        color = RED
    draw_text(Window.display, text, font, color, "right", "top", Window.width, 0)

def display_selection_mode(user_input, font, Window):
    text = "Selction Mode:"
    color = WHITE
    if user_input.selection_mode == SelectionMode.control_points:
        text += " Control Points"
        color = BLUE
    if user_input.selection_mode == SelectionMode.end_points:
        text += " End Points"
        color = WHITE
    if user_input.selection_mode == SelectionMode.segment:
        text += " Segment"
        color = GREEN
    if user_input.selection_mode == SelectionMode.spline:
        text += " Spline"
        color = RED
    draw_text(Window.display, text, font, color, "right", "top", Window.width, Window.height * 1 /64)

def display_print_mode(user_input, font, Window):
    text = "Print Mode:"
    color = WHITE
    if user_input.print_mode == PrintMode.Relative:
        text += " Relative"
        color = BLUE
    elif user_input.print_mode == PrintMode.Absolute:
        text += " Absolute"
        color = RED
    draw_text(Window.display, text, font, color, "right", "top", Window.width, Window.height * 2 /64)

def display_edit_hotkeys(Window, font):
    text = "Show Hot Keys: H"
    if Window.hot_keys:
        text = "Hide Hot keys: H"
        draw_text(Window.display, text, font, WHITE, "left", "top", 0 , 0)
        i = 2
        text = "Edit Modes"
        draw_text(Window.display, text, font, WHITE, "left", "centered", 0 , Window.height * i /64)
        text = "Add: a"
        i += 1
        draw_text(Window.display, text, font, WHITE, "left", "centered", 0 , Window.height * i /64)
        text = "Select: s"
        i +=1
        draw_text(Window.display, text, font, WHITE, "left", "centered", 0 , Window.height * i /64)
        text = "Delete: d" 
        i +=1
        draw_text(Window.display, text, font, WHITE, "left", "centered", 0 , Window.height * i /64)
    else:
       draw_text(Window.display, text, font, WHITE, "left", "top", 0 , 0) 

def display_selection_hotkeys(Window, font):
    text = ""
    if Window.hot_keys:
        i = 7
        text = "Selection Modes"
        draw_text(Window.display, text, font, WHITE, "left", "centered", 0 , Window.height * i /64)
        i += 1
        text = "Control Points: q"
        draw_text(Window.display, text, font, WHITE, "left", "centered", 0 , Window.height * i /64)
        i +=1
        text = "End Points: w"
        draw_text(Window.display, text, font, WHITE, "left", "centered", 0 , Window.height * i /64)
        i +=1
        text = "Segments: e"
        draw_text(Window.display, text, font, WHITE, "left", "centered", 0 , Window.height * i /64)
        i +=1
        text = "Spline: r"
        draw_text(Window.display, text, font, WHITE, "left", "centered", 0 , Window.height * i /64)

def display_print_hotkeys(Window, font):
    text = ""
    if Window.hot_keys:
        i = 4
        text = "Toggle Print Mode: M"
        draw_text(Window.display, text, font, WHITE, "right", "centered", Window.width , Window.height * i /64)
        i += 1
        text = "Print to Terminal: P"
        draw_text(Window.display, text, font, WHITE, "right", "centered", Window.width , Window.height * i /64)

def render_window(pygame, Window, splines, user_input):
    Window.draw_window()
    for spline in splines:
        for segments in spline.segments:
            segments.draw_segment(pygame, Window.display)
    font = get_menu_font()
    display_edit_mode(user_input, font, Window)
    display_selection_mode(user_input, font, Window)
    display_edit_hotkeys(Window, font)
    display_selection_hotkeys(Window, font)
    display_print_hotkeys(Window, font)
    display_print_mode(user_input, font, Window)
    pygame.display.update()

def main():
    a = 0

if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: draw_window"
    )
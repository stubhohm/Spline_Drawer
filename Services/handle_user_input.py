from Classes.enums import EditMode, SelectionMode
from Classes.input_object import InputObject
from Classes.segments import Segment

def add_segment(splines, user_input, pos):
    for spline in splines:
        if len(splines) != 1:
            if spline.segments[0].selected_end != 1 or spline.segment[-1].selected_end != 2:
                continue
        if spline.segments[0] != user_input.selected_element and spline.segments[-1] != user_input.selected_element:
          continue
        if spline.segments[0].selected_end == 1:
            o_p = spline.segments[0].start_point
            o_c = spline.segments[0].start_control_point
            new_o_p, new_e_c = get_new_seg_origin_point_and_control(o_c, o_p, pos)
            new_segment = Segment(new_o_p,  new_o_p, spline.segments[0].start_point, new_e_c)
            spline.segments.insert(0, new_segment)
            clear_selected(splines, user_input)
            spline.segments[0].selected_end == 2
            user_input.selected_segment = spline.segments[0]
        elif spline.segments[-1].selected_end == 2:
            o_p = spline.segments[-1].end_point
            o_c = spline.segments[-1].end_control_point
            new_o_p, new_e_c = get_new_seg_origin_point_and_control(o_c, o_p, pos)
            new_segment = Segment(spline.segments[-1].end_point, new_e_c, new_o_p, new_o_p)
            spline.segments.append(new_segment)
            clear_selected(splines, user_input)
            spline.segments[0].selected_end == 1
            user_input.selected_segment = spline.segments[0]
       
def get_new_seg_origin_point_and_control(o_c, o_p, pos):
    new_e_c = [o_p[0] - o_c[0], o_p[1] - o_c[1]]
    new_o_p = pos
    return new_o_p, new_e_c

def change_point_location(segment, target, position, pos):
    point = pos
    if target == "control":
        if position == 1:
            segment.start_control_point = point
        else:
            segment.end_control_point = point
    else:
        if position == 1:
            segment.start_point = point
        else:
            segment.end_point = point
    return segment

def clear_selected(splines, user_input):
    for spline in splines:
        for segment in spline.segments:
            segment.selected_end = False
    user_input.selected_element = None 

def check_points(start, end, pos, dist, pref):
    if pref == 1:
        first = start
        second = end
    elif pref == 2:
        first = end
        second = start
    else:
        first = start
        second = end
    if first[0] - dist < pos[0] < first[0] + dist:
        if first[1] - dist < pos[1] < first[1] + dist:
            return 1
    if second[0] - dist < pos[0] < second[0] + dist:
        if second[1] - dist < pos[1] < second[1] + dist:
            return 2
    return 0

def look_for_point(pos, splines, target, user_input):
    dis = 10
    for spline in splines:
        for segment in spline.segments:
            if target == "control":
                start = segment.start_control_point
                end = segment.end_control_point
                segment.selected_end = check_points(start, end, pos, dis, None)
            elif target == "end":
                start = segment.start_point
                end = segment.end_point
                segment.selected_end = check_points(start, end, pos, dis, None)
            if segment.selected_end:
                user_input.selected_element = segment
                return
    clear_selected(splines, user_input)

def drag_point(pos, splines, target, user_input):
    position = 0
    dist = 50
    if not user_input.selected_element:
        clear_selected(splines,user_input)
        return
    segment = user_input.selected_element
    if target == "control":
        start = segment.start_control_point
        end = segment.end_control_point
    elif target == "end":
        start = segment.start_point
        end = segment.end_point 
    if user_input.selected_element.selected_end:
        segment = change_point_location(segment, target, user_input.selected_element.selected_end, pos)

def point_selection(mouse, keys, user_input, splines, type, pygame):
    previous_input = user_input.previous_input
    # Check for click start
    if mouse.left_click and not previous_input.mouse.left_click:
        look_for_point(mouse.pos, splines, type, user_input)
    elif mouse.left_click and previous_input.mouse.left_click:
        drag_point(mouse.pos, splines, type, user_input)

def look_for_segment(pos, splines):
    a = 0

def drag_segment(pos,splines):
    a = 0

def look_for_spline(pos, splines):
    a = 0

def drag_spline(pos, splines):
    a = 0

def segment_selection(mouse, keys, user_input, splines, pygame):
    previous_input = user_input.previous_input
    if mouse.left_click and not previous_input.mouse.left_click:
        look_for_segment(mouse.pos, splines)
    elif mouse.left_click and previous_input.mouse.left_click:
        drag_segment(mouse.pos, splines)

def spline_selection(mouse, keys, user_input, splines, pygame):
    previous_input = user_input.previous_input
    if mouse.left_click and not previous_input.mouse.left_click:
        look_for_spline(mouse.pos, splines)
    elif mouse.left_click and previous_input.mouse.left_click:
        drag_spline(mouse.pos, splines)

def handle_add(mouse, keys, user_input, splines, pygame): 
    previous_input = user_input.previous_input
    # Check for click start
    if mouse.left_click and not previous_input.mouse.left_click:
        look_for_point(mouse.pos, splines, "end", user_input)
        add_segment(splines,user_input, mouse.pos)
    elif mouse.left_click and previous_input.mouse.left_click:
        drag_point(mouse.pos, splines, type, user_input)

def switch_on_selection_mode(mouse, keys, user_input, splines, pygame):
    if user_input.selection_mode == SelectionMode.control_points:
        point_selection(mouse, keys, user_input, splines, "control", pygame)
    if user_input.selection_mode == SelectionMode.end_points:
        point_selection(mouse, keys, user_input, splines, "end", pygame)
    if user_input.selection_mode == SelectionMode.segment:
        segment_selection(mouse, keys, user_input, splines, pygame)
    if user_input.selection_mode == SelectionMode.spline:
        spline_selection(mouse, keys, user_input, splines, pygame)

def handle_delete(mouse, keys, user_input, splines, pygame):
    a = 0

def switch_on_edit_mode(mouse, keys,  user_input, splines, pygame):
    if user_input.edit_mode == EditMode.Add:
       handle_add(mouse, keys, user_input, splines, pygame)
    elif user_input.edit_mode == EditMode.Select:
        switch_on_selection_mode(mouse, keys, user_input, splines, pygame)
    elif user_input.edit_mode == EditMode.Delete:
        handle_delete(mouse, keys, user_input, splines, pygame) 

def set_selection_mode(mouse, keys, user_input, pygame):
    if user_input.edit_mode == EditMode.Add:
        return
    if keys.released == pygame.K_q:
        user_input.selection_mode = SelectionMode.control_points
    if keys.released == pygame.K_w:
        user_input.selection_mode = SelectionMode.end_points
    if keys.released == pygame.K_e:
        user_input.selection_mode = SelectionMode.segment
    if keys.released == pygame.K_r:
        user_input.selection_mode = SelectionMode.spline

def set_edit_mode(mouse, keys, user_input, pygame):
    if keys.released == pygame.K_a:
        user_input.edit_mode = EditMode.Add
        user_input.selection_mode = SelectionMode.end_points
    if keys.released == pygame.K_s:
        user_input.edit_mode = EditMode.Select
    if keys.released == pygame.K_d:
        user_input.edit_mode = EditMode.Delete

def branch_input(mouse, keys, user_input, splines, pygame):
    switch_on_edit_mode(mouse, keys, user_input, splines, pygame)
    set_selection_mode(mouse, keys, user_input, pygame)
    set_edit_mode(mouse, keys, user_input, pygame)

def check_hot_key_toggle(window, keys, pygame):
    if keys.released == pygame.K_h:
        if window.hot_keys:
            window.hot_keys = False
        else:
            window.hot_keys = True

def snap_spline_start_to_ends(splines):
    for spline in splines:
        for i in range(len(spline.segments) - 1):
            if not i + 1 < len(spline.segments):
                return
            if spline.segments[i + 1].selected_end:
                spline.segments[i].end_point = spline.segments[i + 1].start_point
            else:
                spline.segments[i + 1].start_point = spline.segments[i].end_point

def find_opposite_point(point_1, origin, point_2, math):
    x_1, y_1 = point_1[0], point_1[1]
    origin_x, origin_y = origin[0], origin[1]
    x_2, y_2 = point_2[0], point_2[1]

    # Calculate the vector components from origin to point_1
    vec_x = x_1 - origin_x
    vec_y = y_1 - origin_y

    # Calculate the angle of the vector
    angle = math.atan2(vec_y, vec_x)

    # Calculate the coordinates of the second point using the opposite angle
    x_3 = origin_x + math.cos(angle + math.pi) * math.sqrt(vec_x**2 + vec_y**2)
    y_3 = origin_y + math.sin(angle + math.pi) * math.sqrt(vec_x**2 + vec_y**2)

    return [x_3, y_3]

def snap_control_to_opposing_angles(splines, math):
    for spline in splines:
        for i in range(len(spline.segments) - 1):
            if not i + 1 < len(spline.segments):
                return
            if spline.segments[i + 1].selected_end:
                spline.segments[i].end_control_point = find_opposite_point(
                    spline.segments[i + 1].start_control_point, 
                    spline.segments[i + 1].start_point, 
                    spline.segments[i].end_control_point,
                    math)
            else:
                spline.segments[i + 1].start_control_point = find_opposite_point(
                    spline.segments[i].end_control_point, 
                    spline.segments[i].end_point,
                    spline.segments[i + 1].start_control_point, 
                    math)

def handle_user_input(pygame, user_input, window, splines, math):
    mouse = parse_mouse(user_input)
    keys = parse_keyboard(user_input)
    check_hot_key_toggle(window, keys, pygame)
    branch_input(mouse, keys, user_input, splines, pygame)
    snap_spline_start_to_ends(splines)
    snap_control_to_opposing_angles(splines, math)
    user_input.previous_input.mouse = mouse
    user_input.previous_input.keys = keys

def parse_mouse(user_input):
    mouse = InputObject()
    mouse.pos = user_input.current_input.get("cursor position")
    mouse.left_click = user_input.current_input.get("cursor click")[0]
    mouse.middle_click = user_input.current_input.get("cursor click")[1]
    mouse.right_click = user_input.current_input.get("cursor click")[2]
    return mouse

def parse_keyboard(user_input):
    active_key = InputObject
    active_key.pressed = user_input.current_input.get("key pressed")
    active_key.released = user_input.current_input.get("key released")
    return active_key

def main():
    a = 0

if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: handle_user_input"
    )
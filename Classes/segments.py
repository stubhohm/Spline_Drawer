from Constants.CONSTANTS import *
from Calculations.Bezier_curve import bezier_point

class Segment:
    def __init__(self,
            start_point = [0,0],
            start_control_point = [0,0],
            end_point = [0,0],
            end_control_point = [0,0],
            segment_color = WHITE,
            segment_thickness = INIT_LINE_THICKNESS,
            start_control_point_color = INIT_START_CONTROL_POINT_COLOR,
            start_control_point_size = INIT_POINT_SIZE,
            end_control_point_color = INIT_END_CONTROL_POINT_COLOR,
            end_control_point_size = INIT_POINT_SIZE,
            start_control_point_line_color = INIT_CONTROL_LINE_COLOR,
            start_control_point_line_thickness = INIT_LINE_THICKNESS,
            end_control_point_line_color= INIT_CONTROL_LINE_COLOR,
            end_control_point_line_thickness = INIT_LINE_THICKNESS,
            segment_steps = INIT_SEGMENT_STEPS,
            selected_end = False
            ):
        self.start_point = start_point
        self.end_point = end_point
        self.start_control_point = start_control_point
        self.end_control_point = end_control_point
        self.segment_color = segment_color
        self.segment_thickness = segment_thickness
        self.start_control_point_color = start_control_point_color
        self.start_control_point_size = start_control_point_size
        self.end_control_point_color = end_control_point_color
        self.end_control_point_size = end_control_point_size 
        self.start_control_point_line_color = start_control_point_line_color
        self.start_control_point_line_thickness = start_control_point_line_thickness
        self.end_control_point_line_color = end_control_point_line_color
        self.end_control_point_line_thickness = end_control_point_line_thickness
        self.segment_steps = segment_steps
        self.selected_end = selected_end

    def draw_segment(self, pygame, display):
        i = 0
        # Draw curve
        while i < 1:
            x, y = bezier_point(self, i)
            pygame.draw.circle(display, self.segment_color,(x,y),self.segment_thickness)
            i += 1 / self.segment_steps
        # Start and end control point lines
        pygame.draw.line(display, self.start_control_point_line_color, self.start_point, self.start_control_point, self.start_control_point_line_thickness)
        pygame.draw.line(display, self.end_control_point_line_color, self.end_point, self.end_control_point, self.end_control_point_line_thickness)
        # Start and end control points
        pygame.draw.circle(display, self.start_control_point_color, self.start_control_point, self.start_control_point_size)
        pygame.draw.circle(display, self.end_control_point_color, self.end_control_point, self.end_control_point_size)
        

def main():
    print('segment class')

if __name__ == '__main__':
    main()
    print(
        'this main only runs if this file is ran, not if another program executes it: segment class'
    )
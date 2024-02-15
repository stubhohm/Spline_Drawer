from Constants.CONSTANTS import *
from Classes.segments import Segment

class Spline:
    def __init__(self,
            spline_point_color = INIT_POINT_COLOR,
            spline_point_size = INIT_POINT_SIZE,
            line_color = INIT_LINE_COLOR,
            line_thickness = INIT_LINE_THICKNESS,
            segments = [],
            selected = False
            ):
        spline_point_color = spline_point_color
        spline_point_size = spline_point_size
        line_color = line_color
        line_thickness = line_thickness
        self.segments = segments
        self.selected = selected

    # Adding Segmetns
    def add_segment(self, start_point, end_point):
        segment = Segment
        
            
def main():
    print('spline class')

if __name__ == '__main__':
    main()
    print(
        'this main only runs if this file is ran, not if another program executes it: spline class'
    )
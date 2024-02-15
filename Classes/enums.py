from enum import Enum

class SelectionMode(Enum):
    control_points = 1
    end_points = 2
    segment = 3
    spline = 4

class EditMode(Enum):
    Add = 1
    Select = 2
    Delete = 3
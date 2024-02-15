class UserInput:
    def __init__(self,
                 edit_mode,
                 selection_mode,
                 selected_element,
                 print_mode, 
                 current_input = None,
                 previous_input = None):
        self.previous_input = previous_input
        self.current_input = current_input
        self.edit_mode = edit_mode
        self.print_mode = print_mode
        self.selection_mode = selection_mode
        self.selected_element = selected_element
import enum
class GuiEventType(enum.Enum):
    def MovePacman():
        pass
    def MoveGhost():
        pass
    def ChangePacmanDirection():
        pass
    def ChangeGhostDirection():
        pass

class GuiEvent():

    gui_type = GuiEventType()
    extra_properties = {"", object}

    def __init__(self, gui_type):
        self.gui_type = gui_type


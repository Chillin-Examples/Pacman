# -*- coding: utf-8 -*-

# python imports
import enum


# TODO: some other events are left
class GuiEventType(enum.Enum):
    
    MovePacman = 0
    MoveGhost = 1
    ChangePacmanDirection = 2
    ChangeGhostDirection = 3

class GuiEvent(object):

    gui_type = GuiEventType()
    extra_properties = {"": object}

    def __init__(self, gui_type):
        self.gui_type = gui_type

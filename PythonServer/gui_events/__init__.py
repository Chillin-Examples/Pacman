# -*- coding: utf-8 -*-

# python imports
from enum import Enum


# TODO: some other events are left
class GuiEventType(Enum):    
    MovePacman = 0
    MoveGhost = 1
    ChangePacmanDirection = 2
    ChangeGhostDirection = 3


class GuiEvent(object):

    def __init__(self, type, previous_pos, new_pos, direction):
        self.type = type
        self.extra_properties = {"previous_pos":previous_pos, "new_pos":new_pos, "direction": direction}

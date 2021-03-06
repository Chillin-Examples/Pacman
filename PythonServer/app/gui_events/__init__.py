# -*- coding: utf-8 -*-

# python imports
from enum import Enum


class GuiEventType(Enum):    
    MovePacman = 0
    MoveGhost = 1
    ChangePacmanDirection = 2
    ChangeGhostDirection = 3
    EatFood = 4
    KillPacman = 5
    EatSuperFood = 6
    EndGiantForm = 7
    UpdateGiantFormStatus = 8
    KillGhost = 9


class GuiEvent(object):

    def __init__(self, type, **kwargs):
        self.type = type
        self.payload = kwargs

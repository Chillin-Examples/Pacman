# -*- coding: utf-8 -*-

# project imports
from ks.commands import ECommandDirection, ChangePacmanDirection, ChangeGhostDirection
from ks.models import World, ECell
from gui_events import GuiEvent, GuiEventType


def apply_command(self, side_name, command):

    if command.name() == ChangePacmanDirection.name():
        x = self.pacman.x
        y = self.pacman.y
        pacman_position = (x,y)
        self.pacman.direction = command.direction
        return GuiEvent(GuiEventType.ChangePacmanDirection, pos=pacman_position, direction=self.pacman.direction.name)

World.apply_command = apply_command

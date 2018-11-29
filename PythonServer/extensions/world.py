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
        return GuiEvent(GuiEventType.ChangePacmanDirection, pacman_position, pacman_position, self.pacman.direction.name)

    # if command.name() == ChangeGhostDirection.name():
    #     self.ghosts[command.id].direction = command.direction


World.apply_command = apply_command

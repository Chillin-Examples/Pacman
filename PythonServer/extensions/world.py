# -*- coding: utf-8 -*-

# project imports
from ks.commands import ECommandDirection, ChangePacmanDirection, ChangeGhostDirection
from ks.models import World, ECell
from gui_events import GuiEvent, GuiEventType


def apply_command(self, side_name, command):

    if command.name() == ChangePacmanDirection.name():
        # if self._can_change_direction(command)
        self.pacman.change_direction(command)
        return [GuiEvent(GuiEventType.ChangePacmanDirection, direction=self.pacman.direction)]

    elif command.name() == ChangeGhostDirection.name():
        self.ghosts[command.id].change_direction(command)
        return [GuiEvent(GuiEventType.ChangeGhostDirection, id=command.id, direction=self.ghosts[command.id].direction)]


# def _can_change_direction(self, command):
#     print (command.name())

World.apply_command = apply_command
# World._can_change_direction = _can_change_direction

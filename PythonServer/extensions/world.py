# -*- coding: utf-8 -*-

# project imports
from ks.commands import ECommandDirection, ChangePacmanDirection, ChangeGhostDirection
from ks.models import World, ECell
from gui_events import GuiEvent, GuiEventType


def apply_command(self, side_name, command):

    if command.name() == ChangePacmanDirection.name():
        x = self.pacman.x
        y = self.pacman.y
        pacman_position = (x, y)
        new_position = self._calculate_new_pos(command.direction.name, pacman_position)

        if self._can_change_direction(new_position):
            self.pacman.change_direction(command)
            return [GuiEvent(GuiEventType.ChangePacmanDirection, direction=self.pacman.direction)]
        else:
            return []

    elif command.name() == ChangeGhostDirection.name():
        x = self.ghosts[command.id].x
        y = self.ghosts[command.id].y
        ghost_position = (x, y)
        new_position = self._calculate_new_pos(command.direction.name, ghost_position)

        if self._can_change_direction(new_position):
            self.ghosts[command.id].change_direction(command)
            return [GuiEvent(GuiEventType.ChangeGhostDirection, id=command.id, direction=self.ghosts[command.id].direction)]
        else:
            return []


def _calculate_new_pos(self, direction, pre_pos):

    if direction == ECommandDirection.Right.name:
        return (pre_pos[0]+1, pre_pos[1])

    elif direction == ECommandDirection.Left.name:
        return (pre_pos[0]-1, pre_pos[1])

    elif direction == ECommandDirection.Up.name:
        return (pre_pos[0], pre_pos[1]-1)

    elif direction == ECommandDirection.Down.name:
        return (pre_pos[0], pre_pos[1]+1)


def _can_change_direction(self, position):
    return self.board[(position[1])][(position[0])] != ECell.Wall


World.apply_command = apply_command
World._can_change_direction = _can_change_direction
World._calculate_new_pos = _calculate_new_pos

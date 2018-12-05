# -*- coding: utf-8 -*-

# project imports
from ks.commands import ECommandDirection, ChangePacmanDirection, ChangeGhostDirection
from ks.models import World, ECell, EDirection
from gui_events import GuiEvent, GuiEventType


def apply_command(self, side_name, command):
    
    if command.name() == ChangePacmanDirection.name():

        pacman_position = self._get_position("Pacman", None)
        new_position = (self._convert_dir_to_pos[command.direction.name][0]+pacman_position[0],
                         self._convert_dir_to_pos[command.direction.name][1]+pacman_position[1])

        if self._pacman_can_change_direction(new_position):
            self.pacman.change_direction(command)
            return [GuiEvent(GuiEventType.ChangePacmanDirection, direction=self.pacman.direction)]
        else:
            return []

    elif command.name() == ChangeGhostDirection.name():

        ghost_position = self._get_position("Ghost", command.id)
        new_positions = (self._convert_dir_to_pos[command.direction.name][0]+ghost_position[0],
                         self._convert_dir_to_pos[command.direction.name][1]+ghost_position[1])

        if self._ghost_can_change_direction(new_position,ghost_position, command):
            self.ghosts[command.id].change_direction(command)
            return [GuiEvent(GuiEventType.ChangeGhostDirection, id=command.id, direction=self.ghosts[command.id].direction)]
        else:
            return []


def _pacman_can_change_direction(self, position):
    return self.board[(position[1])][(position[0])] != ECell.Wall


def _ghost_can_change_direction(self, new_position, ghost_position, command):

    self._calculate_forbidden_direction = {
        EDirection.Up.name: EDirection.Down.name,
        EDirection.Down.name: EDirection.Up.name,
        EDirection.Right.name: EDirection.Left.name,
        EDirection.Left.name: EDirection.Right.name
    }

    if self.board[(new_position[1])][(new_position[0])] == ECell.Wall:
        print("its a wall")
        return False

    forbidden_direction = self._calculate_forbidden_direction[command.direction.name]
    if self.ghosts[command.id].direction.name != forbidden_direction:
        print("legal")
        return True
    else:
        print("forbidden direction")
        if self._check_dead_end(ghost_position, command.direction.name):
            print("its a dead-end")
            return True
        else:
            print("forbidden but you have other choices")
            return False


def _check_dead_end(self, ghost_position, dir_to_go):
    
    self._convert_dir_to_pos = {
        EDirection.Up.name:(0, -1),
        EDirection.Down.name: (0, +1),
        EDirection.Right.name: (+1, 0),
        EDirection.Left.name: (-1, 0)
    }

    exception = self._convert_dir_to_pos[dir_to_go]
    cells_around = [(-1, 0),(1, 0), (0, 1), (0, -1)]
    cells_around.remove(exception)
    # check if there is a dead end
    for i in cells_around:
        if self.board[(ghost_position[1]+i[1])][(ghost_position[0]+i[0])] != ECell.Wall:
            return False
    return True


def _get_position(self, side_name, id):

    if side_name == "Pacman":
        return (self.pacman.x, self.pacman.y)

    elif side_name == "Ghost":
        return (self.ghosts[id].x, self.ghosts[id].y)


World.apply_command = apply_command
World._pacman_can_change_direction = _pacman_can_change_direction
World._ghost_can_change_direction = _ghost_can_change_direction
World._check_dead_end = _check_dead_end
World._get_position = _get_position

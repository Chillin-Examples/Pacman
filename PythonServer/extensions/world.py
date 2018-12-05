# -*- coding: utf-8 -*-

# project imports
from ks.commands import ECommandDirection, ChangePacmanDirection, ChangeGhostDirection
from ks.models import World, ECell, EDirection
from gui_events import GuiEvent, GuiEventType


def apply_command(self, side_name, command):
    
    if command.name() == ChangePacmanDirection.name():
        x = self.pacman.x
        y = self.pacman.y
        pacman_position = (x, y)
        new_position = self._calculate_new_pos(command.direction.name, pacman_position)

        if self._pacman_can_change_direction(new_position):
            self.pacman.change_direction(command)
            return [GuiEvent(GuiEventType.ChangePacmanDirection, direction=self.pacman.direction)]
        else:
            return []

    elif command.name() == ChangeGhostDirection.name():
        x = self.ghosts[command.id].x
        y = self.ghosts[command.id].y
        ghost_position = ((x, y))
        new_position = self._calculate_new_pos(command.direction.name, ghost_position)

        if self._ghost_can_change_direction(new_position,ghost_position, command):
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


def _pacman_can_change_direction(self, position):
    return self.board[(position[1])][(position[0])] != ECell.Wall


def _ghost_can_change_direction(self, position,ghost_position, command):

    if self.board[(position[1])][(position[0])] == ECell.Wall:
        print("its a wall")
        return False

    forbidden_direction = self._calculate_forbidden_direction(command.direction.name)
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


def _convert_dir_to_pos(self,direction):

    if direction == EDirection.Up.name:
        return(0, -1)
    elif direction == EDirection.Down.name:
        return(0, +1)
    elif direction == EDirection.Right.name:
        return(+1, 0)
    elif direction == EDirection.Left.name:
        return(-1, 0)


def _check_dead_end(self, ghost_position, dir_to_go):

    exception = self._convert_dir_to_pos(dir_to_go)
    cells_around = [(-1, 0),(1, 0), (0, 1), (0, -1)]
    cells_around.remove(exception)

    for i in cells_around:
        if self.board[(ghost_position[1]+i[1])][(ghost_position[0]+i[0])] != ECell.Wall:
            return False
    return True


# Can be a dictionary also
def _calculate_forbidden_direction(self, direction):

    if direction == EDirection.Up.name:
        return EDirection.Down.name
    elif direction == EDirection.Down.name:
        return EDirection.Up.name
    elif direction == EDirection.Right.name:
        return EDirection.Left.name
    elif direction == EDirection.Left.name:
        return EDirection.Right.name


World.apply_command = apply_command
World._pacman_can_change_direction = _pacman_can_change_direction
World._calculate_new_pos = _calculate_new_pos
World._ghost_can_change_direction = _ghost_can_change_direction
World._calculate_forbidden_direction = _calculate_forbidden_direction
World._convert_dir_to_pos = _convert_dir_to_pos
World._check_dead_end = _check_dead_end

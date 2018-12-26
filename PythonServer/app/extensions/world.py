# -*- coding: utf-8 -*-

# project imports
from ..ks.commands import ChangePacmanDirection, ChangeGhostDirection
from ..ks.models import World, ECell, EDirection
from ..gui_events import GuiEvent, GuiEventType


def apply_command(self, side_name, command):

    if command.name() == ChangePacmanDirection.name():

        pacman_position = self._get_position("Pacman", None)
        new_position = self._get_new_position(pacman_position, command.direction.name)

        if self._pacman_can_change_direction(new_position):
            self.pacman.change_direction(self, command)
            return [GuiEvent(GuiEventType.ChangePacmanDirection, direction=self.pacman.direction)]
        else:
            return []

    elif command.name() == ChangeGhostDirection.name():

        ghost_position = self._get_position("Ghost", command.id)
        new_position = self._get_new_position(ghost_position, command.direction.name)

        if self._ghost_can_change_direction(new_position, ghost_position, command):
            self.ghosts[command.id].change_direction(self, command)
            return [GuiEvent(GuiEventType.ChangeGhostDirection, id=command.id, direction=self.ghosts[command.id].direction)]
        else:
            return []


def _pacman_can_change_direction(self, position):
    return self.board[(position[1])][(position[0])] != ECell.Wall


def _ghost_can_change_direction(self, new_position, current_position, command):

    if self.board[(new_position[1])][(new_position[0])] == ECell.Wall:
        # It's a wall
        return False

    forbidden_direction = self._calculate_forbidden_direction[command.direction.name]
    if self.ghosts[command.id].direction.name != forbidden_direction:
        # Legal
        return True
    else:
        # Forbidden direction
        if self._check_dead_end(current_position, command.direction.name):
            # It's a dead-end
            return True
        else:
            # Forbidden but you have other choices
            return False


def _check_dead_end(self, ghost_position, dir_to_go):

    exception = self._convert_dir_to_pos[dir_to_go]
    cells_around = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    cells_around.remove(exception)
    # check if there is a dead end
    for i in cells_around:
        if self.board[(ghost_position[1]+i[1])][(ghost_position[0]+i[0])] != ECell.Wall:
            return False
    return True


def _get_new_position(self, position, direction):
    return(
        self._convert_dir_to_pos[direction][0] + position[0],
        self._convert_dir_to_pos[direction][1] + position[1]
    )


def _get_position(self, side_name, id):
    if side_name == "Pacman":
        return (self.pacman.x, self.pacman.y)
    elif side_name == "Ghost":
        return (self.ghosts[id].x, self.ghosts[id].y)


def recover_agents(self, is_ghost_dead):
    gui_events = []

    # Pacman reset
    self.pacman.x = self.pacman.init_x
    self.pacman.y = self.pacman.init_y
    self.pacman.direction = self.pacman.init_direction
    gui_events.append(GuiEvent(GuiEventType.ChangePacmanDirection, direction=self.pacman.direction))
    gui_events.append(GuiEvent(GuiEventType.MovePacman, new_pos=self.pacman.get_position()))

    # Ghosts reset
    for ghost in self.ghosts:
        gui_events.extend(ghost.recover_ghost(ghost.id, self, is_ghost_dead))

    # Update health
    gui_events.append(GuiEvent(GuiEventType.UpdateHealth))
    self._is_pacman_dead = False
    return gui_events


_convert_dir_to_pos = {
        EDirection.Up.name: (0, -1),
        EDirection.Down.name: (0, +1),
        EDirection.Right.name: (+1, 0),
        EDirection.Left.name: (-1, 0)
    }

_calculate_forbidden_direction = {
        EDirection.Up.name: EDirection.Down.name,
        EDirection.Down.name: EDirection.Up.name,
        EDirection.Right.name: EDirection.Left.name,
        EDirection.Left.name: EDirection.Right.name
    }


World.apply_command = apply_command
World._pacman_can_change_direction = _pacman_can_change_direction
World._ghost_can_change_direction = _ghost_can_change_direction
World._check_dead_end = _check_dead_end
World._get_position = _get_position
World._get_new_position = _get_new_position
World._convert_dir_to_pos = _convert_dir_to_pos
World._calculate_forbidden_direction = _calculate_forbidden_direction
World.recover_agents = recover_agents

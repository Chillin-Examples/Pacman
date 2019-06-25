# -*- coding: utf-8 -*-

# project imports
from ..ks.models import EDirection, World
from ..ks.commands import ChangePacmanDirection, ChangeGhostDirection
from ..gui_events import GuiEvent, GuiEventType


def apply_command(self, side_name, command):
    if command.name() == ChangePacmanDirection.name():
        command_direction = EDirection(command.direction.value)
        if self.pacman.can_change_direction(self, command_direction):
            self.pacman.change_direction(self, command_direction)
            return [GuiEvent(GuiEventType.ChangePacmanDirection, direction=self.pacman.direction)]

    if command.name() == ChangeGhostDirection.name():
        command_direction = EDirection(command.direction.value)
        if self.ghosts[command.id].can_change_direction(self, command_direction):
            self.ghosts[command.id].change_direction(self, command_direction)
            return [GuiEvent(GuiEventType.ChangeGhostDirection, id=command.id, direction=self.ghosts[command.id].direction)]

    return []


def on_pacman_dead(self):
    gui_events = []

    # It must be before recovers
    gui_events.append(GuiEvent(GuiEventType.KillPacman))

    # Recover Pacman
    gui_events.extend(self.pacman.recover(self))

    # Recover Ghosts
    for ghost in self.ghosts:
        gui_events.extend(ghost.recover(self))

    return gui_events


def check_hit(self):
    hit_ghosts_id = []

    for ghost in self.ghosts:
        # Check same cell
        if self.ghosts[ghost.id].position == self.pacman.position:
            hit_ghosts_id.append(ghost.id)

        # Check moving toward each other
        elif self._check_toward_move(ghost) and self._check_adjacency(ghost):
            hit_ghosts_id.append(ghost.id)

    return hit_ghosts_id


def _check_toward_move(self, ghost):
    if ghost.direction == self.pacman.direction.opponent():
        ghost_dir = ghost.direction
        ghost_pos = ghost.position
        pacman_pos = self.pacman.position
        if ghost_dir == EDirection.Up and ghost_pos.y < pacman_pos.y:
            return True
        if ghost_dir == EDirection.Down and ghost_pos.y > pacman_pos.y:
            return True
        if ghost_dir == EDirection.Right and ghost_pos.x > pacman_pos.x:
            return True
        if ghost_dir == EDirection.Left and ghost_pos.x < pacman_pos.x:
            return True
    return False


def _check_adjacency(self, ghost):
    ghost_pos = ghost.position
    pacman_pos = self.pacman.position
    if ghost_pos.x == pacman_pos.x and (ghost_pos.y == pacman_pos.y+1 or ghost_pos.y == pacman_pos.y-1):
        return True
    if ghost_pos.y == pacman_pos.y and (ghost_pos.x == pacman_pos.x+1 or ghost_pos.x == pacman_pos.x-1):
        return True
    return False


World.apply_command = apply_command
World.on_pacman_dead = on_pacman_dead
World.check_hit = check_hit
World._check_toward_move = _check_toward_move
World._check_adjacency = _check_adjacency

# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Ghost, ECell
from ..extensions.agent import get_position, calculate_new_position, can_move
from ..gui_events import GuiEvent, GuiEventType


def change_direction(self, world, command):
    self.direction = command.direction


def move(self,world, ghost):

    gui_events = []
    new_position = ghost.calculate_new_position()

    if ghost.can_move(world, new_position) and not ghost.is_dead:
        ghost.x = new_position[0]
        ghost.y = new_position[1]
        if not ghost.is_dead:
            gui_events.append(GuiEvent(GuiEventType.MoveGhost, new_pos=new_position, id=ghost.id))

    return gui_events


def recover_ghost(self, ghost_id, world):
    world.ghosts[ghost_id].x = world.ghosts[ghost_id].init_x
    world.ghosts[ghost_id].y = world.ghosts[ghost_id].init_y
    world.ghosts[ghost_id].direction = world.ghosts[ghost_id].init_direction
    world.ghosts[ghost_id].is_dead = False

    return [
        GuiEvent(GuiEventType.ChangeGhostDirection, id=ghost_id, direction=world.ghosts[ghost_id].direction),
        GuiEvent(GuiEventType.MoveGhost, new_pos=(world.ghosts[ghost_id].x, world.ghosts[ghost_id].y), id=ghost_id)
    ]


def kill_pacman(self, world):
    world.scores["Ghost"] += world.constants.pacman_death_score
    world.pacman.health -= 1


def can_change_direction(self, new_position, current_position, command, world):

    if world.board[(new_position[1])][(new_position[0])] == ECell.Wall:
        # It's a wall
        return False

    forbidden_direction = world._calculate_forbidden_direction[command.direction.name]
    if world.ghosts[command.id].direction.name != forbidden_direction:
        # Legal
        return True
    else:
        # Forbidden direction
        if world._check_dead_end(current_position, command.direction.name):
            # It's a dead-end
            return True
        else:
            # Forbidden but you have other choices
            return False


Ghost.change_direction = change_direction
Ghost.get_position = get_position
Ghost.calculate_new_position = calculate_new_position
Ghost.can_move = can_move
Ghost.move = move
Ghost.recover_ghost = recover_ghost
Ghost.kill_pacman = kill_pacman
Ghost.can_change_direction = can_change_direction

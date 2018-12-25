# -*- coding: utf-8 -*-

# project imports
from ks.models import Ghost
from extensions.agent import get_position, calculate_new_position, can_move
from gui_events import GuiEvent, GuiEventType


def change_direction(self, world, command):
    self.direction = command.direction


def move(self,world, ghost, is_ghost_dead):

    gui_events = []

   
    new_position = ghost.calculate_new_position()

    if ghost.can_move(world, new_position) and not is_ghost_dead[ghost.id]:
        ghost.x = new_position[0]
        ghost.y = new_position[1]
        if not is_ghost_dead[ghost.id]:
            gui_events.append(GuiEvent(GuiEventType.MoveGhost, new_pos=new_position, id=ghost.id))

    return gui_events


def recover_ghost(self, ghost_id, world, is_ghost_dead):
    world.ghosts[ghost_id].x = world.ghosts[ghost_id].init_x
    world.ghosts[ghost_id].y = world.ghosts[ghost_id].init_y
    world.ghosts[ghost_id].direction = world.ghosts[ghost_id].init_direction
    is_ghost_dead[ghost_id] = False
    return [
        GuiEvent(GuiEventType.ChangeGhostDirection, id=ghost_id, direction=world.ghosts[ghost_id].direction),
        GuiEvent(GuiEventType.MoveGhost, new_pos=(world.ghosts[ghost_id].x, world.ghosts[ghost_id].y), id=ghost_id)
    ]
# def set_ghosts_status(self, ghost_id):
#     self.is_dead = {ghost_id: False}

def kill_pacman(self, world):
    world.scores["Ghost"] += world.constants.pacman_death_score
    world.pacman.health -= 1


Ghost.change_direction = change_direction
Ghost.get_position = get_position
Ghost.calculate_new_position = calculate_new_position
Ghost.can_move = can_move
Ghost.move = move
Ghost.recover_ghost = recover_ghost
Ghost.kill_pacman = kill_pacman
# Ghost.set_ghosts_status = set_ghosts_status
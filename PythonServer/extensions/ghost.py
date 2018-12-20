# -*- coding: utf-8 -*-

# project imports
from ks.models import Ghost
from extensions.agent import get_position, calculate_new_position, can_move
from gui_events import GuiEvent, GuiEventType


def change_direction(self, world, command):
    self.direction = command.direction


def move(self,world, ghost):

    gui_events = []

   
    new_position = ghost.calculate_new_position()

    if ghost.can_move(world, new_position) and not ghost.is_dead[ghost.id]:
        ghost.x = new_position[0]
        ghost.y = new_position[1]
        if not self.is_dead[ghost.id]:
            gui_events.append(GuiEvent(GuiEventType.MoveGhost, new_pos=new_position, id=ghost.id))

    return gui_events


def set_ghosts_status(self, ghost_id):
    self.is_dead = {ghost_id: False}


Ghost.change_direction = change_direction
Ghost.get_position = get_position
Ghost.calculate_new_position = calculate_new_position
Ghost.can_move = can_move
Ghost.move = move
Ghost.set_ghosts_status = set_ghosts_status
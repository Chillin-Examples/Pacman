# -*- coding: utf-8 -*-

# project imports
from ks.models import Ghost
from extensions.agent import get_position, calculate_new_position, can_move


def change_direction(self, world, command):
    self.direction = command.direction


Ghost.change_direction = change_direction
Ghost.get_position = get_position
Ghost.calculate_new_position = calculate_new_position
Ghost.can_move = can_move

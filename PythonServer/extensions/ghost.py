# -*- coding: utf-8 -*-

# project imports
from ks.models import Ghost
from extensions.agent import get_position


def change_direction(self, world, command):
    self.direction = command.direction


Ghost.change_direction = change_direction
Ghost.get_position = get_position

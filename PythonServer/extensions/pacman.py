# -*- coding: utf-8 -*-

# project imports
from ks.models import Pacman
from extensions.agent import get_position


def change_direction(self, world, command):
    self.direction = command.direction


Pacman.change_direction = change_direction
Pacman.get_position = get_position

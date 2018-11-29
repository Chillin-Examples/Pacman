# -*- coding: utf-8 -*-

# project imports
from ks.models import Pacman


def change_direction(self, world, command):
    return True


Pacman.change_direction = change_direction

# -*- coding: utf-8 -*-

# project imports
from ks.models import Pacman


def change_direction(self, command):
    self.direction = command.direction


Pacman.change_direction = change_direction

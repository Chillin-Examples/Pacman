# -*- coding: utf-8 -*-

# project imports
from ks.models import Ghost


def change_direction(self, command):
    self.direction = command.direction

Ghost.change_direction = change_direction

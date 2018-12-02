# -*- coding: utf-8 -*-

# project imports
from ks.models import Ghost


def change_direction(self, world, command):
    return True


Ghost.change_direction = change_direction

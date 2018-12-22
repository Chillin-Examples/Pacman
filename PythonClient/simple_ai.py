# -*- coding: utf-8 -*-

# python imports
import random

# project imports
from ks.commands import ECommandDirection,ChangeGhostDirection,ChangePacmanDirection


ai = None

MOVE_DIR_UP = ECommandDirection.Up
MOVE_DIR_RIGHT = ECommandDirection.Right
MOVE_DIR_DOWN = ECommandDirection.Down
MOVE_DIR_LEFT = ECommandDirection.Left

def initialize(width, height, my_score, other_side,
               board, pacman, ghosts, constants,
               my_side, current_cycle, cycle_duration):
    pass


def decide(width, height, my_score, other_side,
           board, pacman, ghosts, constants,
           my_side, current_cycle, cycle_duration):

    if my_side == 'Pacman':
        direction = random.choice([
            MOVE_DIR_UP,
            MOVE_DIR_RIGHT,
            MOVE_DIR_DOWN,
            MOVE_DIR_LEFT
        ])
        ai.send_command(ChangePacmanDirection(direction=direction))

    if my_side == 'Ghost':
        direction = random.choice([
            MOVE_DIR_UP,
            MOVE_DIR_RIGHT,
            MOVE_DIR_DOWN,
            MOVE_DIR_LEFT
        ])
        ai.send_command(ChangeGhostDirection(direction=direction, id=0))
        ai.send_command(ChangeGhostDirection(direction=direction, id=1))

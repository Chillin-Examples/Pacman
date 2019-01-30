# -*- coding: utf-8 -*-

# python imports
import random

# project imports
from ks.commands import ECommandDirection, ChangeGhostDirection, ChangePacmanDirection
from ks.models import ECell, EDirection


ai = None

CELL_EMPTY = ECell.Empty
CELL_FOOD = ECell.Food
CELL_SUPERFOOD = ECell.SuperFood
CELL_WALL = ECell.Wall

DIR_UP = EDirection.Up
DIR_RIGHT = EDirection.Right
DIR_DOWN = EDirection.Down
DIR_LEFT = EDirection.Left


def initialize(width, height, my_score, other_score,
               board, pacman, ghosts, constants,
               my_side, other_side, current_cycle, cycle_duration):

    pass


def decide(width, height, my_score, other_score,
           board, pacman, ghosts, constants,
           my_side, other_side, current_cycle, cycle_duration):

    if my_side == 'Pacman':
        change_pacman_direction(random.choice([
            DIR_UP,
            DIR_RIGHT,
            DIR_DOWN,
            DIR_LEFT
        ]))

    elif my_side == 'Ghost':
        for ghost in ghosts:
            change_ghost_direction(ghost.id, random.choice([
                        DIR_UP,
                        DIR_RIGHT,
                        DIR_DOWN,
                        DIR_LEFT
                    ]))


def change_pacman_direction(dir):
    ai.send_command(ChangePacmanDirection(direction=dir))


def change_ghost_direction(id, dir):
    ai.send_command(ChangeGhostDirection(id=id, direction=dir))

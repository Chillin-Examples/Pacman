# -*- coding: utf-8 -*-

# project imports
from ks.models import Pacman, ECell
from extensions.agent import get_position, calculate_new_position


def change_direction(self, world, command):
    self.direction = command.direction


def eat_food(self, world):

     # Add score to pacman
    world.scores["Pacman"] += world.constants.food_score
    # Change Food to Empty
    world.board[self.y][self.x] = ECell.Empty
    # Decrease the number of foods
    world.num_of_foods -= 1


def eat_super_food(self, world):

    # Add score to pacman
    world.scores["Pacman"] += world.constants.super_food_score
    # Change Food to Empty
    world.board[self.y][self.x] = ECell.Empty
    # Decrease the number of super foods
    world.num_of_super_foods -= 1


Pacman.change_direction = change_direction
Pacman.get_position = get_position
Pacman.calculate_new_position = calculate_new_position
Pacman.eat_food = eat_food
Pacman.eat_super_food = eat_super_food

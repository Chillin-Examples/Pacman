# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Agent, ECell


def get_new_position(self, new_direction=None):
    new_direction = new_direction or self.direction
    return self.position.dir_to_pos(new_direction) + self.position


def change_direction(self, world, direction):
    self.direction = direction


def recover(self, world):
    self.position = self._init_position
    self.direction = self._init_direction


def can_change_direction(self, world, new_direction):
    new_direction = new_direction
    new_position = self.get_new_position(new_direction)
    return world.board[new_position.y][new_position.x] != ECell.Wall


def can_move(self, world, position):
    return world.board[position.y][position.x] != ECell.Wall


Agent.get_new_position = get_new_position
Agent.change_direction = change_direction
Agent.recover = recover
Agent.can_change_direction = can_change_direction
Agent.can_move = can_move

# -*- coding: utf-8 -*-

# python imports
import json

# project imports
from ks.models import World, Pacman, Ghost, Constants, ECell, EDirection


class MapHandler:

    def __init__(self, sides):
        self._sides = sides


    def create_board(self, height, width, board, new_board):        
        for y in range(height):
                for x in range(width):
                    if board[y][x] == 'w':
                        new_board[y][x] = ECell.Wall
                    elif board[y][x] == 'e':
                        new_board[y][x] = ECell.Empty
        return new_board


    def load_map(self, config):
        map_config = json.loads(open((config['map']), "r").read())
        board = map_config['board']
        world = World()
        world.width = len(board[0])
        world.height = len(board)
        # board initialization
        world.board = [[ECell.Empty for _ in range(world.width)] for _ in range(world.height)]
        world.board = self.create_board(world.height, world.width, board, world.board)
        # self.world.scores = {side: 0 for side in self.sides}
        return world

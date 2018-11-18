# -*- coding: utf-8 -*-

# python imports
import json

# project imports
from ks.models import World, Pacman, Ghost, Constants, ECell, EDirection


class MapHandler:

    def __init__(self, sides):
        self._sides = sides


    def  _fill_board(self, world, map_board):
        world.board = [[ECell.Empty for _ in range(world.width)] for _ in range(world.height)]   
        
        for y in range(world.height):
                for x in range(world.width):
                    if map_board[y][x] == 'w':
                        world.board[y][x] = ECell.Wall
                    elif map_board[y][x] == 'e':
                        world.board[y][x] = ECell.Empty


    def load_map(self, config):
        map_config = json.loads(open((config['map']), "r").read())
        board = map_config['board']
        world = World()
        world.width = len(board[0])
        world.height = len(board)
        # board initialization
        world.board = self._fill_board(world, board)
        # self.world.scores = {side: 0 for side in self.sides}
        return world

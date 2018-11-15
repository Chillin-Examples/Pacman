# -*- coding: utf-8 -*-

# python imports
import json

# project imports
from ks.models import World, Pacman, Ghost, Constants, ECell, EDirection


class MapHandler ():
    _sides = []

    def __init__(self, sides):
        self._sides = sides

    def create_board(self, height, width, board, new):
        
        for y in range(height):
                for x in range(width):
                    if board[y][x] == 'w': # Tree
                        print("www")
                        new[y][x] = ECell.Wall
                    elif board[y][x] == 'e': # Box
                        new[y][x] = ECell.Empty
        
        return new
    def load_map(self, config):

        map_config = json.loads(open((config['map']), "r").read())
        board = map_config['board']
        world = World()
        world.width = len(board[0])
        world.height = len(board)
        # self.world.scores = {side: 0 for side in self.sides}
        # create_board(world.height, world.width, world.board)
        
    # world is an instance of World 
        return world, board

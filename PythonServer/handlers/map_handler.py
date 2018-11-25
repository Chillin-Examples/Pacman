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
                    elif map_board[y][x] == 'f':
                        world.board[y][x] = ECell.Food
                    elif map_board[y][x] == 's':
                        world.board[y][x] = ECell.SuperFood


    def load_map(self, config):
        map_config = json.loads(open((config['map']), "r").read())
        board = map_config['board']
        constants_config = map_config['constants']
        players_config = map_config['players']
        world = World()
        world.width = len(board[0])
        world.height = len(board)
        # board initialization
        self._fill_board(world, board)
        # self._fill_constants(world, constants_config)
        # self._fill_players(world, players_config)
        # self.world.scores = {side: 0 for side in self.sides}
        return world

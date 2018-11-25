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


    def _fill_constants(self, world, constants_config):

        world.constants.food_score = constants_config["food_score"]
        world.constants.super_food_score = constants_config["super_food_score"]
        world.constants.ghost_death_score = constants_config["ghost_death_score"]
        world.constants.pacman_death_score = constants_config["pacman_death_score"]
        world.constants.pacman_max_health = constants_config["pacman_max_health"]
        world.constants.pacman_giant_form_duration = constants_config["pacman_giant_form_duration"]
        world.constants.max_cycles = constants_config["max_cycles"]


    def _fill_players(self, world, players_config):

        # pacman
        pacman_config = players_config["pacman"]
        pacman = Pacman()
        pacman.id = 1
        pacman.position = Position(x=pacman_config["position"][0], y=pacman_config["position"][1])
        pacman.direction = pacman_config["direction"]
        pacman.health = 1
        pacman.giant_form_remaining_time = 0
        world.pacman = pacman

        # ghosts
        world.ghosts = []
        ghost_id = 1
        for ghost_config in player_config["ghosts"]:
            new_ghost = Ghost()
            new_ghost.id = ghost_id
            new_ghost.position = Position(x=ghost_config['position'][0], y=ghost_config['position'][1])
            new_ghost.direction = ghost_config["direction"]
            world.ghosts.append(new_ghost)
            ghost_id += 1


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
        self._fill_constants(world, constants_config)
        self._fill_players(world, players_config)
        # self.world.scores = {side: 0 for side in self.sides}
        return world

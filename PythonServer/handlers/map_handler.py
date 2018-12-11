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
        world.constants = Constants()
        world.constants.food_score = constants_config["food_score"]
        world.constants.super_food_score = constants_config["super_food_score"]
        world.constants.ghost_death_score = constants_config["ghost_death_score"]
        world.constants.pacman_death_score = constants_config["pacman_death_score"]
        world.constants.pacman_giant_form_duration = constants_config["pacman_giant_form_duration"]
        world.constants.max_cycles = constants_config["max_cycles"]


    def _fill_players(self, world, players_config):

        # pacman
        pacman_config = players_config["pacman"]
        pacman = Pacman()
        pacman.x = pacman_config["position"][0]
        pacman.y = pacman_config["position"][1]
        pacman.direction = EDirection[pacman_config["direction"]]
        pacman.init_x = pacman_config["position"][0]
        pacman.init_y = pacman_config["position"][1]
        pacman.ini = 2
        pacman.init_direction = EDirection[pacman_config["direction"]]
        pacman.health = pacman_config["health"]
        pacman.giant_form_remaining_time = 0
        world.pacman = pacman

        # ghosts
        world.ghosts = []
        for ghost_id, ghost_config in enumerate(players_config["ghosts"]):
            new_ghost = Ghost()
            new_ghost.id = ghost_id
            new_ghost.x = ghost_config["position"][0]
            new_ghost.y = ghost_config["position"][1]
            new_ghost.direction = EDirection[ghost_config["direction"]]
            new_ghost.init_x = ghost_config["position"][0]
            new_ghost.init_y = ghost_config["position"][1]
            new_ghost.init_direction = EDirection[ghost_config["direction"]]
            world.ghosts.append(new_ghost)


    def load_map(self, map_path, config, canvas):

        with open((map_path), "r") as map_file:
            map_config = json.loads(map_file.read())
        board = map_config['board']
        constants_config = map_config['constants']
        players_config = map_config['players']

        world = World()
        world.width = len(board[0])
        world.height = len(board)

        # Initialize scores
        world.scores = {side: 0 for side in self._sides}
        # board initialization
        self._fill_board(world, board)
        self._fill_constants(world, constants_config)
        self._fill_players(world, players_config)
        self._init_statuses(world, config, canvas)

        return world

    def _init_statuses(self, world, config, canvas):

        self.statuses = {
                'start_x': canvas.width - config['statuses_width'],
                'end_x': canvas.width,
                'mid_x': canvas.width - (config['statuses_width'] // 2),

                'cycle': None,
                'title_font_size': 55 * config['statuses_width'] // 1000,
                'logo_width': config['cell_size'] * config['statuses_width'] // 1000,

                'players': {side: {} for side in self._sides}
            }

        self.statuses['start_x_Pacman'] = self.statuses['start_x']
        self.statuses['mid_x_Pacman'] = (self.statuses['start_x'] + self.statuses['mid_x']) // 2
        self.statuses['start_x_Ghost'] = self.statuses['mid_x']
        self.statuses['mid_x_Ghost'] = (self.statuses['mid_x'] + self.statuses['end_x']) // 2
        self.statuses['cell_size'] = (self.statuses['mid_x'] - self.statuses['start_x'] - 30) // (world.pacman.health +  3)
        self.statuses['font_size'] = self.statuses['cell_size'] + 5
        self.statuses['start_y'] = 5 * (self.statuses['title_font_size'] + 10) + self.statuses['logo_width'] + 10
        self.statuses['step_y'] = self.statuses['cell_size'] + 20
        self.statuses['calc_y'] = lambda id: self.statuses['start_y'] + self.statuses['step_y'] * id
           
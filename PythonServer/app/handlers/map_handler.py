# -*- coding: utf-8 -*-

# python imports
import json

# project imports
from ..ks.models import ECell, Position, EDirection, Pacman, Ghost, Constants, World


class MapHandler:

    def __init__(self, sides):
        self._sides = sides


    def  _fill_board(self, world, char_board):
        world.board = [[ECell.Empty for _ in range(world.width)] for _ in range(world.height)]

        for y in range(world.height):
            for x in range(world.width):
                if char_board[y][x] == 'w':  # Wall
                    world.board[y][x] = ECell.Wall
                elif char_board[y][x] == 'e':  # Empty
                    world.board[y][x] = ECell.Empty
                elif char_board[y][x] == 'f':  # Food
                    world.board[y][x] = ECell.Food
                elif char_board[y][x] == 's':  # SuperFood
                    world.board[y][x] = ECell.SuperFood


    def _fill_constants(self, world, constants_config):
        world.constants = Constants(
            food_score = constants_config['food_score'],
            super_food_score = constants_config['super_food_score'],
            ghost_death_score = constants_config['ghost_death_score'],
            pacman_death_score = constants_config['pacman_death_score'],
            pacman_giant_form_duration = constants_config['pacman_giant_form_duration'],
            max_cycles = constants_config['max_cycles']
        )


    def _fill_agents(self, world, agents_config):
        # Pacman
        pacman_config = agents_config['pacman']
        pacman = Pacman(
            position = Position(pacman_config['position'][0], pacman_config['position'][1]),
            direction = EDirection[pacman_config['direction']],
            health = pacman_config['health'],
            giant_form_remaining_time = 0
        )
        pacman._init_position = Position(pacman_config['position'][0], pacman_config['position'][1])
        pacman._init_direction = EDirection[pacman_config['direction']]
        pacman.is_giant_form = False
        pacman.foods_count = len([cell for row in world.board for cell in row if cell in [ECell.Food, ECell.SuperFood]])
        world.pacman = pacman

        # Ghosts
        world.ghosts = []
        for ghost_id, ghost_config in enumerate(agents_config['ghosts']):
            ghost = Ghost(
                id = ghost_id,
                position = Position(ghost_config['position'][0], ghost_config['position'][1]),
                direction = EDirection[ghost_config['direction']]
            )
            ghost._init_position = Position(ghost_config['position'][0], ghost_config['position'][1])
            ghost._init_direction = EDirection[ghost_config['direction']]
            world.ghosts.append(ghost)


    def load_map(self, config):
        with open((config['map_path']), 'r') as map_file:
            map_config = json.loads(map_file.read())

        char_board = map_config['board']
        constants_config = map_config['constants']
        agents_config = map_config['agents']

        world = World(width=len(char_board[0]), height=len(char_board))

        # Initialize scores
        world.scores = {side: 0 for side in self._sides}

        # Initialize board
        self._fill_board(world, char_board)
        self._fill_constants(world, constants_config)
        self._fill_agents(world, agents_config)

        return world

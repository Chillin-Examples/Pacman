# -*- coding: utf-8 -*-

# python imports
import math

# chillin imports
from chillin_server.gui.canvas_elements import ScaleType

# project imports
from ks.models import World, Pacman, Ghost, Constants, ECell, EDirection
from gui_events import GuiEventType


# TODO: Define static variables
class GuiHandler():

    def __init__(self, world, sides, canvas):

        self._world = world
        self._sides = sides
        self._canvas = canvas

    def initialize(self, height, width, board, config):

        self.pacman_angle = {
            EDirection.Up.name:        -90,
            EDirection.Right.name:     0,
            EDirection.Down.name:      90,
            EDirection.Left.name:      180,
        }

        self._config(config)
        self._draw_board(height, width, board)
        self._draw_players(height, width, board)


    def _config(self, config):
        
        self._scale_factor = (self._canvas.width - config['statuses_width']) / (self._world.width * config['cell_size'])
        self._scale_percent = math.ceil(self._scale_factor * 100)
        self._cell_size = math.ceil(config['cell_size'] * self._scale_factor)
        self._font_size = self._cell_size // 2


    def _draw_board(self, height, width, board):

        for y in range(height):
            for x in range(width):
                cell = board[y][x]

                if cell == ECell.Wall and (y == height - 1 or y == 0 or x == width - 1 or x == 0):
                    self._canvas.create_image('RoundWall', x * self._cell_size, y * self._cell_size, scale_type=ScaleType.ScaleToWidth,
                                              scale_value=self._cell_size)

                elif cell == ECell.Wall:
                    self._canvas.create_image('InterWall', x * self._cell_size, y * self._cell_size, scale_type=ScaleType.ScaleToWidth,
                                              scale_value=self._cell_size)

                elif cell == ECell.Empty:
                    self._canvas.create_image('Empty', x * self._cell_size, y * self._cell_size, scale_type=ScaleType.ScaleToWidth,
                                              scale_value=self._cell_size)

                elif cell == ECell.Food:
                    img_ref = self._canvas.create_image('Food', x * self._cell_size, y * self._cell_size, scale_type=ScaleType.ScaleToWidth,
                                              scale_value=self._cell_size)


                elif cell == ECell.SuperFood:
                    self._canvas.create_image('SuperFood', x * self._cell_size, y * self._cell_size, scale_type=ScaleType.ScaleToWidth,
                                              scale_value=self._cell_size)


    def _draw_players(self, height, width, board):

        self._pacman_img_ref = self._canvas.create_image('Pacman', self._world.pacman.x, self._world.pacman.y, center_origin=True,
                                scale_type=ScaleType.ScaleToWidth,
                                scale_value=self._cell_size)


    def update(self, events):

        for event in events:
            if event.type == GuiEventType.MovePacman:
                pacman_dir = self.pacman_angle[event.extra_properties["direction"]]
                self._canvas.edit_image(self._pacman_img_ref, event.extra_properties["new_pos"][0], event.extra_properties["new_pos"][1], angle=pacman_dir)

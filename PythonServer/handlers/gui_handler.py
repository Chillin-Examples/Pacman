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


    def config(self):
        print("gameconfig")
        
        # self.scale_factor = (self.canvas.width - self.config['statuses_width']) / (self.world.width * self.config['cell_size'])
        # self.scale_percent = math.ceil(self.scale_factor * 100)
        # self.cell_size = math.ceil(self.config['cell_size'] * self.scale_factor)
        # self.font_size = self.cell_size // 2


    def draw_board(self, height, width, board):
        print('draw board')

        for y in range(height):
            for x in range(width):
                cell = board[y][x]

                if cell == ECell.Wall and (y == height - 1 or y == 0 or x == width - 1 or x == 0):
                    self._canvas.create_image('RoundWall', x * 150, y * 150, scale_type=ScaleType.ScaleToWidth,
                                              scale_value=150)

                elif cell == ECell.Wall:
                    self._canvas.create_image('InterWall', x * 150, y * 150, scale_type=ScaleType.ScaleToWidth,
                                              scale_value=150)

                elif cell == ECell.Empty:
                    self._canvas.create_image('Empty', x * 150, y * 150, scale_type=ScaleType.ScaleToWidth,
                                              scale_value=150)

                elif cell == ECell.Food:
                    img_ref = self._canvas.create_image('Food', x * 150, y * 150, scale_type=ScaleType.ScaleToWidth,
                                              scale_value=150)


                elif cell == ECell.SuperFood:
                    self._canvas.create_image('SuperFood', x * 150, y * 150, scale_type=ScaleType.ScaleToWidth,
                                              scale_value=150)


    def draw_players(self, height, width, board):
        print('draw players')

        self.pacman_img_ref = self._canvas.create_image('Pacman', self._world.pacman.x, self._world.pacman.y,
                                scale_type=ScaleType.ScaleToWidth,
                                scale_value=150)


    def update(self, events):

        for event in events:
            print(event.type)
            if event.type == GuiEventType.MovePacman:
                self._canvas.edit_image(self.pacman_img_ref, event.extra_properties["new_pos"][0], event.extra_properties["new_pos"][1])

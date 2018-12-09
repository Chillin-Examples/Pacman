# -*- coding: utf-8 -*-

# python imports
from __future__ import division
import math

# chillin imports
from chillin_server.gui.canvas_elements import ScaleType

# project imports
from ks.models import World, Pacman, Ghost, Constants, ECell, EDirection
from ks.commands import ECommandDirection
from gui_events import GuiEventType


class GuiHandler():

    def __init__(self, world, sides, canvas):

        self._world = world
        self._sides = sides
        self._canvas = canvas


    def initialize(self, config):

        self._angle = {
            EDirection.Up.name:    90,
            EDirection.Right.name: 0,
            EDirection.Down.name:  -90,
            EDirection.Left.name:  180,
        }

        self._ghosts_ref = {}
        self._foods_ref = {}

        self._config(config)
        self._draw_board()
        self._draw_players()


    def _config(self, config):

        self._status_size = config['statuses_width']
        self._scale_factor = (self._canvas.width - self._status_size) / (self._world.width * config['cell_size'])
        self._scale_percent = math.ceil(self._scale_factor * 100)
        self._cell_size = math.ceil(config['cell_size'] * self._scale_factor)
        self._font_size = self._cell_size // 2


    def _draw_board(self):

        # Draw background
        self._background_ref = self._canvas.create_image('Empty', 0, 0)
        self._canvas.edit_image(self._background_ref, scale_type=ScaleType.ScaleX, scale_value=self._world.width * self._scale_factor * self._cell_size)
        self._canvas.edit_image(self._background_ref, scale_type=ScaleType.ScaleY, scale_value=self._world.height * self._scale_factor * self._cell_size)

        for y in range(self._world.height):
            for x in range(self._world.width):

                cell = self._world.board[y][x]
                canvas_pos = self._get_canvas_position(x=x, y=y, center_origin=False)

                if cell == ECell.Wall and (y == self._world.height - 1 or y == 0 or x == self._world.width - 1 or x == 0):
                    self._canvas.create_image('RoundWall', canvas_pos["x"], canvas_pos["y"], scale_type=ScaleType.ScaleToWidth,
                                              scale_value=self._cell_size)

                elif cell == ECell.Wall:
                    self._canvas.create_image('InterWall', canvas_pos["x"], canvas_pos["y"], scale_type=ScaleType.ScaleToWidth,
                                              scale_value=self._cell_size)

                elif cell == ECell.Empty:
                    self._canvas.create_image('Empty', canvas_pos["x"], canvas_pos["y"], scale_type=ScaleType.ScaleToWidth,
                                              scale_value=self._cell_size)

                elif cell == ECell.Food:
                    food_img_ref = self._canvas.create_image('Food', canvas_pos["x"], canvas_pos["y"], scale_type=ScaleType.ScaleToWidth,
                                              scale_value=self._cell_size)
                    self._foods_ref[x, y] = food_img_ref

                elif cell == ECell.SuperFood:
                    self._canvas.create_image('SuperFood', canvas_pos["x"], canvas_pos["y"], scale_type=ScaleType.ScaleToWidth,
                                              scale_value=self._cell_size)


    def _draw_players(self):

        # draw pacman
        pacman_angle = self._angle[self._world.pacman.direction.name]
        canvas_pos = self._get_canvas_position(x=self._world.pacman.x, y=self._world.pacman.y)
        self._pacman_img_ref = self._canvas.create_image('Pacman',canvas_pos["x"], canvas_pos["y"], center_origin=True,
                                angle=pacman_angle,
                                scale_type=ScaleType.ScaleToWidth,
                                scale_value=self._cell_size)

        #draw ghosts
        for ghost in self._world.ghosts:
            ghost_angle = self._angle[ghost.direction.name]
            canvas_pos = self._get_canvas_position(x=ghost.x, y=ghost.y)
            ghost_img_ref = self._canvas.create_image('Ghost',canvas_pos["x"], canvas_pos["y"], center_origin=True,
                                        angle=ghost_angle,
                                        scale_type=ScaleType.ScaleToWidth,
                                        scale_value=self._cell_size)
                                        
            self._ghosts_ref[ghost.id] = ghost_img_ref


    def update(self, events):

        for event in events:

            # Move
            if event.type in [GuiEventType.MovePacman, GuiEventType.MoveGhost]:
                ref = self._pacman_img_ref if event.type == GuiEventType.MovePacman else self._ghosts_ref[event.payload["id"]]
                pos = self._get_canvas_position(event.payload["new_pos"][0], event.payload["new_pos"][1])
                self._canvas.edit_image(ref, pos['x'], pos['y'])

            # Change direction
            if event.type in [GuiEventType.ChangePacmanDirection, GuiEventType.ChangeGhostDirection]:
                ref = self._pacman_img_ref if event.type == GuiEventType.ChangePacmanDirection else self._ghosts_ref[event.payload["id"]]
                angle = self._angle[event.payload["direction"].name]
                self._canvas.edit_image(ref, None, None, angle=angle)

            # Remove food
            if event.type == GuiEventType.EatFood:

                food_ref =  self._foods_ref[event.payload["position"][0], event.payload["position"][1]]
                self._canvas.delete_element(food_ref)
            
            # kill-pacman
            if event.type == GuiEventType.DecreaseHealth:
                # Reset pacman position
                ref = self._pacman_img_ref
                pos = self._get_canvas_position(self._world.pacman.init_x, self._world.pacman.init_y)
                self._canvas.edit_image(ref, pos['x'], pos['y'])
                # Reset ghosts position
                for ghost in self._world.ghosts:
                    ref = self._ghosts_ref[ghost.id]
                    pos = self._get_canvas_position(ghost.init_x, ghost.init_y)
                    self._canvas.edit_image(ref, pos['x'], pos['y'])



    def _get_canvas_position(self, x, y, center_origin=True):

        addition = self._cell_size // 2 if center_origin else 0
        return {
            'x': x * self._cell_size + addition,
            'y': y * self._cell_size + addition
        }

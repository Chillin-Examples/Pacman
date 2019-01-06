# -*- coding: utf-8 -*-

# python imports

# chillin imports
from chillin_server.gui.canvas_elements import ScaleType


class GameStatus:

    def __init__(self, config, canvas, sides, world):
        self._config = config
        self._canvas = canvas
        self._sides = sides
        self._world = world


    def initialize(self):
        self._title_font_size = 55 * self._config['statuses_width'] // 1000

        self._start_x = self._canvas.width - self._config['statuses_width']
        self._mid_x = self._canvas.width - (self._config['statuses_width'] // 2)
        self._end_x = self._canvas.width

        self._logo_width = self._config['cell_size'] * self._config['statuses_width'] // 1000

        self._mid_x_Pacman = (self._start_x + self._mid_x) // 2
        self._mid_x_Ghost = (self._mid_x + self._end_x) // 2
        self._start_y = 5 * (self._title_font_size + 10) + self._logo_width + 10


    def draw_statuses(self):
        self._cycle_ref = self._canvas.create_text('Cycle: 0', self._mid_x, self._title_font_size, self._canvas.make_rgba(0, 0, 0, 255), self._title_font_size, center_origin=True)

        self._canvas.create_text('Score', self._mid_x, 2 * (self._title_font_size + 10), self._canvas.make_rgba(0, 0, 0, 255), self._title_font_size, center_origin=True)
        self._scores_Pacman = self._canvas.create_text('0', self._mid_x_Pacman, 2 * (self._title_font_size + 10), self._canvas.make_rgba(0, 0, 255, 255), self._title_font_size, center_origin=True)
        self._scores_Ghost = self._canvas.create_text('0', self._mid_x_Ghost, 2 * (self._title_font_size + 10), self._canvas.make_rgba(255, 0, 0, 255), self._title_font_size, center_origin=True)

        self._canvas.create_image('PacmanLogo', self._mid_x_Pacman, self._start_y - self._logo_width // 2 - 15, scale_type=ScaleType.ScaleToWidth, scale_value=self._logo_width, center_origin=True)
        self._canvas.create_image('GhostLogo', self._mid_x_Ghost, self._start_y - self._logo_width // 2 - 15, scale_type=ScaleType.ScaleToWidth, scale_value=self._logo_width, center_origin=True)
        self._canvas.create_line(self._mid_x, self._start_y - self._logo_width, self._mid_x, self._canvas.height, self._canvas.make_rgba(0, 0, 0, 150), stroke_width=1)

        self._canvas.create_text('Health', self._mid_x_Pacman, self._start_y - self._logo_width // 2 - 15 + 200, self._canvas.make_rgba(0, 0, 255, 255), self._title_font_size, center_origin=True)
        self._health_pacman = self._canvas.create_text(str(self._world.pacman.health), self._mid_x_Pacman, self._start_y - self._logo_width // 2 - 15 + 250, self._canvas.make_rgba(0, 0, 255, 255), self._title_font_size, center_origin=True)


    def update_statuses(self, current_cycle):
        # Cycle
        self._canvas.edit_text(self._cycle_ref, 'Cycle: ' + str(current_cycle))
        # Scores
        self._canvas.edit_text(self._scores_Pacman, text=str(self._world.scores['Pacman']))
        self._canvas.edit_text(self._scores_Ghost, text=str(self._world.scores['Ghost']))


    def update_health(self):
        self._canvas.edit_text(self._health_pacman, str(self._world.pacman.health))

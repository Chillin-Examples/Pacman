# -*- coding: utf-8 -*-

# python imports

# chillin imports
from chillin_server.gui.canvas_elements import ScaleType

# project imports


class GameStatus:

    def __init__(self, config, canvas, sides, world):
        self._config = config
        self._canvas = canvas
        self._sides = sides
        self._world = world
    
    def initialize(self):

        self._statuses = {
                'start_x': self._canvas.width - self._config['statuses_width'],
                'end_x': self._canvas.width,
                'mid_x': self._canvas.width - (self._config['statuses_width'] // 2),

                'cycle': None,
                'title_font_size': 55 * self._config['statuses_width'] // 1000,
                'logo_width': self._config['cell_size'] * self._config['statuses_width'] // 1000,

                'players': {side: {} for side in self._sides}
            }

        self._statuses['start_x_Pacman'] = self._statuses['start_x']
        self._statuses['mid_x_Pacman'] = (self._statuses['start_x'] + self._statuses['mid_x']) // 2
        self._statuses['start_x_Ghost'] = self._statuses['mid_x']
        self._statuses['mid_x_Ghost'] = (self._statuses['mid_x'] + self._statuses['end_x']) // 2
        self._statuses['cell_size'] = (self._statuses['mid_x'] - self._statuses['start_x'] - 30) // (self._world.pacman.health +  3)
        self._statuses['font_size'] = self._statuses['cell_size'] + 5
        self._statuses['start_y'] = 5 * (self._statuses['title_font_size'] + 10) + self._statuses['logo_width'] + 10
        self._statuses['step_y'] = self._statuses['cell_size'] + 20
        self._statuses['calc_y'] = lambda id: self._statuses['start_y'] + self._statuses['step_y'] * id
        self._statuses['health_offset_x'] = self._statuses['font_size'] + 5


    def draw_statuses(self):
        self._statuses['cycle_ref'] = self._canvas.create_text('Cycle: 0', self._statuses['mid_x'], self._statuses['title_font_size'], self._canvas.make_rgba(0, 0, 0, 255), self._statuses['title_font_size'], center_origin=True)

        self._canvas.create_text('Score', self._statuses['mid_x'], 2 * (self._statuses['title_font_size'] + 10), self._canvas.make_rgba(0, 0, 0, 255), self._statuses['title_font_size'], center_origin=True)
        self._statuses['scores_Pacman'] = self._canvas.create_text('0', self._statuses['mid_x_Pacman'], 2 * (self._statuses['title_font_size'] + 10), self._canvas.make_rgba(0, 0, 255, 255), self._statuses['title_font_size'], center_origin=True)
        self._statuses['scores_Ghost'] = self._canvas.create_text('0', self._statuses['mid_x_Ghost'], 2 * (self._statuses['title_font_size'] + 10), self._canvas.make_rgba(255, 0, 0, 255), self._statuses['title_font_size'], center_origin=True)

        self._canvas.create_image('PacmanLogo', self._statuses['mid_x_Pacman'], self._statuses['start_y'] - self._statuses['logo_width'] // 2 - 15, scale_type=ScaleType.ScaleToWidth, scale_value=self._statuses['logo_width'], center_origin=True)
        self._canvas.create_image('GhostLogo', self._statuses['mid_x_Ghost'], self._statuses['start_y'] - self._statuses['logo_width'] // 2 - 15, scale_type=ScaleType.ScaleToWidth, scale_value=self._statuses['logo_width'], center_origin=True)
        self._canvas.create_line(self._statuses['mid_x'], self._statuses['start_y'] - self._statuses['logo_width'], self._statuses['mid_x'], self._canvas.height, self._canvas.make_rgba(0, 0, 0, 150), stroke_width=1)

        self._canvas.create_text('Health', self._statuses['mid_x_Pacman'], self._statuses['start_y'] - self._statuses['logo_width'] // 2 - 15 + 200, self._canvas.make_rgba(0, 0, 255, 255), self._statuses['title_font_size'], center_origin=True)
        self._statuses['health_pacman'] = self._canvas.create_text(str(self._world.pacman.health), self._statuses['mid_x_Pacman'], self._statuses['start_y'] - self._statuses['logo_width'] // 2 - 15 + 250, self._canvas.make_rgba(0, 0, 255, 255), self._statuses['title_font_size'], center_origin=True)


    def update_statuses(self):
        pass

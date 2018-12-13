# -*- coding: utf-8 -*-

# python imports

# chillin imports

# project imports


class GameStatus:

    def __init__(self, config, canvas, sides):
        self._config = config
        self._canvas = canvas
        self._sides = sides
    
    def initialize(self, world):

        self.statuses = {
                'start_x': self._canvas.width - self._config['statuses_width'],
                'end_x': self._canvas.width,
                'mid_x': self._canvas.width - (self._config['statuses_width'] // 2),

                'cycle': None,
                'title_font_size': 55 * self._config['statuses_width'] // 1000,
                'logo_width': self._config['cell_size'] * self._config['statuses_width'] // 1000,

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
        self.statuses['health_offset_x'] = self.statuses['font_size'] + 5


    def draw_statuses(self):
        pass

    def update_statuses(self):
        pass

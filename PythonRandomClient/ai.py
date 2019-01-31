# -*- coding: utf-8 -*-

# chillin imports
from chillin_client import RealtimeAI

# project imports
import simple_ai
from ks.models import World


class AI(RealtimeAI):

    def __init__(self, world):
        super(AI, self).__init__(world)
        simple_ai.ai = self


    def initialize(self):
        print('initialize')

        world = self.world
        simple_ai.initialize(world.width, world.height, world.scores[self.my_side], world.scores[self.other_side],
                             world.board, world.pacman, world.ghosts, world.constants,
                             self.my_side, self.other_side, self.current_cycle, self.cycle_duration)


    def decide(self):
        print('decide')

        world = self.world
        simple_ai.decide(world.width, world.height, world.scores[self.my_side], world.scores[self.other_side],
                             world.board, world.pacman, world.ghosts, world.constants,
                             self.my_side, self.other_side, self.current_cycle, self.cycle_duration)

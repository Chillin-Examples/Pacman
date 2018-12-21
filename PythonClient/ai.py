# -*- coding: utf-8 -*-

# python imports
import random

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
        simple_ai.initialize()


    def decide(self):
        print('decide')

        world = self.world
        simple_ai.decide(self.my_side)
        
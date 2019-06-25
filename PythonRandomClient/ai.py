# -*- coding: utf-8 -*-

# python imports
import random

# chillin imports
from chillin_client import RealtimeAI

# project imports
from ks.models import World, EDirection
from ks.commands import ChangeGhostDirection, ChangePacmanDirection


class AI(RealtimeAI):

    def __init__(self, world):
        super(AI, self).__init__(world)


    def initialize(self):
        print('initialize')


    def decide(self):
        print('decide')

        if self.my_side == 'Pacman':
            self.send_command(ChangePacmanDirection(random.choice(list(EDirection))))
        elif self.my_side == 'Ghost':
            for ghost in self.world.ghosts:
                self.send_command(ChangeGhostDirection(ghost.id, random.choice(list(EDirection))))

# -*- coding: utf-8 -*-

# chillin imports
from chillin_client import RealtimeAI

# project imports
from ks.models import World, Pacman, Ghost, Constants, ECell, EDirection
from ks.commands import ChangePacmanDirection, ChangeGhostDirection, ECommandDirection


class AI(RealtimeAI):

    def __init__(self, world):
        super(AI, self).__init__(world)


    def initialize(self):
        print('initialize')


    def decide(self):
        print('decide')
        self.send_command(ChangePacmanDirection(direction=ECommandDirection.Right))

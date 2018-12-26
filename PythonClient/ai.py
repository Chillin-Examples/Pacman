# -*- coding: utf-8 -*-

# python imports
import random

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
        
        if self.my_side == 'Pacman':
            # self.send_command(ChangePacmanDirection(direction=ECommandDirection.Down))
            direction = random.choice([
                ECommandDirection.Up,
                ECommandDirection.Right,
                ECommandDirection.Down,
                ECommandDirection.Left
            ])
            self.send_command(ChangePacmanDirection(direction=direction))

        if self.my_side == 'Ghost':
            direction = random.choice([
                ECommandDirection.Up,
                ECommandDirection.Right,
                ECommandDirection.Down,
                ECommandDirection.Left
            ])
            self.send_command(ChangeGhostDirection(direction=direction, id=0))
            self.send_command(ChangeGhostDirection(direction=direction, id=1))
            self.send_command(ChangeGhostDirection(direction=direction, id=2))
            # self.send_command(ChangeGhostDirection(direction=ECommandDirection.Up, id=0))
            # self.send_command(ChangeGhostDirection(direction=ECommandDirection.Right, id=1))

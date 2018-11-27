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
        print(self.world.board[1][1])
        # if self.world.board[1][1] == ECell.Empty:
        
        self.send_command(ChangePacmanDirection(direction=EDirection.Right, id))
            # self.world.board[1][1] = ECell.Wall
        
        #     return

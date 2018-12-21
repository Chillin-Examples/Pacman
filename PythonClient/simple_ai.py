# -*- coding: utf-8 -*-

# python imports

# project imports
from ks.commands import ECommandDirection,ChangeGhostDirection,ChangePacmanDirection

ai = None


def initialize():
    pass


def decide(my_side):

    if my_side == 'Pacman':
        print "BBBBBBBBBBBBBBBBBBBBBBB"
        ai.send_command(ChangePacmanDirection(direction=ECommandDirection.Down))
        # direction = random.choice([
        #     ECommandDirection.Up,
        #     ECommandDirection.Right,
        #     ECommandDirection.Down,
        #     ECommandDirection.Left
        # ])
        # self.send_command(ChangePacmanDirection(direction=direction))
    print "CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC"
    if my_side == 'Ghost':
        print "AAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        # direction = random.choice([
        #     ECommandDirection.Up,
        #     ECommandDirection.Right,
        #     ECommandDirection.Down,
        #     ECommandDirection.Left
        # ])
        # self.send_command(ChangeGhostDirection(direction=direction, id=0))
        # self.send_command(ChangeGhostDirection(direction=direction, id=1))
        ai.send_command(ChangeGhostDirection(direction=ECommandDirection.Up, id=0))
        ai.send_command(ChangeGhostDirection(direction=ECommandDirection.Right, id=1))

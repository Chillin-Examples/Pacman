# -*- coding: utf-8 -*-

# python imports
from __future__ import division
import random
import json
import math
from enum import Enum

# chillin imports
from chillin_server import TurnbasedGameHandler
from chillin_server.gui.canvas_elements import ScaleType

# project imports
from ks.models import World, Pacman, Ghost, Constants, ECell, EDirection
from ks.commands import ChangePacmanDirection, ChangeGhostDirection, ECommandDirection
from extensions import *


class GameHandler(TurnbasedGameHandler):

    def on_recv_command(self, side_name, agent_name, command_type, command):
        if None in command.__dict__.values():
            print("None in command: %s - %s" % (side_name, command_type))
            return


    def on_initialize(self):
        print('initialize')
        self.world = World()


    def on_initialize_gui(self):
        print('initialize gui')


    def on_process_cycle(self):
        print('cycle %i' % (self.current_cycle, ))
        if self.world.validate_command(None, None):
            self.world.apply_command(None, None)


    def on_update_clients(self):
        print('update clients')
        self.send_snapshot(self.world)


    def on_update_gui(self):
        print('update gui')
        self.canvas.apply_actions()

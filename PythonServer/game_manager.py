# -*- coding: utf-8 -*-

# python imports
from __future__ import division
import random
import json
import math
from enum import Enum

# chillin imports
from chillin_server import RealtimeGameHandler
from chillin_server.gui.canvas_elements import ScaleType

# project imports
from ks.models import World, Pacman, Ghost, Constants, ECell, EDirection
from ks.commands import ChangePacmanDirection, ChangeGhostDirection, ECommandDirection
from extensions import *
from handlers import gui_handler, logic_handler, map_handler


class GameManager(RealtimeGameHandler):

    def on_recv_command(self, side_name, agent_name, command_type, command):

        if None in command.__dict__.values():
            print("None in command: %s - %s" % (side_name, command_type))
            return
        self._logic_handler.store_command(side_name,command)


    def on_initialize(self):
        print('initialize')

        self._map_handler = map_handler.MapHandler(self.sides)
        world = self._map_handler.load_map(self.config['map'], self.config, self.canvas)
        self._logic_handler = logic_handler.LogicHandler(world, self.sides)
        self._logic_handler.initialize()



    def on_initialize_gui(self):
        print('initialize gui')

        self.gui_handler = gui_handler.GuiHandler(self._logic_handler.get_client_world(), self.sides, self.canvas)
        self.gui_handler.initialize(self.config, self._map_handler.statuses)
        self.canvas.apply_actions()


    def on_process_cycle(self):
        print " "
        print('cycle %i' % (self.current_cycle, ))

        self._gui_events = self._logic_handler.process(self.current_cycle)


    def on_update_clients(self):
        print('update clients')

        self.send_snapshot(self._logic_handler.get_client_world())


    def on_update_gui(self):
        print('update gui')

        self.gui_handler.update(self._gui_events)
        self.canvas.apply_actions()

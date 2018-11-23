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


class GameHandler(RealtimeGameHandler):   

    def on_recv_command(self, side_name, agent_name, command_type, command):
        if None in command.__dict__.values():
            print("None in command: %s - %s" % (side_name, command_type))
            return
        # Store ?
        self.commands[side_name][command.id] = command


    def on_initialize(self):
        print('initialize')
        
        self._map_handler = map_handler.MapHandler(self.sides)
        world = self._map_handler.load_map(self.config)
        self._logic_handler = logic_handler.LogicHandler(world, self.sides)
        # status config


    def on_initialize_gui(self):
        print('initialize gui')
        
        self._gui_handler = gui_handler.GuiHandler(self._logic_handler.world, self.sides, self.canvas)
        self._gui_handler.draw_board(self._logic_handler.world.height, self._logic_handler.world.width , self._logic_handler.world.board)


    def on_process_cycle(self):
        print('cycle %i' % (self.current_cycle, ))
        # self.apply_command(None, None)
        # check endgame
        # end_game_info = self._logic_handler.check_end_game()


    def on_update_clients(self):
        print('update clients')
        self.send_snapshot(self._logic_handler.world)
        # self.send_snapshot(self._logic_handler.world)


    def on_update_gui(self):
        print('update gui')
        # gui_event 
        # self._gui_handler.update(gui_event)
        self.canvas.apply_actions()

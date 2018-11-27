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
        print('command: %s(%i) %s' % (side_name, command.id, command_type))
        store_command(side_name,command)
        # Store ?


    def on_initialize(self):
        print('initialize')
        
        world = map_handler.MapHandler(self.sides).load_map(self.config)
        self.logic_handler = logic_handler.LogicHandler(world, self.sides)
        self.logic_handler.initialize()
        # status config


    def on_initialize_gui(self):
        print('initialize gui')
        
        self.gui_handler = gui_handler.GuiHandler(self.logic_handler.world, self.sides, self.canvas)
        self.gui_handler.draw_board(self.logic_handler.world.height, self.logic_handler.world.width , self.logic_handler.world.board)


    def on_process_cycle(self):
        print('cycle %i' % (self.current_cycle, )) 
        self.logic_handler.process(self.current_cycle)
        # self.logic_handler.world.apply_command(None, None)


    def on_update_clients(self):
        print('update clients')
        self.send_snapshot(self.logic_handler.world)


    def on_update_gui(self):
        print('update gui')
        # self.gui_handler.update(self.logic_handler.process.gui_event_list)
        self.canvas.apply_actions()

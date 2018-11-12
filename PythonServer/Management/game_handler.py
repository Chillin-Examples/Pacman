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
from . import game_handler, gui_handler, logic_handler, map_handler

class GameHandler(TurnbasedGameHandler):
    
    current_process = 0
    _logic_handler = logic_handler.LogicHandler(self.world, self.sides)

    def on_recv_command(self, side_name, agent_name, command_type, command):
        if None in command.__dict__.values():
            print("None in command: %s - %s" % (side_name, command_type))
            return
        # Store ?
        self.commands[side_name][command.id] = command
        
        

    def on_initialize(self):
        print('initialize')

        _map_handler = map_handler.MapHandler(sides)
        self.world = _map_handler.load_map("mappath")
        # create world board
        # self.world = World()
        # status config

    def on_initialize_gui(self):
        print('initialize gui')


    def on_process_cycle(self):
        print('cycle %i' % (self.current_cycle, ))
        
        self.apply_command(None, None)
        
        #check endgame
        end_game_info = {"", {"",{"",{}}}}
        end_game_info = _logic_handler.check_end_game()
        

    def on_update_clients(self):
        print('update clients')
        self.send_snapshot(self.world)


    def on_update_gui(self):
        print('update gui')
        _gui_handler = gui_handler.GuiHandler(self.world, self.sides, self.canvas)
        # gui_event 
        _gui_handler.update(gui_event)
        self.canvas.apply_actions()

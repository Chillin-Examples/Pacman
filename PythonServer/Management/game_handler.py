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
from . import  gui_handler, logic_handler, map_handler
from . import map_handler
class GameHandler(TurnbasedGameHandler):
    
    current_process = 0
    _logic_handler = None
    # _map_handler = map_handler.MapHandler(self.sides)
    # _gui_handler = None
    

    def on_recv_command(self, side_name, agent_name, command_type, command):
        if None in command.__dict__.values():
            print("None in command: %s - %s" % (side_name, command_type))
            return
        # Store ?
        self.commands[side_name][command.id] = command
        

    def on_initialize(self):
        print('initialize')
        
        _map_handler = map_handler.MapHandler(self.sides)

        self.world, board  = _map_handler.load_map(self.config)
        self.world.board = [[ECell.Empty for _ in range(self.world.width)] for _ in range(self.world.height)]

        

        self.world.board = _map_handler.create_board(self.world.height,self.world.width, board, self.world.board)
       
        # print(self.world.board[0][0])
        self.scale_factor = (self.canvas.width - self.config['statuses_width']) / (self.world.width * self.config['cell_size'])
        self.scale_percent = math.ceil(self.scale_factor * 100)
        self.cell_size = math.ceil(self.config['cell_size'] * self.scale_factor)
        self.font_size = self.cell_size // 2

        # self._logic_handler = LogicHandler(world, self.sides)
        # create world board
        # status config

    def on_initialize_gui(self):
        print('initialize gui')
        # self._gui_handler = gui_handler.GuiHandler(self._logic_handler.world, self.sides, self.canvas)
        _gui_handler = gui_handler.GuiHandler(self.world, self.sides, self.canvas)
        _gui_handler.draw_board(self.world.height, self.world.width , self.world.board)

      
    def on_process_cycle(self):
        print('cycle %i' % (self.current_cycle, ))
        
        # self.apply_command(None, None)

        #check endgame
        # end_game_info = self._logic_handler.check_end_game()
        

    def on_update_clients(self):
        print('update clients')
        self.send_snapshot(self.world)
        # self.send_snapshot(self._logic_handler.world)


    def on_update_gui(self):
        print('update gui')
        # gui_event 
        # self._gui_handler.update(gui_event)
        self.canvas.apply_actions()

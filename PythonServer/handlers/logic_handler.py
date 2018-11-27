# -*- coding: utf-8 -*-
from ks.models import Position
from ks.commands import ECommandDirection
# from gui_event import *


class LogicHandler ():

    def __init__ (self, world, sides):
        self._sides = sides
        self.world = world
        # self.gui_event = GuiEvent(0)

    def initialize(self):

        self.move_dirs = {
            ECommandDirection.Up.name: Position(x=0, y=-1),
            ECommandDirection.Right.name: Position(x=1, y=0),
            ECommandDirection.Down.name: Position(x=0, y=1),
            ECommandDirection.Left.name: Position(x=-1, y=0)
        }

        self.commands = {side: {} for side in self._sides}


    def store_command(self, side_name, command):
        # too aply command change directiono seda mizanim ?
        # behtar nis inja age id e command -  bood store nakone?
        # gui event ye list bashe va har seri tahe cycle faghat liste pak she dige ? be last gui event kri nadarim ?
        # move pacman farghsh ba change pacman direction ?
        # az koja mifahme type hamun enum e ?

        self.commands[side_name][command.id] = command
        return commands


    def clear_commands(self):
        for side in self._sides:
            self.commands = {side: {} for side in self._sides}


    def process(self, current_cycle):
        # test code
        
        if self.world.pacman.health == 0:
            return
        
        # pacman Command
        for id in self.commands["Pacman"]:
            command = self.commands["Pacman"][id]
            if command.name() == ChangePacmanDirection.name():
                new_position = Pos(position=pacman.position) + self.move_dirs[command.direction.name]

            if self.world.board[new_position.y][new_position.x] != ECell.Wall:
                # if there was a ghost there
                world.pacman.position = new_position
                
        self.clear_commands()        
        
        
        # self.world.apply_command(None, None)
        # return guievent


    def get_client_world(self, side_name):
        return world


    def check_end_game(self):
        pass
        #should return tuple<string, dict<string,dict<string, duct<string,string>>>

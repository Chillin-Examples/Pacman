# -*- coding: utf-8 -*-
from ks.models import Position
from ks.commands import ECommandDirection
from extensions import world
# from gui_event import *


class LogicHandler ():

    def __init__ (self, world, sides):
        self._sides = sides
        self.world = world
        # for bezan ino
        self._last_cycle_commands = {'Pacman': [], 'Ghost': []}
        # self.gui_event = GuiEvent(0)

    def initialize(self):

        self.move_dirs = {
            ECommandDirection.Up.name: Position(x=0, y=-1),
            ECommandDirection.Right.name: Position(x=1, y=0),
            ECommandDirection.Down.name: Position(x=0, y=1),
            ECommandDirection.Left.name: Position(x=-1, y=0)
        }

        


    def store_command(self, side_name, command):
        # too aply command change directiono seda mizanim ?
        # gui event ye list bashe va har seri tahe cycle faghat liste pak she dige ? be last gui event kri nadarim ?
        
        if command.id < 0 or command.id >= (len(self.world.pacman), len(self.world.ghosts)):
            print('Invalid id in command: %s %i' % (side_name, command.id))
            return
        
        self._last_cycle_commands[side_name] = command
        print('command: %s(%i) %s' % (side_name, command.id, command_type))


    def clear_commands(self):
        for side in self._sides:
            self.commands = {side: {} for side in self._sides}


    def process(self, current_cycle):
        # test code
        # for side_name in self._sides
        #     self.world.apply_command(side_name, command)
        print("processssx   ")
        for i in self._last_cycle_commands["Pacman"]:
            print(i)
            gui_event = self.world.apply_command("Pacman", i)
            print("aaaaaaaaaaaa")
            print(gui_event)
            print("\n")
        # self.clear_commands()        
        # return guievent


    def get_client_world(self, side_name):
        return world


    def check_end_game(self):
        pass
        #should return tuple<string, dict<string,dict<string, duct<string,string>>>

# -*- coding: utf-8 -*-
from ks.commands import ECommandDirection
from extensions import world
from gui_events import *
# from gui_event import *


class LogicHandler ():

    def __init__ (self, world, sides):
        self._sides = sides
        self.world = world
        # for bezan ino
        self._last_cycle_commands = {'Pacman': [], 'Ghost': []}
        # self.gui_event = GuiEvent(0)

    def initialize(self):
        pass
        # self.move_dirs = {
        #     ECommandDirection.Up.name: Position(x=0, y=-1),
        #     ECommandDirection.Right.name: Position(x=1, y=0),
        #     ECommandDirection.Down.name: Position(x=0, y=1),
        #     ECommandDirection.Left.name: Position(x=-1, y=0)
        # }


    def store_command(self, side_name, command):
       
        # if side_name == "Ghost":
        #     if command.id < 0 or command.id >= (len(self.world.pacman), len(self.world.ghosts)):
        #         print('Invalid id in command: %s %i' % (side_name, command.id))
        #         return

        self._last_cycle_commands[side_name] = command
        print(command.__dict__)
        # print('command: %s(%i) %s' % (side_name, command.id, command_type))


    def clear_commands(self):
        for side in self._sides:
            self._last_cycle_commands = {'Pacman': [], 'Ghost': []}


    def process(self, current_cycle):

       
        gui_events_list = []

        # APPLY COMMAND FOR PACMAN AND GHOSTS
        for side in self._sides:
            gui_events_list.append(self.world.apply_command(side, self._last_cycle_commands[side]))

        self._move_objects(gui_events_list)
        self.clear_commands()        
        return gui_events_list
    
    def _move_objects(self,gui_events):

        for gui_event in gui_events:
            if gui_event.type == GuiEventType.MovePacman:
                print("successfully moved")
                self.world.pacman.x = gui_event.extra_properties["new_pos"][0]
                self.world.pacman.y = gui_event.extra_properties["new_pos"][1]


    def check_end_game(self):
        pass
        #should return tuple<string, dict<string,dict<string, duct<string,string>>>

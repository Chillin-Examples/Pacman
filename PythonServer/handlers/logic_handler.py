# -*- coding: utf-8 -*-

class LogicHandler ():

    def __init__ (self, world, sides):
        self._sides = sides
        self.world = world
 
        
    def store_command(self, side_name, command):
        return command


    def clear_commands():
        pass


    def process(self, current_cycle):
        # guievent is a list of GuiEvents-> guievent = Guievent[]
        return guievent


    def get_client_world(self, side_name):
        return world


    def check_end_game(self):
        pass
        #should return tuple<string, dict<string,dict<string, duct<string,string>>>

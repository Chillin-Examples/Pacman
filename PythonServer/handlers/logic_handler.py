# -*- coding: utf-8 -*-

class LogicHandler ():

    def __init__ (self, world, sides):
        self._sides = sides
        self.world = world


    def initialize(self):

        self.move_dirs = {
            ECommandDirection.Up.name: Position(x=0, y=-1),
            ECommandDirection.Right.name: Position(x=1, y=0),
            ECommandDirection.Down.name: Position(x=0, y=1),
            ECommandDirection.Left.name: Position(x=-1, y=0)
        }

        self.commands = {side: {} for side in self._sides}


    def store_command(self, side_name, command):
        self.commands[side_name][command.id] = command
        return command


    def clear_commands():
        pass


    def process(self, current_cycle):
        # test code
        if self.world.pacman.health == 0:
            return

        command = self.commands["pacman"][1]
        if command.name() == ChangePacmanDirection.name():
            new_position = Pos(position=pacman.position) + self.move_dirs[command.direction.name]

            if self.world.board[new_position.y][new_position.x] != ECell.Wall:
                # if there was a ghost there
                world.pacman.position = new_position
        
        # self.world.apply_command(None, None)
        # return guievent


    def get_client_world(self, side_name):
        return world


    def check_end_game(self):
        pass
        #should return tuple<string, dict<string,dict<string, duct<string,string>>>

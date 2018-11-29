# -*- coding: utf-8 -*-
from ks.commands import ECommandDirection
from extensions import world
from gui_events import *
from ks.models import World, ECell


class LogicHandler ():

    def __init__ (self, world, sides):
        self._sides = sides
        self.world = world
        self._last_cycle_commands = {side: {} for side in self._sides}
        

    def initialize(self):
        pass


    def store_command(self, side_name, command):
       
        # if side_name == "Ghost":
        #     if command.id < 0 or command.id >= ( len(self.world.ghosts)):
        #         print('Invalid id in command: %s %i' % (side_name, command.id))
        #         return

        self._last_cycle_commands[side_name][command.id if side_name == 'Ghost' else None] = command
        # print("command on reciev ")
        # if side_name == "Pacman":
        #     print(self._last_cycle_commands[side_name])
        
        # elif side_name == "Ghost":
        #     print(self._last_cycle_commands[side_name][command.id])
        


    def clear_commands(self):

        self._last_cycle_commands = {side: {} for side in self._sides}


    def process(self, current_cycle):
       
        gui_events = []
        gui_events.append(self.world.apply_command("Pacman", self._last_cycle_commands["Pacman"][None]))

        if self._move_objects(self._last_cycle_commands["Pacman"][None])!= None:
            gui_events.append(self._move_objects(self._last_cycle_commands["Pacman"][None]))

        self.clear_commands()
        for f in gui_events:
            print "TOOOOOOOOOOOOOOOOOOOOOOOOOOO CYCLEEEEEEEEEEEEEEEEEE"
            print f.extra_properties["new_pos"][0]
        return gui_events


    def _move_objects(self, command):
        
        x = self.world.pacman.x
        y = self.world.pacman.y
        pacman_position = (x, y)
        new_position = self._calculate_new_pos(command, pacman_position)

        if self._can_move(new_position):
            print("can move")

            self.world.pacman.x = new_position[0]
            self.world.pacman.y = new_position[1]
            return GuiEvent(GuiEventType.MovePacman, pacman_position, new_position, self.world.pacman.direction.name)

        else:
            print("cannot move")
            # okeye ?
            return


    def _calculate_new_pos(self, command, pre_pos):
        
        if command.direction.name == ECommandDirection.Right.name:
            return (pre_pos[0]+1, pre_pos[1])

        elif command.direction.name == ECommandDirection.Left.name:
            return (pre_pos[0]-1, pre_pos[1])

        elif command.direction.name == ECommandDirection.Up.name:
            return (pre_pos[0], pre_pos[1]-1)

        elif command.direction.name == ECommandDirection.Down.name:
            return (pre_pos[0], pre_pos[1]+1)


    def _can_move(self, new_pos):
        # inke hesab kone hatman khoone he baghalesh bashe chi ?
        if self.world.board[(new_pos[1])][(new_pos[0])] == ECell.Wall:
            return False
        
        else:
            return True


    def get_client_world(self):
        return self.world


    def check_end_game(self):
        pass
        #should return tuple<string, dict<string,dict<string, duct<string,string>>>

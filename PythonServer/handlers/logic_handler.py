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

        if side_name == "Ghost":
            if command.id < 0 or command.id >= ( len(self.world.ghosts)):
                print('Invalid id in command: %s %i' % (side_name, command.id))
                return

        self._last_cycle_commands[side_name][command.id if side_name == 'Ghost' else None] = command


    def clear_commands(self):

        self._last_cycle_commands = {side: {} for side in self._sides}


    def process(self, current_cycle):

        gui_events = []

        for side_name in self._sides:
            for command_id in self._last_cycle_commands[side_name]:

                gui_events.extend(self.world.apply_command(side_name, self._last_cycle_commands[side_name][command_id]))
                
        gui_events.extend(self._move_pacman())
        gui_events.extend(self._move_ghosts())

        self.clear_commands()
        return gui_events


    def _move_pacman(self):

        x = self.world.pacman.x
        y = self.world.pacman.y
        pacman_position = (x, y)
        new_position = self._calculate_new_pos(self.world.pacman.direction.name, pacman_position)

        if self._can_move(new_position):
            print("pacman can move")

            self.world.pacman.x = new_position[0]
            self.world.pacman.y = new_position[1]
            return [GuiEvent(GuiEventType.MovePacman, new_pos=new_position)]

        else:
            print("pacman cannot move")
            return []


    def _move_ghosts(self):

        for ghost in self.world.ghosts:
    
            x = ghost.x
            y = ghost.y
            ghost_position = (x, y)
            new_position = self._calculate_new_pos(ghost.direction.name, ghost_position)

            if self._can_move(new_position):
                print("ghost can move")

                ghost.x = new_position[0]
                ghost.y = new_position[1]
                return [GuiEvent(GuiEventType.MoveGhost, new_pos=new_position)]

            else:
                print("ghost cannot move")
                return []


    def _calculate_new_pos(self, direction, pre_pos):
    
        if direction == ECommandDirection.Right.name:
            return (pre_pos[0]+1, pre_pos[1])

        elif direction == ECommandDirection.Left.name:
            return (pre_pos[0]-1, pre_pos[1])

        elif direction == ECommandDirection.Up.name:
            return (pre_pos[0], pre_pos[1]-1)

        elif direction == ECommandDirection.Down.name:
            return (pre_pos[0], pre_pos[1]+1)


    def _can_move(self, position):

        if self.world.board[(position[1])][(position[0])] == ECell.Wall:
            return False

        else:
            return True


    def get_client_world(self):

        return self.world


    def check_end_game(self):
        pass
        #should return tuple<string, dict<string,dict<string, duct<string,string>>>

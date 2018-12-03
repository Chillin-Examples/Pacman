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
        gui_events.extend(self.check_end_game(current_cycle))

        for i in gui_events:
            print(i.__dict__)
        self.clear_commands()
        return gui_events


    def _move_pacman(self):

        gui_events = []
        pacman_position = self._get_position("Pacman", None)
        new_position = self._calculate_new_pos(self.world.pacman.direction.name, pacman_position)

        if self._can_move(new_position):
            print("pacman can move")

            if self._can_be_eaten(new_position):
                print("can be eaten")
                self._eat_food(new_position)
                gui_events.append(GuiEvent(GuiEventType.EatFood, position=new_position))

            self.world.pacman.x = new_position[0]
            self.world.pacman.y = new_position[1]
            gui_events.append(GuiEvent(GuiEventType.MovePacman, new_pos=new_position))
            return gui_events

        else:
            print("pacman cannot move")
            return []


    def _move_ghosts(self):

        gui_events = []

        for ghost in self.world.ghosts:
            ghost_position = self._get_position("Ghost", ghost.id)
            new_position = self._calculate_new_pos(ghost.direction.name, ghost_position)

            if self._can_move(new_position):
                print("ghost can move")
                ghost.x = new_position[0]
                ghost.y = new_position[1]
                gui_events.append(GuiEvent(GuiEventType.MoveGhost, new_pos=new_position, id=ghost.id))

            else:
                print("ghost cannot move")
                gui_events.extend([])

        return gui_events


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
        return self.world.board[(position[1])][(position[0])] != ECell.Wall


    def _can_be_eaten(self, position):
        return self.world.board[(position[1])][(position[0])] == ECell.Food


    def _eat_food(self, position):
        # Add score to pacman
        self.world.scores["Pacman"] += self.world.constants.food_score
        # Change Food to Empty
        self.world.board[(position[1])][(position[0])] == ECell.Empty


    def _get_position(self, side_name, id):

        if side_name == "Pacman":
            return (self.world.pacman.x, self.world.pacman.y)

        elif side_name == "Ghost":
            return (self.world.ghosts[id].x, self.world.ghosts[id].y)


    def get_client_world(self):
        return self.world


    def check_end_game(self, current_cycle):
        gui_events = []
        end_game = False

        if current_cycle >= self.world.constants.max_cycles - 1:
            end_game = True

        # TODO:Check winner
        # Check if ghost can kill pacman
        for ghost in self.world.ghosts:
            end_game = True
            ghost_position = self._get_position("Ghost", ghost.id)

            if ghost_position == self._get_position("Pacman", None):
                print("pacman was eaten by ghost: ",ghost.id)
                self.world.scores["Ghost"] += self.world.constants.pacman_death_score
                gui_events.append(GuiEvent(GuiEventType.KillPacman))

        return gui_events

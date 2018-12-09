# -*- coding: utf-8 -*-
from ks.commands import ECommandDirection
from extensions import world
from gui_events import *
from ks.models import World, ECell, EDirection


class LogicHandler ():

    def __init__ (self, world, sides):

        self._sides = sides
        self.world = world
        self._last_cycle_commands = {side: {} for side in self._sides}


    def initialize(self):

        self._convert_dir_to_pos = {
        EDirection.Up.name:(0, -1),
        EDirection.Down.name: (0, +1),
        EDirection.Right.name: (+1, 0),
        EDirection.Left.name: (-1, 0)
    }


    def store_command(self, side_name, command):

        if side_name == "Ghost":
            if command.id < 0 or command.id >= ( len(self.world.ghosts)):
                print('Invalid id in command: %s %i' % (side_name, command.id))
                return
        if side_name == "Pacman":
            print("pacman command")
            print(command.__dict__)
        self._last_cycle_commands[side_name][command.id if side_name == 'Ghost' else None] = command


    def clear_commands(self):
        self._last_cycle_commands = {side: {} for side in self._sides}


    def process(self, current_cycle):
        print(self.world.pacman.health)
        gui_events = []
        if self._check_hit():
            print("kill")
            return(self._kill_pacman())
            # return [GuiEvent(GuiEventType.MoveGhost, new_pos=(self.world.ghosts[0].x, self.world.ghosts[0].y),id=1)]


        for side_name in self._sides:
            for command_id in self._last_cycle_commands[side_name]:
                gui_events.extend(self.world.apply_command(side_name, self._last_cycle_commands[side_name][command_id]))

        gui_events.extend(self._move_pacman())
        gui_events.extend(self._move_ghosts())

        # EAT FOOD
        pacman_position = self._get_position("Pacman", None)
        if self._can_be_eaten(pacman_position):
            print("can be eaten")
            self._eat_food(pacman_position)
            gui_events.append(GuiEvent(GuiEventType.EatFood, position=(pacman_position)))

        self.clear_commands()
        return gui_events


    def _check_toward_move(self, pacman, ghost):

        self.opponent_direction={
            EDirection.Up.name: EDirection.Down.name,
            EDirection.Down.name: EDirection.Up.name,
            EDirection.Right.name: EDirection.Left.name,
            EDirection.Left.name: EDirection.Right.name
        }
        if ghost.direction.name == self.opponent_direction[pacman.direction.name]:
            if ghost.direction.name == EDirection.Up.name and ghost.y > pacman.y:
                return True
            if ghost.direction.name == EDirection.Down.name and ghost.y < pacman.y:
                return True
            if ghost.direction.name == EDirection.Right.name and ghost.x < pacman.x:
                return True
            if ghost.direction.name == EDirection.Left.name and ghost.x > pacman.x:
                return True


    def _check_hit(self):

        # Check same cell 
        for ghost in self.world.ghosts:
            if self._get_position("Ghost", ghost.id) == self._get_position("Pacman", None):
                return True

        # Check moving toward each other
        for ghost in self.world.ghosts:
            if self._check_toward_move(self.world.pacman, ghost) and self._check_adjacency(ghost):
                return True
            else:
                return False


    def _check_adjacency(self, ghost):
        if ghost.x == self.world.pacman.x and (ghost.y==self.world.pacman.y+1 or ghost.y==self.world.pacman.y-1):
            return True
        elif ghost.y == self.world.pacman.y and (ghost.x==self.world.pacman.x+1 or ghost.x==self.world.pacman.x-1):
            return True
        else:
            return False


    def _move_pacman(self):

        gui_events = []
        pacman_position = self._get_position("Pacman", None)
        new_position = (self._convert_dir_to_pos[self.world.pacman.direction.name][0]+pacman_position[0],
                         self._convert_dir_to_pos[self.world.pacman.direction.name][1]+pacman_position[1])

        if self._can_move(new_position):
            print("pacman can move")

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
            new_position = (self._convert_dir_to_pos[ghost.direction.name][0]+ghost_position[0],
                         self._convert_dir_to_pos[ghost.direction.name][1]+ghost_position[1])

            if self._can_move(new_position):
                print("ghost can move")
                ghost.x = new_position[0]
                ghost.y = new_position[1]
                gui_events.append(GuiEvent(GuiEventType.MoveGhost, new_pos=new_position, id=ghost.id))

            else:
                print("ghost cannot move")

        return gui_events


    def _can_move(self, position):
        return self.world.board[(position[1])][(position[0])] != ECell.Wall


    def _can_be_eaten(self, position):
        return self.world.board[(position[1])][(position[0])] == ECell.Food


    def _eat_food(self, position):
        # Add score to pacman
        self.world.scores["Pacman"] += self.world.constants.food_score
        # Change Food to Empty
        self.world.board[(position[1])][(position[0])] = ECell.Empty


    def _get_position(self, side_name, id):

        if side_name == "Pacman":
            return (self.world.pacman.x, self.world.pacman.y)

        elif side_name == "Ghost":
            return (self.world.ghosts[id].x, self.world.ghosts[id].y)


    def get_client_world(self):
        return self.world


    def _kill_pacman(self):

        self.world.scores["Ghost"] += self.world.constants.pacman_death_score
        self.world.pacman.health -= 1
        return(self._recover_agents())


    def _recover_agents(self):
        gui_events = []

        self.world.pacman.x = self.world.pacman.init_x
        self.world.pacman.y = self.world.pacman.init_y
        self.world.pacman.direction = self.world.pacman.init_direction
        # self._get_position("Pacman", None)
        gui_events.append(GuiEvent(GuiEventType.MovePacman, new_pos=(self.world.pacman.x, self.world.pacman.y)))

        for ghost in self.world.ghosts:
            ghost.x = ghost.init_x
            ghost.y = ghost.init_y
            ghost.direction = ghost.init_direction
            gui_events.append(GuiEvent(GuiEventType.MoveGhost, new_pos=(ghost.x, ghost.y), id=ghost.id))
        gui_events.append(GuiEvent(GuiEventType.DecreaseHealth))
        return gui_events

    def check_end_game(self, current_cycle):
        pass

# -*- coding: utf-8 -*-

# project imports
from ..extensions import world
from ..gui_events import *
from ..ks.models import World, ECell, EDirection


class LogicHandler ():

    def __init__ (self, world, sides):

        self._sides = sides
        self.world = world
        self._last_cycle_commands = {side: {} for side in self._sides}

    def initialize(self):

        self._opponent_direction = {
            EDirection.Up.name: EDirection.Down.name,
            EDirection.Down.name: EDirection.Up.name,
            EDirection.Right.name: EDirection.Left.name,
            EDirection.Left.name: EDirection.Right.name
        }


    def store_command(self, side_name, command):

        if side_name == "Ghost":
            if command.id < 0 or command.id >= (len(self.world.ghosts)):
                print('Invalid id in command: %s %i' % (side_name, command.id))
                return
            self._last_cycle_commands[side_name][command.id] = command

        elif side_name == "Pacman":
            self._last_cycle_commands[side_name][None] = command


    def clear_commands(self):
        self._last_cycle_commands = {side: {} for side in self._sides}


    def process(self, current_cycle):

        gui_events = []

        if self.world.pacman.is_giant_form:
            self.world.pacman.giant_form_remaining_time -= 1
            gui_events.append(GuiEvent(GuiEventType.UpdateGiantFormStatus, remaining=self.world.pacman.giant_form_remaining_time))
            gui_events.extend(self._check_end_giant_form())

        # Change direction
        for side_name in self._sides:
            for command_id in self._last_cycle_commands[side_name]:
                gui_events.extend(self.world.apply_command(side_name, self._last_cycle_commands[side_name][command_id]))

        # Move
        gui_events.extend(self.world.pacman.move(self.world))
        for ghost in self.world.ghosts:
            gui_events.extend(ghost.move(self.world, ghost))

        # Check hits
        is_pacman_dead = False
        hit_ghosts_id = self._check_hit()
        if len(hit_ghosts_id) > 0 and not self.world.pacman.is_giant_form:
            # Kill pacman
            is_pacman_dead = True
            # 0 is chosen in case of hitting more than one ghost
            self.world.ghosts[hit_ghosts_id[0]].kill_pacman(self.world)
            gui_events.extend(self.world.on_pacman_dead())

        elif len(hit_ghosts_id) > 0 and self.world.pacman.is_giant_form:
            # Kill ghosts
            for ghost_id in hit_ghosts_id:
                self.world.pacman.kill_ghost(self.world)
                gui_events.append(GuiEvent(GuiEventType.KillGhost, id=ghost_id))
                gui_events.extend(self.world.ghosts[ghost_id].recover(self.world))

        # Eat food
        if not is_pacman_dead:
            pacman_position = self.world.pacman.get_position()
            # Food
            if self.world.pacman.can_eat_food(self.world, pacman_position):
                gui_events.extend(self.world.pacman.eat_food(self.world))
            # SuperFood
            if self.world.pacman.can_eat_super_food(self.world, pacman_position):
                gui_events.extend(self.world.pacman.eat_super_food(self.world))
                self.world.pacman.giant_form(self.world)

        return gui_events


    def _check_toward_move(self, pacman, ghost):

        if ghost.direction.name == self._opponent_direction[pacman.direction.name]:
            if ghost.direction.name == EDirection.Up.name and ghost.y < pacman.y:
                return True
            if ghost.direction.name == EDirection.Down.name and ghost.y > pacman.y:
                return True
            if ghost.direction.name == EDirection.Right.name and ghost.x > pacman.x:
                return True
            if ghost.direction.name == EDirection.Left.name and ghost.x < pacman.x:
                return True


    def _check_hit(self):
        hit_ghosts_id = []
        for ghost in self.world.ghosts:

            # Check same cell
            if self.world.ghosts[ghost.id].get_position() == self.world.pacman.get_position():
                hit_ghosts_id.append(ghost.id)

            # Check moving toward each other
            elif self._check_toward_move(self.world.pacman, ghost) and self._check_adjacency(ghost):
                hit_ghosts_id.append(ghost.id)

        return hit_ghosts_id


    def _check_adjacency(self, ghost):

        if ghost.x == self.world.pacman.x and (ghost.y == self.world.pacman.y+1 or ghost.y == self.world.pacman.y-1):
            return True

        elif ghost.y == self.world.pacman.y and (ghost.x == self.world.pacman.x+1 or ghost.x == self.world.pacman.x-1):
            return True
        else:
            return False


    def get_client_world(self):
        return self.world


    def _check_end_giant_form(self):
        gui_events = []
        if self.world.pacman.giant_form_remaining_time == 0:
            self.world.pacman.is_giant_form = False
            gui_events.append(GuiEvent(GuiEventType.EndGiantForm))
        return gui_events


    def check_end_game(self, current_cycle):

        end_game = False
        winner = None
        details = None
        
        if current_cycle >= self.world.constants.max_cycles - 1:
            end_game = True

        elif self.world.pacman.health == 0 and not self.world.pacman.is_giant_form:
            end_game = True

        elif self.world.num_of_foods == 0 and self.world.num_of_super_foods == 0 and not self.world.pacman.is_giant_form:
            end_game = True

        if end_game:

            if self.world.scores['Pacman'] > self.world.scores['Ghost']:
                winner = 'Pacman'
            elif self.world.scores['Ghost'] > self.world.scores['Pacman']:
                winner = 'Ghost'
            details = {
                'Scores': {
                    'Pacman': str(self.world.scores['Pacman']),
                    'Ghost': str(self.world.scores['Ghost'])
                    }
                }
        return end_game, winner, details

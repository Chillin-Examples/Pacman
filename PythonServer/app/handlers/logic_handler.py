# -*- coding: utf-8 -*-

# python imports
from copy import deepcopy

# project imports
from ..ks.models import World


class LogicHandler:

    def __init__ (self, world, sides):
        self._sides = sides
        self.world = world


    def initialize(self):
        self._last_cycle_commands = {side: {} for side in self._sides}


    def store_command(self, side_name, command):
        if side_name == 'Ghost':
            if command.id < 0 or command.id >= (len(self.world.ghosts)):
                print("Invalid id in command: %s %i" % (side_name, command.id))
                return
            self._last_cycle_commands[side_name][command.id] = command

        elif side_name == 'Pacman':
            self._last_cycle_commands[side_name][None] = command


    def clear_commands(self):
        self._last_cycle_commands = {side: {} for side in self._sides}


    def process(self, current_cycle):
        gui_events = []

        if self.world.pacman.is_giant_form:
            gui_events.extend(self.world.pacman.update_giant_form(self.world))

        # Change direction
        for side_name in self._sides:
            for command_id in self._last_cycle_commands[side_name]:
                gui_events.extend(self.world.apply_command(side_name, self._last_cycle_commands[side_name][command_id]))

        # Move
        gui_events.extend(self.world.pacman.move(self.world))
        for ghost in self.world.ghosts:
            gui_events.extend(ghost.move(self.world))

        # Check hits
        is_pacman_dead = False
        hit_ghosts_id = self.world.check_hit()
        if len(hit_ghosts_id) > 0 and not self.world.pacman.is_giant_form:
            # Kill pacman
            is_pacman_dead = True
            # 0 is chosen in case of hitting more than one ghost
            self.world.ghosts[hit_ghosts_id[0]].kill_pacman(self.world)
            gui_events.extend(self.world.on_pacman_dead())

        elif len(hit_ghosts_id) > 0 and self.world.pacman.is_giant_form:
            # Kill ghosts
            for ghost_id in hit_ghosts_id:
                gui_events.extend(self.world.pacman.kill_ghost(self.world, ghost_id))

        # Eat food
        if not is_pacman_dead:
            # Food
            if self.world.pacman.can_eat_food(self.world, is_super_food=False):
                gui_events.extend(self.world.pacman.eat_food(self.world, is_super_food=False))
            # SuperFood
            if self.world.pacman.can_eat_food(self.world, is_super_food=True):
                gui_events.extend(self.world.pacman.eat_food(self.world, is_super_food=True))
                self.world.pacman.start_giant_form(self.world)

        return gui_events


    def get_client_world(self, side_name):
        return self.world


    def check_end_game(self, current_cycle):
        end_game = False
        winner = None
        details = None

        if current_cycle >= self.world.constants.max_cycles - 1:
            end_game = True

        elif self.world.pacman.health == 0 and not self.world.pacman.is_giant_form:
            end_game = True

        elif self.world.pacman.foods_count == 0 and not self.world.pacman.is_giant_form:
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

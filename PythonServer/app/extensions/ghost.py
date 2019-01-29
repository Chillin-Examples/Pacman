# -*- coding: utf-8 -*-

# project imports
from ..ks.models import Ghost, ECell
from ..extensions.agent import get_position, calculate_new_position, can_move, recover as recover_agent
from ..gui_events import GuiEvent, GuiEventType


def change_direction(self, world, command):
    self.direction = command.direction


def move(self,world, ghost):

    gui_events = []
    new_position = ghost.calculate_new_position()

    if ghost.can_move(world, new_position):
        ghost.x = new_position[0]
        ghost.y = new_position[1]
        gui_events.append(GuiEvent(GuiEventType.MoveGhost, id=ghost.id, new_pos=new_position))

    return gui_events


def recover(self, world):
    recover_agent(self)

    return [
        GuiEvent(GuiEventType.ChangeGhostDirection, id=self.id, direction=self.direction),
        GuiEvent(GuiEventType.MoveGhost, id=self.id, new_pos=(self.x, self.y))
    ]


def kill_pacman(self, world):
    world.scores["Ghost"] += world.constants.pacman_death_score
    world.pacman.health -= 1


def can_change_direction(self, new_position, current_position, command, world):
    if world.board[(new_position[1])][(new_position[0])] == ECell.Wall:
        # It's a wall
        return False

    forbidden_direction = world._calculate_forbidden_direction[command.direction.name]
    if world.ghosts[command.id].direction.name != forbidden_direction:
        # Legal
        return True
    else:
        # Forbidden direction
        if world._check_dead_end(current_position, command.direction.name):
            # It's a dead-end
            return True
        else:
            # Forbidden but you have other choices
            return False


Ghost.change_direction = change_direction
Ghost.get_position = get_position
Ghost.calculate_new_position = calculate_new_position
Ghost.can_move = can_move
Ghost.move = move
Ghost.recover = recover
Ghost.kill_pacman = kill_pacman
Ghost.can_change_direction = can_change_direction

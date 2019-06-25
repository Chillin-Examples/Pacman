# -*- coding: utf-8 -*-

# project imports
from ..ks.models import ECell, Pacman
from ..gui_events import GuiEvent, GuiEventType


def eat_food(self, world, is_super_food):
    gui_events = []
    world.scores['Pacman'] += world.constants.super_food_score if is_super_food else \
                              world.constants.food_score
    world.board[self.position.y][self.position.x] = ECell.Empty
    self.foods_count -= 1

    gui_events.append(
        GuiEvent(
            GuiEventType.EatSuperFood if is_super_food else GuiEventType.EatFood,
            position = self.position
        )
    )
    return gui_events


def can_eat_food(self, world, is_super_food):
    cell = world.board[self.position.y][self.position.x]
    return (cell == ECell.Food and not is_super_food) or \
           (cell == ECell.SuperFood and is_super_food)


def move(self, world):
    gui_events = []
    new_position = self.get_new_position()
    if self.can_move(world, new_position):
        self.position = new_position
        gui_events.append(GuiEvent(GuiEventType.MovePacman, new_pos=self.position))
    return gui_events


def recover(self, world):
    super(Pacman, self).recover(world)
    return [
        GuiEvent(GuiEventType.ChangePacmanDirection, direction=self.direction),
        GuiEvent(GuiEventType.MovePacman, new_pos=self.position)
    ]


def kill_ghost(self, world, ghost_id):
    gui_events = []
    world.scores['Pacman'] += world.constants.ghost_death_score
    gui_events.append(GuiEvent(GuiEventType.KillGhost, id=ghost_id))
    gui_events.extend(world.ghosts[ghost_id].recover(world))
    return gui_events


def start_giant_form(self, world):
    self.is_giant_form = True
    world.pacman.giant_form_remaining_time = world.constants.pacman_giant_form_duration + 1


def update_giant_form(self, world):
    gui_events = []
    self.giant_form_remaining_time -= 1
    gui_events.append(GuiEvent(GuiEventType.UpdateGiantFormStatus, remaining=self.giant_form_remaining_time))
    if self.giant_form_remaining_time == 0:
        self.is_giant_form = False
        gui_events.append(GuiEvent(GuiEventType.EndGiantForm))
    return gui_events


def can_change_direction(self, world, new_direction):
    return super(Pacman, self).can_change_direction(world, new_direction)


Pacman.eat_food = eat_food
Pacman.can_eat_food = can_eat_food
Pacman.move = move
Pacman.recover = recover
Pacman.kill_ghost = kill_ghost
Pacman.start_giant_form = start_giant_form
Pacman.update_giant_form = update_giant_form
Pacman.can_change_direction = can_change_direction

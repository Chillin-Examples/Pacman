# -*- coding: utf-8 -*-

# python imports

# chillin imports
from chillin_server.gui import scene_actions


class GameStatus:

    def __init__(self, world, scene, eat_delay):
        self._world = world
        self._scene = scene
        self._rm = scene.rm
        self._eat_delay = eat_delay


    def initialize(self):
        self._top_panel_ref = self._rm.new()
        self._health_panel_ref = 'HealthPanel'
        self._health_images_ref = []
        self._cycle_ref = 'CycleText'
        self._pacman_score_ref = 'ScorePanel/PacmanScore'
        self._ghost_score_ref = 'ScorePanel/GhostScore'


    def draw_statuses(self):
        self._scene.add_action(scene_actions.InstantiateBundleAsset(
            ref = self._top_panel_ref,
            asset = scene_actions.Asset(bundle_name='main', asset_name='TopPanel'),
            default_parent = scene_actions.EDefaultParent.RootCanvas
        ))

        # Cycle
        self._set_cycle_text(0)

        # Pacman health
        for i in range(self._world.pacman.health):
            new_ref = self._rm.new()
            self._health_images_ref.append(new_ref)

            self._scene.add_action(scene_actions.InstantiateBundleAsset(
                ref = new_ref,
                asset = scene_actions.Asset(bundle_name='main', asset_name='PacmanImage'),
                parent_ref = self._top_panel_ref,
                parent_child_ref = self._health_panel_ref
            ))


    def update_statuses(self, current_cycle):
        # Cycle
        self._set_cycle_text(current_cycle)

        # Scores
        self._scene.add_action(scene_actions.ChangeText(
            cycle = self._eat_delay,
            ref = self._top_panel_ref,
            child_ref = self._pacman_score_ref,
            text = str(self._world.scores['Pacman'])
        ))

        self._scene.add_action(scene_actions.ChangeText(
            cycle = self._eat_delay,
            ref = self._top_panel_ref,
            child_ref = self._ghost_score_ref,
            text = str(self._world.scores['Ghost'])
        ))

    def _set_cycle_text(self, cycle):
        self._scene.add_action(scene_actions.ChangeText(
            ref = self._top_panel_ref,
            child_ref = self._cycle_ref,
            text = 'Cycle: {:d}/{:d}'.format(cycle, self._world.constants.max_cycles)
        ))

    def decrease_health(self):
        self._scene.add_action(scene_actions.Destroy(
            ref = self._health_images_ref.pop()
        ))

# -*- coding: utf-8 -*-

# python imports
from __future__ import division
import math

# chillin imports
from chillin_server.gui import scene_actions

# project imports
from ks.models import World, Pacman, Ghost, Constants, ECell, EDirection
from ks.commands import ECommandDirection
from gui_events import GuiEventType


class GuiHandler():

    def __init__(self, world, scene):

        self._world = world
        self._scene = scene
        self._rm = scene.rm


    def initialize(self, config):

        self._angle = {
            EDirection.Up.name:    90,
            EDirection.Right.name: 0,
            EDirection.Down.name:  -90,
            EDirection.Left.name:  180,
        }

        self._ghost_eyes_index = {
            EDirection.Up.name:    5,
            EDirection.Right.name: 3,
            EDirection.Down.name:  1,
            EDirection.Left.name:  2,
        }

        self._ghosts_color = [
            scene_actions.Vector4(x=213/255, y=0, z=0, w=1),
            scene_actions.Vector4(x=236/255, y=64/255, z=122/255, w=1),
            scene_actions.Vector4(x=100/255, y=181/255, z=246/255, w=1),
            scene_actions.Vector4(x=244/255, y=81/255, z=30/255, w=1),
        ]

        self._eat_delay = 0.75
        self._ghost_eyes_ref = 'Eyes'

        self._ghosts_ref = {}
        self._foods_ref = {}
        self._super_foods_ref = {}

        self._config(config)
        self._init_camera()
        self._draw_board()
        self._draw_players()

        # Status
        self._game_status = game_status.GameStatus(self._world, self._scene, self._eat_delay)
        self._game_status.initialize()
        self._game_status.draw_statuses()


    def _config(self, config):
        self._cell_size = config['cell_size']
        self._x_offset = -self._world.width / 2.0 * self._cell_size
        self._y_offset = -self._world.height / 2.0 * self._cell_size


    def _init_camera(self):
        self._scene.add_action(scene_actions.ChangeCamera(
            ref = self._rm.get('MainCamera'),
            clear_flag = scene_actions.ECameraClearFlag.SolidColor,
            background_color = scene_actions.Vector4(x=0, y=19/255, z=48/255),
            is_orthographic = True,
            orthographic_size = 9 # TODO: set based on map size
        ))


    def _draw_board(self):
        for y in range(self._world.height):
            for x in range(self._world.width):
                cell = self._world.board[y][x]
                if cell == ECell.Empty: continue

                scene_pos = self._get_scene_position(x=x, y=y)
                z = 5
                reference = self._rm.new()

                # if cell == ECell.Wall and (y == self._world.height - 1 or y == 0 or x == self._world.width - 1 or x == 0):
                #     self._scene.add_action(scene_actions.InstantiateBundleAsset(
                #         ref = reference,
                #         asset = scene_actions.Asset(bundle_name='main', asset_name='Wall')
                #     ))
                #     self._scene.add_action(scene_actions.ChangeSprite(
                #         ref = reference,
                #         sprite_asset = scene_actions.Asset(bundle_name='main', asset_name='Walls', index=0)
                #     ))

                if cell == ECell.Wall:
                    wall_type, wall_angle = self._get_wall_type_angle(x, y)
                    if wall_type == None: continue

                    self._scene.add_action(scene_actions.InstantiateBundleAsset(
                        ref = reference,
                        asset = scene_actions.Asset(bundle_name='main', asset_name='Wall')
                    ))
                    self._scene.add_action(scene_actions.ChangeSprite(
                        ref = reference,
                        sprite_asset = scene_actions.Asset(bundle_name='main', asset_name='Walls', index=wall_type)
                    ))
                    self._scene.add_action(scene_actions.ChangeTransform(
                        ref = reference,
                        rotation = scene_actions.Vector3(z=wall_angle)
                    ))

                elif cell == ECell.Food:
                    self._foods_ref[x, y] = reference
                    self._scene.add_action(scene_actions.InstantiateBundleAsset(
                        ref = reference,
                        asset = scene_actions.Asset(bundle_name='main', asset_name='Food')
                    ))

                elif cell == ECell.SuperFood:
                    self._super_foods_ref[x, y] = reference
                    self._scene.add_action(scene_actions.InstantiateBundleAsset(
                        ref = reference,
                        asset = scene_actions.Asset(bundle_name='main', asset_name='SuperFood')
                    ))

                # Set Position
                self._scene.add_action(scene_actions.ChangeTransform(
                    ref = reference,
                    position = scene_actions.Vector3(x=scene_pos['x'], y=scene_pos['y'], z=z)
                ))


    def _get_wall_type_angle(self, x, y):
        has_top_wall = y != 0 and self._world.board[y - 1][x] == ECell.Wall
        has_right_wall = x != self._world.width - 1 and self._world.board[y][x + 1] == ECell.Wall
        has_bot_wall = y != self._world.height - 1 and self._world.board[y + 1][x] == ECell.Wall
        has_left_wall = x != 0 and self._world.board[y][x - 1] == ECell.Wall

        num_neighbor_walls = int(has_top_wall) + int(has_right_wall) + int(has_bot_wall) + int(has_left_wall)

        wall_type = None
        wall_angle = 0

        if num_neighbor_walls == 1:
            wall_type = 0 # End

            if has_top_wall:
                wall_angle = 180
            elif has_right_wall:
                wall_angle = 90
            elif has_bot_wall:
                wall_angle = 0
            elif has_left_wall:
                wall_angle = -90

        elif num_neighbor_walls == 2:
            if (has_top_wall and has_bot_wall) or (has_left_wall and has_right_wall):
                wall_type = 2 # Straight

                if has_top_wall:
                    wall_angle = 0
                else:
                    wall_angle = 90
            else:
                wall_type = 1 # Corner

                if has_top_wall and has_right_wall:
                    wall_angle = -90
                elif has_right_wall and has_bot_wall:
                    wall_angle = 180
                elif has_bot_wall and has_left_wall:
                    wall_angle = 90
                elif has_left_wall and has_top_wall:
                    wall_angle = 0

        elif num_neighbor_walls == 3:
            wall_type = 3

            if not has_top_wall:
                wall_angle = 90
            elif not has_right_wall:
                wall_angle = 0
            elif not has_bot_wall:
                wall_angle = -90
            elif not has_left_wall:
                wall_angle = 180

        return wall_type, wall_angle


    def _draw_players(self):

        # Draw pacman
        pacman_angle = self._angle[self._world.pacman.direction.name]
        scene_pos = self._get_scene_position(x=self._world.pacman.x, y=self._world.pacman.y)
        self._pacman_ref = self._rm.new()

        self._scene.add_action(scene_actions.InstantiateBundleAsset(
            ref = self._pacman_ref,
            asset = scene_actions.Asset(bundle_name='main', asset_name='Pacman')
        ))
        self._scene.add_action(scene_actions.ChangeTransform(
            ref = self._pacman_ref,
            position = scene_actions.Vector3(x=scene_pos['x'], y=scene_pos['y'], z=0),
            rotation = scene_actions.Vector3(z=pacman_angle)
        ))

        # Draw ghosts
        for ghost in self._world.ghosts:
            scene_pos = self._get_scene_position(x=ghost.x, y=ghost.y)
            self._ghosts_ref[ghost.id] = self._rm.new()
            color = self._ghosts_color[ghost.id % len(self._ghosts_color)]

            self._scene.add_action(scene_actions.InstantiateBundleAsset(
                ref = self._ghosts_ref[ghost.id],
                asset = scene_actions.Asset(bundle_name='main', asset_name='Ghost')
            ))
            self._scene.add_action(scene_actions.ChangeTransform(
                ref = self._ghosts_ref[ghost.id],
                position = scene_actions.Vector3(x=scene_pos['x'], y=scene_pos['y'], z=0),
            ))
            # Change color
            self._scene.add_action(scene_actions.ChangeSprite(
                ref = self._ghosts_ref[ghost.id],
                child_ref = 'Body',
                color = color
            ))
            self._scene.add_action(scene_actions.ChangeSprite(
                ref = self._ghosts_ref[ghost.id],
                child_ref = 'Foots',
                color = color
            ))

            self._set_ghost_eyes(ghost.id, ghost.direction)


    def _set_ghost_eyes(self, ghost_id, direction, is_scared = False):
        ghost_ref = self._ghosts_ref[ghost_id]

        if is_scared:
            self._scene.add_action(scene_actions.ChangeSprite(
                ref = ghost_ref,
                child_ref = self._ghost_eyes_ref,
                sprite_asset = scene_actions.Asset(bundle_name='main', asset_name='GhostParts', index=4)
            ))
        else:
            self._scene.add_action(scene_actions.ChangeSprite(
                ref = ghost_ref,
                child_ref = self._ghost_eyes_ref,
                sprite_asset = scene_actions.Asset(bundle_name='main', asset_name='GhostParts', index=self._ghost_eyes_index[direction.name])
            ))


    def update(self, events):

        self.freeze_mode = False
        for event in events:

            # Move
            if event.type in [GuiEventType.MovePacman, GuiEventType.MoveGhost]:
                ref = self._pacman_ref if event.type == GuiEventType.MovePacman else self._ghosts_ref[event.payload["id"]]
                pos = self._get_scene_position(event.payload["new_pos"][0], event.payload["new_pos"][1])
                self._scene.add_action(scene_actions.ChangeTransform(
                    ref = ref,
                    duration_cycles = 1,
                    position = scene_actions.Vector3(x=pos['x'], y=pos['y'])
                ))

            # Change Pacman direction
            elif event.type == GuiEventType.ChangePacmanDirection:
                angle = self._angle[event.payload["direction"].name]
                self._scene.add_action(scene_actions.ChangeTransform(
                    ref = self._pacman_ref,
                    rotation = scene_actions.Vector3(z=angle)
                ))

            # Change Ghost direction
            elif event.type == GuiEventType.ChangeGhostDirection:
                self._set_ghost_eyes(event.payload["id"], event.payload["direction"])

            # Remove food
            elif event.type == GuiEventType.EatFood:
                self._scene.add_action(scene_actions.Destroy(
                    cycle = self._eat_delay,
                    ref = self._foods_ref[event.payload["position"][0], event.payload["position"][1]]
                ))

            # Remove super food
            if event.type == GuiEventType.EatSuperFood:
                self.freeze_mode = True
                # Remove food
                self._scene.add_action(scene_actions.Destroy(
                    cycle = self._eat_delay,
                    ref = self._super_foods_ref[event.payload["position"][0], event.payload["position"][1]]
                ))

                # Pacman giant form
                self._scene.add_action(scene_actions.ChangeAnimatorState(
                    cycle = self._eat_delay,
                    ref = self._pacman_ref,
                    state_name = 'PacmanSuper'
                ))

            # Go to default mode
            elif event.type == GuiEventType.EndGiantForm:
                self._scene.add_action(scene_actions.ChangeAnimatorState(
                    ref = self._pacman_ref,
                    state_name = 'PacmanNormal'
                ))

            # Status
            elif event.type == GuiEventType.UpdateHealth:
                self._game_status.decrease_health()
            self._game_status.update_statuses(current_cycle)


    def _get_scene_position(self, x, y):

        addition = self._cell_size / 2
        return {
            'x': x * self._cell_size + addition + self._x_offset,
            'y': -(y * self._cell_size + addition + self._y_offset)
        }

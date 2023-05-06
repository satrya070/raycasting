import pygame as pg
import math

from raycasting.settings import *

class RayCasting:
    def __init__(self, game):
        self.game = game

    def ray_cast(self):
        px, py = self.game.player.position
        x_map, y_map = self.game.player.map_position

        ray_angle = self.game.player.angle - HALF_FOV # 30deg

        # for every  ray shot 
        for ray in range(NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # check horizontals intersecting
            y_horz, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 0.000001, -1) # move up y_map if sinus(vertical) pos, else move down
            
            depth_horz = (y_horz - py) / sin_a # get diagonal length distance: (y_horz - player_y) / sin_a = 1.4
            x_horz = px + depth_horz * cos_a # get the x coord from the horz line intersect

            delta_depth = dy / sin_a # -1 / sin(315) = 1.4 | howlong a diagonal unit compared to dy(1)
            dx = delta_depth * cos_a # 1.4 * 0.7 = 0.98

            # the amount of horizontal lines the ray travels
            for i in range(MAX_DEPTH):
                tile_horz = int(x_horz), int(y_horz) # 0.98, 1
                if tile_horz in self.game.map.world_map: # if hits wall
                    break
                x_horz += dx # move 0.98
                y_horz += dy # move 1
                depth_horz += delta_depth # plus 1.4

            # check verticals
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 0.000001, -1) #
            
            depth_vert = (x_vert - px) / cos_a  # distance diagonal of dist x
            y_vert = py + depth_vert * sin_a  # player_y + sin(of diagonal)

            delta_depth = dx / cos_a # how long a diagonal unit compared to dx(1) | 1 / cos(315) = 1.4
            dy = delta_depth * sin_a # howmuch y per x unit | 1.4 * -0.7 = -0.98

            # the amount of vertical lines the ray travels
            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert) # 1, -0.7 | this is the first tile the ray hits on the vertical axis
                if tile_vert in self.game.map.world_map: # if mapindex  out of bounds of map
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            # get the shortest depth (does angle intersect with vertical or horizontal first)
            if depth_vert < depth_horz:
                depth = depth_vert
            else:
                depth = depth_horz

            # remove fish eye effect
            depth *= math.cos(self.game.player.angle - ray_angle)

            # show all ray lines
            #pg.draw.line(self.game.screen, 'yellow', (100 * px + WIDTH, 100 * py),
            #              (100 * px + WIDTH + 100 * depth * cos_a, 100 * py + 100 * depth * sin_a), 2)

            # projection
            projection_height = SCREEN_DIST / (depth + 0.0001) # avoid division by zero # 

            # draw walls
            ray_angle += DELTA_ANGLE

            # draw walls
            color = [255 / (1 + depth ** 5 * 0.00002)] * 3
            pg.draw.rect(self.game.screen,
                         color,
                         (ray * SCALE, HALF_HEIGHT - projection_height // 2, SCALE, projection_height)
            )

    def update(self):
        self.ray_cast()
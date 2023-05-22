import pygame as pg
import math

from raycasting.settings import *

class RayCasting:
    def __init__(self, game):
        self.game = game

    def ray_cast(self):
        px, py = self.game.player.position
        x_map, y_map = self.game.player.map_position

        # the angle of the first / most left ray in the FOV
        ray_angle = self.game.player.angle - HALF_FOV

        # for all 320 rays
        for ray in range(NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # horizontal line checking section ------------------------------------------------

            # get the y coord of the next horizontal line if the ray angle positive
            # if the ray angle is negative get the previous horizontal line
            y_horz, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 0.000001, -1)
            
            # get diagonal line distance between player and the next horizontal line
            depth_horz = (y_horz - py) / sin_a

            # get the x coord of the next horizontal line (where the ray will intersect)
            x_horz = px + depth_horz * cos_a

            # after the calculation of the player to the first horizontal line we can now
            # increment further with y units of 1 (the next horizontal lines)
            delta_depth = dy / sin_a  # length of diagonal for 1 y unit
            dx = delta_depth * cos_a  # howmuch x moves for 1 y unit

            # the next 20 horizontal lines intersections we're checking
            for i in range(MAX_DEPTH):
                # coordinates where the ray is intersecting on current vertical line
                tile_horz = int(x_horz), int(y_horz)
                
                # ray intersection with a wall, no need to check further
                if tile_horz in self.game.map.world_map:
                    break
                
                # update the coordinates when we go 1 horizontal line further
                x_horz += dx
                y_horz += dy

                # update the diagonal distance when we go 1 horizontal line further
                depth_horz += delta_depth

            # vertical line checking section ------------------------------------------------
            
            # get the x coord of the next vertical line if the ray cos angle is positive
            # if negative get the previous vertical line
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 0.000001, -1) #
            
            # get diagonal line distance between player and the next horizontal line
            depth_vert = (x_vert - px) / cos_a
            
            # get the y coord where the ray intersects the next vertical line
            y_vert = py + depth_vert * sin_a
            
            # after the calculation of the player to the first vertical line we can now
            # increment further with x units of 1 (for the next vertical lines)
            delta_depth = dx / cos_a 
            dy = delta_depth * sin_a

            # the next 20 horizontal lines intersections we're checking
            for i in range(MAX_DEPTH):
                # coordinates where the ray is intersecting on current vertical line
                tile_vert = int(x_vert), int(y_vert)
                
                # ray intersection with a wall, no need to check further
                if tile_vert in self.game.map.world_map:
                    break

                # update the coordinates when we go 1 vertical line further
                x_vert += dx
                y_vert += dy

                # update the diagonal distance when we go 1 vertical line further
                depth_vert += delta_depth

            # get the shortest depth as we always want the exact distance to the wall
            if depth_vert < depth_horz:
                depth = depth_vert
            else:
                depth = depth_horz

            # removes the fish eye effect by making sure on rays that that in
            depth *= math.cos(self.game.player.angle - ray_angle)

            # turn on to see all rays when displaying the map and playe
            # pg.draw.line(self.game.screen, 'yellow', (100 * px, 100 * py),
            #     (100 * px + 100 * depth * cos_a, 100 * py + 100 * depth * sin_a), 2)

            # the distance of the intersection difference ratio with the screen distance
            projection_height = SCREEN_DIST / (depth + 0.0001)  # avoids division by zero error 

            # get the angle of the next ray that will be processed in this loop
            ray_angle += DELTA_ANGLE

            # this draws the real in which each ray account for 2 pixels in width on the screen
            # and height projection of the wall if it intersected with one.
            color = [255 / (1 + depth ** 5 * 0.00002)] * 3
            pg.draw.rect(self.game.screen,
                         color,
                         (ray * SCALE, HALF_HEIGHT - projection_height // 2, SCALE, projection_height)
            )

    def update(self):
        self.ray_cast()
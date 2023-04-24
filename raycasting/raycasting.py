import pygame as pg
import math

from main import WIDTH, HEIGHT

FOV = math.pi / 3  # 60 degrees
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20


class RayCasting:
    def __init__(self, game):
        self.game = game

    def ray_cast(self):
        px, py = self.game.player.position
        x_map, y_map = self.player.position.map_position

        ray_angle = self.player.angle - HALF_FOV

        # shoot out a ray for every 
        for ray in range(NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # move 
            x_tile, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1, -1)

            ray_angle += DELTA_ANGLE

    def update(self):
        self.ray_cast()
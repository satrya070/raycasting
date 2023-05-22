import pygame as pg
import math

from raycasting.settings import *


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y, = PLAYER_POSITION
        self.angle = PLAYER_ANGLE
    
    def movement(self):
        sin = math.sin(self.angle)
        cos = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta
        speed_sin = speed * sin
        speed_cos = speed * cos

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx -= speed_cos
            dy -= speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy -= speed_cos
        if keys[pg.K_d]:
            dx -= speed_sin
            dy += speed_cos
        
        self.check_wall_collision(dx, dy)

        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROTATION * self.game.delta
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROTATION * self.game.delta

        # make sure angle stay within 360 degrees
        self.angle %= 2 * math.pi

    def update(self):
        self.movement()
    
    def check_walls(self, x, y):
        return (x, y) not in self.game.map.world_map
    
    def check_wall_collision(self, dx, dy):
        if self.check_walls(int(self.x + dx), int(self.y + dy)):
            self.x += dx
            self.y += dy

    def draw(self):
        # your drawing the map and player, you can turn this on to see every ray that's projected
        # pg.draw.line(
        #     self.game.screen,
        #     "green",
        #     (self.x * 100, self.y * 100),
        #     (
        #         self.x * 100 + WIDTH * math.cos(self.angle),
        #         self.y * 100 + WIDTH * math.sin(self.angle)
        #     ),
        #     2
        # )

        pg.draw.circle(
            self.game.screen,
            "green",
            (self.x * 100, self.y * 100), 15
        )

    @property
    def position(self):
        return self.x, self.y

    @property
    def map_position(self):
        return int(self.x), int(self.y)

import pygame as pg
import math
#from main import WIDTH, HEIGHT

PLAYER_POSITION = (0, 0)
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.001
PLAYER_ROTATION = 0.001

WIDTH, HEIGHT = 640, 480

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
        speed_cos = speed* cos

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
        
        self.x += dx
        self.y += dy

        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROTATION * self.game.delta
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROTATION * self.game.delta
        self.angle %= 2 * math.pi

    def update(self):
        self.movement()

    def draw(self):
        pg.draw.line(
            self.game.screen,
            "yellow",
            (self.x * 100, self.y * 100),
            (
                self.x * 100 + WIDTH * math.cos(self.angle),
                self.y * 100 + WIDTH * math.sin(self.angle)
            ),
            2
        )

    @property
    def position(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)

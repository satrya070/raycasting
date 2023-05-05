import pygame as pg
from raycasting.settings import *

map = [
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [0, 1, 0, 1]
]

class Map:
    def __init__(self, game):
        self.game = game
        self.map = map
        self.world_map = {}
        self.get_map()
    
    def get_map(self):
        for i, row in enumerate(self.map):
            for j, col in enumerate(row):
                if col:
                    self.world_map[(i, j)] = col
    
    def draw(self):
        [pg.draw.rect(self.game.screen, "darkgray", (pos[0] * 100 + WIDTH, pos[1] * 100, 100, 100), 2)
         for pos in self.world_map]
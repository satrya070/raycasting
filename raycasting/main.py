import sys
import pygame as pg

from raycasting.settings import *
from raycasting.map import Map
from raycasting.player import Player
from raycasting.raycast import RayCasting

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RESOLUTION)
        self.clock = pg.time.Clock()
        self.delta = 1
        self.new_game()
    
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.raycasting = RayCasting(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        pg.display.flip()
        self.delta = self.clock.tick(FPS)
        pg.display.set_caption(f"{self.clock.get_fps():.2f}")

    def draw(self):
        self.screen.fill("black")
        # turn these on to the raycasting on the map with the player
        # self.map.draw()
        # self.player.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()


    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
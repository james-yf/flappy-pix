import random
import pygame
from states.game_state import GameState
from consts import GAME_W, GAME_H, TILE_SIZE, IMGS
from parallax_layer import ParallaxLayer
from player import Player

class PlayState(GameState):
    def __init__(self,game):
        super().__init__(game)

        self.sky_img=pygame.image.load(IMGS/"sky.png").convert()

        self.clouds_img=pygame.image.load(IMGS/"clouds.png").convert_alpha()
        self.clouds=ParallaxLayer(self.clouds_img, speed=30, draw_at_y=TILE_SIZE)

        self.tree_img=pygame.image.load(IMGS/"tree.png").convert_alpha()
        self.tree=ParallaxLayer(self.tree_img, speed=100, draw_at_y=GAME_H-2*TILE_SIZE)

        self.grass_img=pygame.image.load(IMGS/"grass.png").convert()

        self.player_img=pygame.image.load(IMGS/"sheep.png").convert_alpha()
        self.player_pos=(GAME_W//2-TILE_SIZE, GAME_H//2)
        self.player=Player(self.player_pos,self.player_img)

    def handle_input(self, e):
        self.player.handle_input(e)

    def update(self, dt):
        self.clouds.update(dt)
        self.tree.update(dt)
        self.player.update(dt)

    def draw(self, surf):
        surf.blit(self.sky_img,(0,0))
        self.clouds.draw(surf)
        self.tree.draw(surf)
        surf.blit(self.grass_img,(0,GAME_H-TILE_SIZE))
        self.player.draw(surf)

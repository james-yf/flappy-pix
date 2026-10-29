import pygame
from states.game_state import GameState
from consts import GAME_W,GAME_H,IMGS
from player import Player

class PlayState(GameState):
    def __init__(self,game):
        super().__init__(game)
        self.player_img=pygame.image.load(IMGS/"sheep.png").convert_alpha()
        self.player_img=pygame.transform.scale(self.player_img,(32,32))
        self.player_pos=(GAME_W//2-self.player_img.get_width(), GAME_H//2)
        self.player=Player(self.player_pos,self.player_img)

    def handle_input(self, e):
        self.player.handle_input(e)

    def update(self, dt):
        self.player.update(dt)

    def draw(self, surf):
        surf.fill((0,255,255))
        self.player.draw(surf)

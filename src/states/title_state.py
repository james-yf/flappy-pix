import pygame
from states.game_state import GameState
from states.play_state import PlayState
from parallax_layer import ParallaxLayer
from consts import GAME_W, GAME_H, TILE_SIZE 
from assets import get_asset
from math import sin, radians

class TitleState(GameState):
    def __init__(self,game):
        super().__init__(game)

        self.font=pygame.font.Font(None,16)
        self.prompt_txt=self.font.render("Press SPACE to start", True, (255,255,255))
        self.prompt_w,self.prompt_h=self.prompt_txt.get_size()

        self.sky_img=get_asset("sky")

        self.clouds_img=get_asset("clouds")
        self.clouds=ParallaxLayer(self.clouds_img, speed=30, draw_at_y=TILE_SIZE)

        self.tree_img=get_asset("tree")
        self.tree=ParallaxLayer(self.tree_img, speed=100, draw_at_y=GAME_H-2*TILE_SIZE)

        self.grass_img=get_asset("grass")

        self.player_img=get_asset("sheep")        
        self.player_base_y=GAME_H//2
        self.player_rect=pygame.Rect((GAME_W//2-TILE_SIZE, self.player_base_y), self.player_img.get_size()) 

    def handle_input(self,e):
        if e.type==pygame.KEYDOWN and e.key==pygame.K_SPACE:
            self.game.switch_state(PlayState(self.game))

    def update(self,dt):
        self.clouds.update(dt)
        self.tree.update(dt)
        t=pygame.time.get_ticks()/1000
        bobbing_offset=sin(t*5) * 6
        self.player_rect.y=(self.player_base_y+bobbing_offset)

    def draw(self,surf):
        surf.blit(self.sky_img,(0,0))
        self.clouds.draw(surf)
        self.tree.draw(surf)
        surf.blit(self.grass_img,(0,GAME_H-TILE_SIZE))
        surf.blit(self.player_img, self.player_rect)
        surf.blit(self.prompt_txt,(GAME_W//2-self.prompt_w//2, GAME_H//2+TILE_SIZE*1.5))

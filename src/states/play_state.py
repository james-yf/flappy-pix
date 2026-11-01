import random
import pygame
from states.game_state import GameState
from consts import GAME_W, GAME_H, TILE_SIZE, IMGS
from parallax_layer import ParallaxLayer
from player import Player
from utils import extract_tile
from pipe import PipePair
from states.game_over_state import GameOverState

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

        self.pipe_tilesheet=pygame.image.load(IMGS/"logs.png")
        self.pipe_body_img=extract_tile(self.pipe_tilesheet, col_off=0, row_off=0)
        self.pipe_top_img=extract_tile(self.pipe_tilesheet, col_off=1, row_off=0)
        self.pipe_pair=PipePair(self.pipe_body_img, self.pipe_top_img)
        self.pipe_pairs=[self.pipe_pair]

        self.score_font=pygame.font.Font(None,16)
        self.score=0

    def handle_input(self, e):
        self.player.handle_input(e)

    def update(self, dt):
        self.clouds.update(dt)
        self.tree.update(dt)
        self.player.update(dt)

        for pipe_pair in self.pipe_pairs:
            pipe_pair.update(dt)
            if pipe_pair.player_collided(self.player.mask, self.player.rect):
                self.game.switch_state(GameOverState(self.game))

        pipe_pairs_on_screen=[pipe_pair for pipe_pair in self.pipe_pairs if pipe_pair.rect.right > 0]
        for pipe_pair in pipe_pairs_on_screen:
            if pipe_pair.rect.x==GAME_W//2-TILE_SIZE:
                pipe_pairs_on_screen.append(PipePair(self.pipe_body_img, self.pipe_top_img))  
            if not pipe_pair.scored and pipe_pair.rect.centerx < self.player.rect.right:
                pipe_pair.scored=True
                self.score+=1

        self.pipe_pairs=pipe_pairs_on_screen

    def draw(self, surf):
        surf.blit(self.sky_img,(0,0))
        self.clouds.draw(surf)
        self.tree.draw(surf)
        surf.blit(self.grass_img,(0,GAME_H-TILE_SIZE))
        for pipe_pair in self.pipe_pairs:
            pipe_pair.draw(surf)
        self.player.draw(surf)
        score_txt=self.score_font.render(f"Score: {self.score}", True, (255,255,255)) 
        surf.blit(score_txt,(0,0))

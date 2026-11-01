import random
import pygame
from consts import GAME_W, GAME_H, TILE_SIZE

PIPE_SPEED=50

class Pipe:
    def __init__(self, body_tile_img, cap_tile_img, size, start_top):
        self.x=GAME_W-TILE_SIZE
        self.y, self.off = (0, TILE_SIZE) if start_top else (GAME_H-TILE_SIZE*2, -TILE_SIZE) 
        self.rect=pygame.Rect(self.x, self.y, TILE_SIZE, size*TILE_SIZE) 
        self.body_tile_img=body_tile_img
        self.cap_tile_img=cap_tile_img
        self.size=size

    def draw(self,surf):
        curr_y=self.rect.y
        for i in range(self.size):
            surf.blit(self.body_tile_img,(self.rect.x, curr_y))
            curr_y+=self.off
        surf.blit(self.cap_tile_img,(self.rect.x, curr_y))

class PipePair:
    def __init__(self, body_tile_img, top_tile_img):
        self.body_tile_img=body_tile_img
        self.top_tile_img=top_tile_img
        self.top_pipe_size, self.bottom_pipe_size=self.rand_sizes()
        self.top_pipe=Pipe(body_tile_img, top_tile_img, self.top_pipe_size, False) 
        self.bottom_pipe=Pipe(body_tile_img, top_tile_img, self.bottom_pipe_size, True) 
        self.rect=pygame.Rect(
                self.top_pipe.rect.x, self.top_pipe.rect.y, TILE_SIZE, GAME_H 
        ) 

    def rand_sizes(self):
        h=GAME_H//TILE_SIZE 
        grass=1
        caps=2
        gap=3
        tiles_for_pipes=h-grass-caps-gap   
        size_top=random.randint(0, tiles_for_pipes)
        size_bottom=tiles_for_pipes-size_top
        return size_top, size_bottom

    def update(self,dt):
        self.rect.x-=PIPE_SPEED*dt
        self.top_pipe.rect.x=self.rect.x
        self.bottom_pipe.rect.x=self.rect.x

    def draw(self,surf):
        self.top_pipe.draw(surf)
        self.bottom_pipe.draw(surf)

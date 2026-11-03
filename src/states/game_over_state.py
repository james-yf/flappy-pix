import pygame
from states.game_state import GameState
from consts import GAME_W, GAME_H

class GameOverState(GameState):
    def __init__(self,game):
        super().__init__(game)
        self.over_font=pygame.font.Font(None,32)
        self.prompt_font=pygame.font.Font(None,16)
        self.txt_color=(255,255,255)
        self.over_txt=self.over_font.render("Game Over...", True, self.txt_color)
        self.prompt_txt=self.prompt_font.render("Press R to restart", False, self.txt_color)
        self.over_w,self.over_h=self.over_txt.get_size()
        self.prompt_w,self.prompt_h=self.over_txt.get_size()

    def handle_input(self,e):
        if e.type==pygame.KEYDOWN and e.key==pygame.K_r: 
            from states.title_state import TitleState
            self.game.switch_state(TitleState(self.game))

    def update(self,dt):
        pass

    def draw(self,surf):
        surf.blit(self.over_txt,(GAME_W//2-self.over_w//2, GAME_H//2-self.over_h//2))
        surf.blit(self.prompt_txt,(GAME_W//2-self.prompt_w//2, GAME_H//2+self.over_h))

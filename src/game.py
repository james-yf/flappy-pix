import sys
import pygame
from consts import GAME_W,GAME_H
from states.play_state import PlayState

SCALE_FACTOR=4

class Game:
    def __init__(self):
        pygame.init()
        self.surf=pygame.Surface((GAME_W,GAME_H))
        self.screen=pygame.display.set_mode((GAME_W*SCALE_FACTOR,GAME_H*SCALE_FACTOR),vsync=1)
        pygame.display.set_caption("Flappy Pix")
        self.clock=pygame.time.Clock()
        self.font=pygame.font.Font(None,16)
        self.running=True
        self.state=PlayState(self)

    def switch_state(self,state):
        self.state=state

    def run(self):
        while self.running:
            dt=self.clock.tick(60)/1000

            for e in pygame.event.get():
                if e.type==pygame.QUIT:
                    self.running=False
                    break
                self.state.handle_input(e)

            self.state.update(dt)

            fps_txt=self.font.render(f"FPS: {int(self.clock.get_fps())}", True, (0,0,0))
            self.state.draw(self.surf)
            self.surf.blit(fps_txt,(0,0))
            pygame.transform.scale(self.surf,self.screen.get_size(),self.screen)

            pygame.display.flip()

        pygame.quit()
        sys.exit()

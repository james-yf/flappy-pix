import pygame

class Player:
    def __init__(self,pos,img):
        self.x,self.y=pos
        self.img=img
        self.v=0
        self.angle=0

    def flap(self):
        self.v=-300
        self.angle=45

    def handle_input(self,e):
        if e.type==pygame.KEYDOWN and e.key==pygame.K_SPACE:
            self.flap()
    
    def update(self,dt):
        dv=981*dt
        self.v+=dv
        self.y+=(self.v*dt)

        if self.angle >= -45:
            self.angle-=(100*dt)

    def draw(self,screen):
        rot=pygame.transform.rotate(self.img,self.angle)
        screen.blit(rot,(self.x,self.y))

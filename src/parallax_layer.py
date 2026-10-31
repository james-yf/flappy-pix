from consts import GAME_W

class ParallaxLayer:
    def __init__(self,img,speed,draw_at_y):
        self.speed=speed
        self.y=draw_at_y
        self.img=img
        self.left_img_rect=self.img.get_rect()
        self.left_img_rect.left=0
        self.right_img_rect=self.img.get_rect()
        self.right_img_rect.left=GAME_W

    def update(self,dt):
        self.left_img_rect.left-=self.speed*dt
        self.right_img_rect.left-=self.speed*dt
        if self.right_img_rect.right<=0: self.right_img_rect.left=GAME_W
        if self.left_img_rect.right<=0: self.left_img_rect.left=GAME_W

    def draw(self,surf):
        surf.blit(self.img,(self.left_img_rect.left,self.y))
        surf.blit(self.img,(self.right_img_rect.left,self.y))

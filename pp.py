from random import *
from pygame import *
import time as timer
total = 0
b = True
a = True
gametime = "0"
start = timer.time()
clock = time.Clock()
window = display.set_mode((700,500))
class spriten(sprite.Sprite):
    def __init__ (self, img, sx, sy, px, py, pspx, pspy):
        super().__init__()
        self.sizex = sx
        self.sizey = sy
        self.image = transform.scale(image.load(img),(self.sizex,self.sizey))
        self.last_time = timer.time()
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
        self.start_x = px
        self.start_y = py
        self.speedx2 = pspx
        self.speedy2 = pspy
        self.speedx = pspx
        self.speedy = pspy
        self.rects = [self.rect.x,self.rect.y]
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and hero.rect.x >5:
                hero.rect.x -= 3
        if keys[K_RIGHT] and hero.rect.x < 635:
                hero.rect.x += 3
        if keys[K_UP] and hero.rect.y > 250:
                hero.rect.y -= 3
        if keys[K_DOWN] and hero.rect.y < 450:
                hero.rect.y += 3
    def update2(self):
        keys = key.get_pressed()
        if keys[K_A] and hero.rect.x >5:
                hero.rect.x -= 3
        if keys[K_D] and hero.rect.x < 635:
                hero.rect.x += 3
        if keys[K_W] and hero.rect.y > 250:
                hero.rect.y -= 3
        if keys[K_S] and hero.rect.y < 450:
                hero.rect.y += 3
    def upd(self):
            if ball.rect.y < 0:
                self.speedy *=-1
            if ball.rect.y > 435:
                self.speedy*=-1
            self.rect.x += self.speedx
            self.rect.y += self.speedy
ball = spriten("pngwing.com (1).png",65,65,350,250,3,3)
while a:
        ball.reset()
        if b:
                ball.upd()
        for e in event.get():
            if e.type == QUIT:
                a = False
        display.update()
        

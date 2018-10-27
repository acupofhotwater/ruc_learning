
import pygame
import random

# screen
SCREEN_RECT = pygame.Rect(0,0,480,800)
# create enemy event
CREATE_ENEMY_EVENT = pygame.USEREVENT
# fire
HERO_FIRE_EVENT = pygame.USEREVENT + 2



class GameSprite(pygame.sprite.Sprite):
    def __init__(self,new_image,new_speed=1):
        super().__init__()
        # image
        self.image = pygame.image.load(new_image)
        # size
        self.rect = self.image.get_rect()
        # speed
        self.speed = new_speed

    def update(self):
        #默认垂直方向移动 y轴控制垂直方向
        self.rect.y += self.speed

class Background(GameSprite):
    def __init__(self,is_alt = False):

        super().__init__("./bg_01.png")
        if is_alt:
            #如果是第二张图片 初始位置为-self.rect.height
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
    
class Enemy(GameSprite):
    def __init__(self):
        # image
        super().__init__("./hero.png")
        # speed 
        self.speed = 2
        # size
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)

    def update(self):
        super().update()
        # out the screen
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

class Hero(GameSprite):
    def __init__(self):
        # image
        super().__init__("./hero.png",0)

        # position
        self.rect.center =SCREEN_RECT.center
        self.rect.bottom =SCREEN_RECT.bottom-120
        self.move = False
        # bullet
        self.bullet = pygame.sprite.Group()

    def update(self):
        #super().update()
        if not self.move:
            self.rect.x += self.speed
        else:
            self.rect.y += self.speed

        # out screen
        if self.rect.bottom <= 0:
            self.rect.y = self.rect.bottom+SCREEN_RECT.height
        elif self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

        if self.rect.right <= 0:
            self.rect.x = self.rect.right+SCREEN_RECT.width
        elif self.rect.x >= SCREEN_RECT.width:
            self.rect.x = -self.rect.width

    def fire(self):
        for i in (1,2,3):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y-i*20
            bullet.rect.center = self.rect.center
            self.bullet.add(bullet)


class Bullet(GameSprite):

    def __init__(self):
        super().__init__("./bullet_1.png",-5)
    def update(self):
        super().update()
        # out screen
        if self.rect.bottom < 0:
            self.kill()
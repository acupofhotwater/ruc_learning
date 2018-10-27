import pygame
from plane_sprites import *


class PlaneGame(object):
    def __init__(self):
        print("start init")

        #1.create screen
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()

        self.creat_sprites()

        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)

        pygame.time.set_timer(HERO_FIRE_EVENT,200)

        print("init ok")

    def start_game(self):
        while True:
            # set zhen
            self.clock.tick(1000)

            self.event_handler()

            self.check_collide()

            self.update_sprites()

            pygame.display.update()


    def creat_sprites(self):
        bg1 = Background()
        bg2 = Background(True)
        
        # background
        self.back_group = pygame.sprite.Group(bg1,bg2)
        # hero
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
        # enemy
        self.enemy_group = pygame.sprite.Group()
        
    def event_handler(self):

        for event in pygame.event.get():

            keys_pressed = pygame.key.get_pressed()
            #控制飞机移动
            if keys_pressed[pygame.K_LEFT]:
                self.hero.move = False
                self.hero.speed = -9
            elif keys_pressed[pygame.K_RIGHT]:
                self.hero.move = False
                self.hero.speed = 9
            elif keys_pressed[pygame.K_UP]:
                self.hero.move = True
                self.hero.speed = -9
            elif keys_pressed[pygame.K_DOWN]:
                self.hero.move = True
                self.hero.speed = 9
            else:
                self.hero.speed = 0

            # create enemy
            if event.type == CREATE_ENEMY_EVENT:
                self.enemy_group.add(Enemy())
            # fire
            elif event.type == HERO_FIRE_EVENT:
                    self.hero.fire()
            # quit
            elif event.type == pygame.QUIT:
                self.game_over()

    # update sprites
    def update_sprites(self):
        for x in[self.back_group,self.enemy_group,self.hero_group,self.hero.bullet]:
            x.update()
            x.draw(self.screen)

    def check_collide(self):

        pygame.sprite.groupcollide( self.enemy_group,self.hero.bullet, True, True)
        herodown = pygame.sprite.spritecollide( self.hero, self.enemy_group, True)

        if len(herodown)>0:
            self.hero.kill()
            PlaneGame.game_over()

    @staticmethod
    def game_over():
        print("Game Over!")
        pygame.quit()
        exit()
        
if __name__ == "__main__":
    game = PlaneGame()
    game.start_game()
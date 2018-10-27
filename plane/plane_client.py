import socket
import pygame
from plane_sprites import *

class PlaneGame(object):

    def __init__(self, ENEMY_EVENT_PERIOD, HERO_FIRE_EVENT_PERIOD) :
        print("start init")

        #1.create screen
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()

        self.creat_sprites()
        self.score = 0

        pygame.time.set_timer(CREATE_ENEMY_EVENT, ENEMY_EVENT_PERIOD)

        pygame.time.set_timer(HERO_FIRE_EVENT, HERO_FIRE_EVENT_PERIOD)

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

        enemydown = pygame.sprite.groupcollide( self.enemy_group,self.hero.bullet, True, True)
        if len(enemydown)>0:
            self.score += 1
        herodown = pygame.sprite.spritecollide( self.hero, self.enemy_group, True)

        if len(herodown)>0:
            self.hero.kill()
            self.game_over()
    
    def game_over(self):
        print("Game Over!")
        print(self.score)
        pygame.quit()
        exit()


if __name__ == "__main__":
    """send start game to server recv game setting"""
    # create socket connect
    client_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999
    client_conn.connect((host, port))

    # send start to s
    client_conn.send("start".encode("UTF-8"))
    # recv game setting
    ENEMY_EVENT_PERIOD = int(client_conn.recv(1024))
    print ("ENEMY_EVENT_PERIOD", ENEMY_EVENT_PERIOD)
    HERO_FIRE_EVENT_PERIOD = int(client_conn.recv(1024))
    print ("HERO_FIRE_EVENT_PERIOD", HERO_FIRE_EVENT_PERIOD)

    # start game
    game = PlaneGame(ENEMY_EVENT_PERIOD, HERO_FIRE_EVENT_PERIOD)
    game.start_game()

    client_conn.close()
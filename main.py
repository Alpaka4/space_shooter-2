import pygame
import sys
import random
from settings import *
from player import Player
from sky import Sky
from asteroid import Asteroid
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT))
all_sprites = pygame.sprite.Group()
meteors = pygame.sprite.Group()
bullets = pygame.sprite.Group()
bonuses = pygame.sprite.Group()
player=Player("images/Ship.png",screen,(SCREEN_WIDTH)//2,(SCREEN_HEIGHT)//2)
sky=Sky("images/Sky.jpg",screen,0,0)
sky_2=Sky("images/Sky.jpg",screen,0,-1000)
meteor_filename_list = ["images/meteorGrey_big1.png","images/meteorGrey_big2.png","images/meteorGrey_med1.png","images/meteorGrey_med2.png",
                        "images/meteorGrey_small1.png","images/meteorGrey_small2.png"]
meteor_image_list = []
for filename in meteor_filename_list:
    meteor_image = pygame.image.load(filename).convert()
    meteor_image_list.append(meteor_image)
all_sprites.add(player)
for i in range(METEORS_QTY):
    asteroid = Asteroid(screen,meteor_image_list)
    meteors.add(asteroid)
    all_sprites.add(asteroid)
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    all_sprites.update()
    sky.update()
    sky_2.update()

    screen.fill(BLACK)
    sky.draw()
    sky_2.draw()
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(FPS)

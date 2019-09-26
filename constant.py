import pygame

FRAME_PER_SECOND = 60
RESOURCE_HERO_IMAGE = "./resource/hero1.png"
RESOURCE_HERO_IMAGE_2 = "./resource/hero2.png"
RESOURCE_HERO_DESTROYED = ["./resource/hero_blowup_n1.png",
                           "./resource/hero_blowup_n2.png",
                           "./resource/hero_blowup_n3.png",
                           "./resource/hero_blowup_n4.png"]
RESOURCE_BG_IMAGE = "./resource/background.png"
RESOURCE_ENEMY_IMAGE = "./resource/enemy0.png"
RESOURCE_ENEMY_IMAGE_1 = "./resource/enemy1.png"
RESOURCE_ENEMY_DESTROYED = ["./resource/enemy0_down1.png",
                            "./resource/enemy0_down2.png",
                            "./resource/enemy0_down3.png",
                            "./resource/enemy0_down4.png"]
RESOURCE_BULLET_IMAGE = "./resource/bullet1.png"
ENEMY_EVENT_TYPE = pygame.USEREVENT
HERO_BULLET_EVENT_TYPE = pygame.USEREVENT + 1

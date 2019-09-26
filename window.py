import pygame

screen_rect = pygame.rect.Rect(0, 0, 480, 852)

__screen = pygame.display.set_mode(screen_rect.size)


def get_screen():
    return __screen

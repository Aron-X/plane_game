import game_support
import window
from constant import *
from main import PlaneGame


class GameSprite(pygame.sprite.Sprite):
    """Game Sprite"""

    def __init__(self, image_path, dest=(0, 0), speed=3):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = dest[0]
        self.rect.y = dest[1]

    def update(self, *args):
        super().update()
        self.rect.y += self.speed


class Hero(GameSprite):
    over_flag = False

    def __init__(self, image_path=RESOURCE_HERO_IMAGE, speed=0):
        super().__init__(image_path, speed=speed)
        self.rect.centerx = window.screen_rect.centerx
        self.rect.bottom = window.screen_rect.bottom - 20
        self.bullets = pygame.sprite.Group()
        self.__over_index = 0
        self.__fire_flag = False

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y
        if self.rect.x > window.screen_rect.width:
            self.rect.x = -100
        if self.rect.x < -100:
            self.rect.x = window.screen_rect.width
        if self.rect.top < 0:
            self.rect.top = window.screen_rect.top
        if self.rect.bottom > window.screen_rect.bottom:
            self.rect.bottom = window.screen_rect.bottom

    def update(self, *args):
        super().update()
        if self.rect.y < -124:
            self.rect.y = window.screen_rect.height
        if self.rect.y > window.screen_rect.height:
            self.rect.y = -124
        self.switch_animation()
        if Hero.over_flag:
            self.__start_destroyed_animation()
            if self.__is_destroyed_animation_over():
                self.kill()

    def __start_destroyed_animation(self):
        if self.__over_index < len(RESOURCE_HERO_DESTROYED):
            self.image = pygame.image.load(RESOURCE_HERO_DESTROYED[self.__over_index])
        self.__over_index += 1

    def switch_animation(self):
        if self.__fire_flag:
            self.__fire_flag = False
            self.image = pygame.image.load(RESOURCE_HERO_IMAGE)
        else:
            self.image = pygame.image.load(RESOURCE_HERO_IMAGE_2)
            self.__fire_flag = True

    def fire(self):
        self.bullets.add(Bullet(self.rect))

    def __is_destroyed_animation_over(self):
        return self.__over_index > len(RESOURCE_HERO_DESTROYED)

    def kill(self):
        super().kill()
        PlaneGame.game_over()


class Background(GameSprite):
    def __init__(self, image_path, dest, speed=3):
        super().__init__(image_path, dest, speed)

    def update(self, *args):
        super().update()
        if self.rect.y > window.screen_rect.height:
            self.rect.y = -window.screen_rect.height


class Enemy(GameSprite):

    def __init__(self):
        super().__init__(RESOURCE_ENEMY_IMAGE, speed=game_support.random_int(3, 10))
        self.rect.x = game_support.random_int(0, window.screen_rect.width - self.rect.width)
        self.rect.y = -self.rect.height
        self.__over_index = 0
        self.over_flag = False

    def update(self, *args):
        super().update()
        if self.rect.y > window.screen_rect.height:
            self.kill()
        if self.over_flag:
            self.__start_destroyed_animation()
            if self.__is_destroyed_animation_over():
                super().kill()

    def __start_destroyed_animation(self):
        if self.__over_index < len(RESOURCE_ENEMY_DESTROYED):
            self.image = pygame.image.load(RESOURCE_ENEMY_DESTROYED[self.__over_index])
        self.__over_index += 1

    def __is_destroyed_animation_over(self):
        return self.__over_index > len(RESOURCE_ENEMY_DESTROYED)

    def kill(self):
        self.over_flag = True

    def __del__(self):
        # print("Enemy object cleared")
        pass


class Bullet(GameSprite):
    def __init__(self, plane_rect):
        super().__init__(RESOURCE_BULLET_IMAGE, speed=-20)
        self.rect.bottom = plane_rect.top
        self.rect.centerx = plane_rect.centerx

    def update(self, *args):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        # print("Bullet object cleared")
        pass

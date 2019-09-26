from modules import *
from constant import *


class PlaneGame(object):
    """plane game main object"""

    def __init__(self):
        pygame.init()
        self.__screen = window.get_screen()
        self.__click = pygame.time.Clock()
        self.__initial_sprites()
        # create enemy event
        pygame.time.set_timer(ENEMY_EVENT_TYPE, 1000)
        pygame.time.set_timer(HERO_BULLET_EVENT_TYPE, 180)

    def __initial_sprites(self):
        self.__bg_group = pygame.sprite.Group(
            Background(RESOURCE_BG_IMAGE, (0, 0)),
            Background(RESOURCE_BG_IMAGE, (0, -window.screen_rect.height)),
        )
        self.hero = Hero()
        self.__hero_group = pygame.sprite.Group(self.hero)
        self.__enemy_group = pygame.sprite.Group()

    def __update_sprites(self):
        self.__bg_group.update()
        self.__bg_group.draw(self.__screen)
        self.__hero_group.update()
        self.__hero_group.draw(self.__screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.__screen)
        self.__enemy_group.update()
        self.__enemy_group.draw(self.__screen)

    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets, self.__enemy_group, True, True)
        collide_sprites = pygame.sprite.spritecollide(self.hero, self.__enemy_group, True)
        if len(collide_sprites) > 0:
            Hero.over_flag = True

    def __even_handler(self):
        kep_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.game_over()
            # add one enemy plane per second
            if event.type == ENEMY_EVENT_TYPE:
                self.__enemy_group.add(Enemy())
            if event.type == HERO_BULLET_EVENT_TYPE:
                if kep_pressed[pygame.K_a]:
                    self.hero.fire()
        # hero move control
        if kep_pressed[pygame.K_RIGHT]:
            self.hero.move(5, 0)
        if kep_pressed[pygame.K_LEFT]:
            self.hero.move(-5, 0)
        if kep_pressed[pygame.K_UP]:
            self.hero.move(0, -5)
        if kep_pressed[pygame.K_DOWN]:
            self.hero.move(0, 5)

    def start(self):
        while True:
            self.__click.tick(FRAME_PER_SECOND)
            self.__even_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()

    @staticmethod
    def game_over():
        pygame.quit()
        exit()


def main():
    PlaneGame().start()


if __name__ == '__main__':
    main()

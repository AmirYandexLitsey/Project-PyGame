import pygame as p, pygame
import os
from pygame import mixer
import random
import sys

pygame.init()
width = 1280
height = 720
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# pygame.mixer.music.load("")

sp = []
for _ in range(1, 10):
        sp.append(_)
print(sp)
class Level1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Изображения/1.png")
        self.rect = self.image.get_rect()
        if window is True:
            self.rect.center = (990 - 400, 540)
        else:
            self.rect.center = (bk_w / 2 - 400, bk_h / 2)


class Level2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Изображения/2.png")
        self.rect = self.image.get_rect()
        if window is True:
            self.rect.center = (990 - 200, 540)
        else:
            self.rect.center = (bk_w / 2 - 200, bk_h / 2)


class Level3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Изображения/3.png")
        self.rect = self.image.get_rect()
        if window is True:
            self.rect.center = (990, 540)
        else:
            self.rect.center = (bk_w / 2, bk_h / 2)


class Level4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Изображения/4.png")
        self.rect = self.image.get_rect()
        if window is True:
            self.rect.center = (990 + 200, 540)
        else:
            self.rect.center = (bk_w / 2 + 200, bk_h / 2)


class Level5(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.clicked = pygame.image.load("Изображения/5_clicked.png")
        self.noclicked = pygame.image.load("Изображения/5.png")
        self.image = self.noclicked
        self.rect = self.image.get_rect()
        if window is True:
            self.rect.center = (990 + 400, 540)
        else:
            self.rect.center = (bk_w / 2 + 400, bk_h / 2)

    def update(self, *args):
        global Menu, InLevel_5
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            InLevel_5 = True
            Menu = False


class Rat(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Изображения/Rat-PNG-Picture.png")
        self.rect = self.image.get_rect()
        spisok = random.choice(sp)
        visota = spisok // 4
        if spisok % 3 == 1:
            self.rect.center = (475, 250 + visota * 125)
        if spisok % 3 == 2:
            self.rect.center = (600, 250 + visota * 125)
        if spisok % 3 == 0:
            self.rect.center = (725, 250 + visota * 125)




    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            print(1)
            self.kill()


class Back(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.back = pygame.image.load("Изображения/233-2338375_go-back-icon-png-transparent-png.png").convert()
        self.back_transform = p.transform.smoothscale(self.back, (50, 50))
        self.color = self.back_transform.get_at((0, 0))
        self.back_transform.set_colorkey(self.color)
        self.image = self.back_transform
        self.rect = self.image.get_rect()
        if InLevel_5 is True:
            if window is True:
                self.rect.center = (1890, 1050)
            else:
                self.rect.center = (bk_w - 30, bk_h - 30)

    def update(self, *args):
        global Menu, InLevel_5
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            InLevel_5 = False
            Menu = True


def screen_setting(bk_w, bk_h):
    global window
    window = False
    screen = p.display.set_mode((bk_w, bk_h), 0)
    p.display.set_caption('Поймай крысу')  # название окна
    p.display.set_icon(pygame.image.load("Изображения/icon.png"))  # ставим иконку крысы для окна
    bk_orig = p.image.load("Изображения/Phon.jpg").convert()
    bg_orig5 = p.image.load("Изображения/5_level_bg2.0.png").convert()
    mouse_image = p.image.load("Изображения/2534908.png").convert()
    mouse_image_transform = p.transform.smoothscale(mouse_image, (30, 30))
    color = mouse_image_transform.get_at((0, 0))
    mouse_image_transform.set_colorkey(color)
    pygame.mouse.set_visible(False)
    bg = p.transform.smoothscale(bk_orig, (bk_w, bk_h))
    bg5 = p.transform.smoothscale(bg_orig5, (bk_w, bk_h))
    clock = p.time.Clock()
    menu_sprites = pygame.sprite.Group()
    level_sprites = p.sprite.Group()
    Spawn = False
    level1 = Level1()
    level2 = Level2()
    level3 = Level3()
    level4 = Level4()
    level5 = Level5()
    menu_sprites.add(level1, level2, level3, level4, level5)
    while True:
        otc = 1000
        c = 0
        Pause = True
        while Menu == True:
            for event in p.event.get():
                if event.type == p.QUIT:
                    sys.exit()
                menu_sprites.update(event)
            screen.blit(bg, (0, 0))
            if p.mouse.get_focused():
                menu_sprites.draw(screen)
                menu_sprites.update()
                x, y = pos = p.mouse.get_pos()
                screen.blit(mouse_image_transform, (x - 10, y - 15))
                clock.tick(FPS)
                p.display.update()

            else:
                menu_sprites.draw(screen)
                menu_sprites.update()
                clock.tick(FPS)
                p.display.update()

            if Menu is False:
                break


        while InLevel_5 is True:  # Здесь начинаются уровни
            ticks = pygame.time.get_ticks()
            seconds = int(ticks / 1000 % 60)
            back = Back()
            rat = Rat()
            level_sprites.add(back)
            pygame.mouse.set_visible(False)
            if seconds // otc == 0:
                otc += 1000
                c += 1
                if c % 60 == 0:
                    Spawn = True
                    print(2)

            if Spawn:
                level_sprites.add(rat)
                Spawn = False
            else:
                pass
            for event in p.event.get():
                if event.type == p.QUIT:
                    sys.exit()

                level_sprites.update(event)


            screen.blit(bg5, (0, 0))

            if p.mouse.get_focused():
                level_sprites.draw(screen)
                level_sprites.update()
                x, y = pos = p.mouse.get_pos()
                screen.blit(mouse_image_transform, (x - 10, y - 15))
                clock.tick(FPS)
                p.display.update()

            else:
                level_sprites.draw(screen)
                level_sprites.update()
                clock.tick(FPS)
                p.display.update()


Spawn = False
Menu = True
InLevel_5 = False
InLevel_4 = False
InLevel_3 = False
InLevel_2 = False
InLevel_1 = False
bk_w = 1280
bk_h = 720
screen_setting(1280, 720)
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
Point = 0

spisok = [480, 260, 640, 260, 800, 360, 475, 365, 635, 360, 800, 365, 480, 470, 635, 470, 800, 470]
w = [0, 2, 4, 6, 8, 10, 12, 14, 16]
h = [1, 3, 5, 7, 9, 11, 13, 15, 17]



class Level1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Изображения/1.png")
        self.rect = self.image.get_rect()
        if window is True:
            self.rect.center = (990 - 400, 540)
        else:
            self.rect.center = (bk_w / 2 - 400, bk_h / 2)

    def update(self, *args):
        global Menu, InLevel_1
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            InLevel_1 = True
            Menu = False


class Level2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Изображения/2.png")
        self.rect = self.image.get_rect()
        if window is True:
            self.rect.center = (990 - 200, 540)
        else:
            self.rect.center = (bk_w / 2 - 200, bk_h / 2)

    def update(self, *args):
        global Menu, InLevel_2
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            InLevel_2 = True
            Menu = False


class Level3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Изображения/3.png")
        self.rect = self.image.get_rect()
        if window is True:
            self.rect.center = (990, 540)
        else:
            self.rect.center = (bk_w / 2, bk_h / 2)

    def update(self, *args):
        global Menu, InLevel_3
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            InLevel_3 = True
            Menu = False


class Level4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Изображения/4.png")
        self.rect = self.image.get_rect()
        if window is True:
            self.rect.center = (990 + 200, 540)
        else:
            self.rect.center = (bk_w / 2 + 200, bk_h / 2)

    def update(self, *args):
        global Menu, InLevel_4
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            InLevel_4 = True
            Menu = False


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
        self.imageload = pygame.image.load("Изображения/Rat-PNG-Picture.png")
        self.image = p.transform.smoothscale(self.imageload, (100, 100))
        self.color = self.image.get_at((0, 0))
        self.image.set_colorkey(self.color)
        self.rect = self.image.get_rect()
        ran = random.choice(w)
        self.rect.center = (spisok[ran], spisok[ran + 1])

    def update(self, *args):
        global Point
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            Point += 1
            pygame.mixer.music.load("zvuk-vyibivaniya-monetyi-iz-igryi-super-mario-30119.mp3")
            pygame.mixer.music.play(0, 1, 0)
            self.kill()


class Back(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.back = pygame.image.load("Изображения/233-2338375_go-back-icon-png-transparent-png.png")
        self.back_transform = p.transform.smoothscale(self.back, (50, 50))
        self.color = self.back_transform.get_at((0, 0))
        self.back_transform.set_colorkey(self.color)
        self.image = self.back_transform
        self.rect = self.image.get_rect()
        if InLevel_5 is True:
            self.rect.center = (bk_w - 30, bk_h - 30)

    def update(self, *args):
        global Menu, InLevel_5, InLevel_4, InLevel_3, InLevel_2, InLevel_1, Point
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            InLevel_5 = False
            InLevel_4 = False
            InLevel_3 = False
            InLevel_2 = False
            InLevel_1 = False
            Menu = True
            Point = 0

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.bottomright = (x, y)
    surf.blit(text_surface, text_rect)


def screen_setting(bk_w, bk_h):
    global window, ran, ran2
    window = False
    screen = p.display.set_mode((bk_w, bk_h), 0)
    p.display.set_caption('Поймай крысу')  # название окна
    p.display.set_icon(pygame.image.load("Изображения/icon.png"))  # ставим иконку крысы для окна
    bk_orig = p.image.load("Изображения/Phon.jpg").convert()
    bg_orig5 = p.image.load("Изображения/5_level_bg2.0.png").convert()
    bg_orig4 = p.image.load("Изображения/4_level_bg2.0.png").convert()
    bg_orig3 = p.image.load("Изображения/3_level_bg2.0.png").convert()
    bg_orig2 = p.image.load("Изображения/2_level_bg2.0.png").convert()
    bg_orig1 = p.image.load("Изображения/1_level_bg2.0.png").convert()
    mouse_image = p.image.load("Изображения/2534908.png").convert()
    mouse_image_transform = p.transform.smoothscale(mouse_image, (30, 30))
    color = mouse_image_transform.get_at((0, 0))
    mouse_image_transform.set_colorkey(color)
    pygame.mouse.set_visible(False)
    bg = p.transform.smoothscale(bk_orig, (bk_w, bk_h))
    bg5 = p.transform.smoothscale(bg_orig5, (bk_w, bk_h))
    bg4 = p.transform.smoothscale(bg_orig4, (bk_w, bk_h))
    bg3 = p.transform.smoothscale(bg_orig3, (bk_w, bk_h))
    bg2 = p.transform.smoothscale(bg_orig2, (bk_w, bk_h))
    bg1 = p.transform.smoothscale(bg_orig1, (bk_w, bk_h))
    clock = p.time.Clock()
    menu_sprites = pygame.sprite.Group()
    back = Back()
    rat = Rat()
    level_sprites = p.sprite.Group(back, rat)
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
            pygame.mouse.set_visible(False)
            if seconds // otc == 0:
                otc += 1000
                c += 1
                Spawn = False
                if c % 60 == 0 and c % 420 != 0:
                    ran = random.choice(w)
                    ran2 = random.choice(h)
                    Spawn = True
                elif c % 70 == 0:
                    level_sprites.remove(rat, rat)
                    rat = Rat()
                    Spawn = False

            if Spawn:
                level_sprites.add(rat)
                level_sprites.update()
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
                draw_text(screen, str(Point), 50, 1110, 83)

                p.display.update()

            else:
                level_sprites.draw(screen)
                level_sprites.update()
                clock.tick(FPS)
                draw_text(screen, str(Point), 50, 1110, 83)
                p.display.update()

        while InLevel_4 is True:  # Здесь начинаются уровни
            ticks = pygame.time.get_ticks()
            seconds = int(ticks / 1000 % 60)
            pygame.mouse.set_visible(False)
            if seconds // otc == 0:
                otc += 1000
                c += 1
                Spawn = False
                if c % 60 == 0 and c % 660 != 0:
                    ran = random.choice(w)
                    ran2 = random.choice(h)
                    Spawn = True
                elif c % 110 == 0:
                    level_sprites.remove(rat, rat)
                    rat = Rat()
                    Spawn = False

            if Spawn:
                level_sprites.add(rat)
                level_sprites.update()
            for event in p.event.get():
                if event.type == p.QUIT:
                    sys.exit()

                level_sprites.update(event)

            screen.blit(bg4, (0, 0))

            if p.mouse.get_focused():
                level_sprites.draw(screen)
                level_sprites.update()
                x, y = pos = p.mouse.get_pos()
                screen.blit(mouse_image_transform, (x - 10, y - 15))
                clock.tick(FPS)
                draw_text(screen, str(Point), 50, 1110, 83)

                p.display.update()

            else:
                level_sprites.draw(screen)
                level_sprites.update()
                clock.tick(FPS)
                draw_text(screen, str(Point), 50, 1110, 83)
                p.display.update()

        while InLevel_3 is True:  # Здесь начинаются уровни
            ticks = pygame.time.get_ticks()
            seconds = int(ticks / 1000 % 60)
            pygame.mouse.set_visible(False)
            if seconds // otc == 0:
                otc += 1000
                c += 1
                Spawn = False
                if c % 60 == 0 and c % 180 != 0:
                    ran = random.choice(w)
                    ran2 = random.choice(h)
                    Spawn = True
                elif c % 180 == 0:
                    level_sprites.remove(rat, rat)
                    rat = Rat()
                    Spawn = False

            if Spawn:
                level_sprites.add(rat)
                level_sprites.update()
            for event in p.event.get():
                if event.type == p.QUIT:
                    sys.exit()

                level_sprites.update(event)

            screen.blit(bg3, (0, 0))

            if p.mouse.get_focused():
                level_sprites.draw(screen)
                level_sprites.update()
                x, y = pos = p.mouse.get_pos()
                screen.blit(mouse_image_transform, (x - 10, y - 15))
                clock.tick(FPS)
                draw_text(screen, str(Point), 50, 1110, 83)

                p.display.update()

            else:
                level_sprites.draw(screen)
                level_sprites.update()
                clock.tick(FPS)
                draw_text(screen, str(Point), 50, 1110, 83)
                p.display.update()

        while InLevel_2 is True:  # Здесь начинаются уровни
            ticks = pygame.time.get_ticks()
            seconds = int(ticks / 1000 % 60)
            pygame.mouse.set_visible(False)
            if seconds // otc == 0:
                otc += 1000
                c += 1
                Spawn = False
                if c % 60 == 0 and c % 240 != 0:
                    ran = random.choice(w)
                    ran2 = random.choice(h)
                    Spawn = True
                elif c % 240 == 0:
                    level_sprites.remove(rat, rat)
                    rat = Rat()
                    Spawn = False

            if Spawn:
                level_sprites.add(rat)
                level_sprites.update()
            for event in p.event.get():
                if event.type == p.QUIT:
                    sys.exit()

                level_sprites.update(event)

            screen.blit(bg2, (0, 0))

            if p.mouse.get_focused():
                level_sprites.draw(screen)
                level_sprites.update()
                x, y = pos = p.mouse.get_pos()
                screen.blit(mouse_image_transform, (x - 10, y - 15))
                clock.tick(FPS)
                draw_text(screen, str(Point), 50, 1110, 83)

                p.display.update()

            else:
                level_sprites.draw(screen)
                level_sprites.update()
                clock.tick(FPS)
                draw_text(screen, str(Point), 50, 1110, 83)
                p.display.update()

        while InLevel_1 is True:  # Здесь начинаются уровни
            ticks = pygame.time.get_ticks()
            seconds = int(ticks / 1000 % 60)
            pygame.mouse.set_visible(False)
            if seconds // otc == 0:
                otc += 1000
                c += 1
                Spawn = False
                if c % 120 == 0 and c % 600 != 0:
                    ran = random.choice(w)
                    ran2 = random.choice(h)
                    Spawn = True
                elif c % 300 == 0:
                    level_sprites.remove(rat, rat)
                    rat = Rat()
                    Spawn = False

            if Spawn:
                level_sprites.add(rat)
                level_sprites.update()
            for event in p.event.get():
                if event.type == p.QUIT:
                    sys.exit()

                level_sprites.update(event)

            screen.blit(bg1, (0, 0))

            if p.mouse.get_focused():
                level_sprites.draw(screen)
                level_sprites.update()
                x, y = pos = p.mouse.get_pos()
                screen.blit(mouse_image_transform, (x - 10, y - 15))
                clock.tick(FPS)
                draw_text(screen, str(Point), 50, 1110, 83)
                print(Point)

                p.display.update()

            else:
                level_sprites.draw(screen)
                level_sprites.update()
                clock.tick(FPS)
                draw_text(screen, str(Point), 50, 1110, 83)
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

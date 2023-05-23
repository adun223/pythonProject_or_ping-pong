import sys
import pygame as pg

w = 1280
h = 720
FPS = 60
clock = pg.time.Clock()

pg.init()  # инициализируем pygame
screen = pg.displya.set_mode((w, h))
pg.display.set_caption('Ping Pong | PyGame')  # создаем экран игры разрешением 1280х720px

while True:  # цикл игры
    clock.tick(FPS)
    for event in pg.event.get():  # обработчик событий pygame
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

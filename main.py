import sys
import pygame as pg

w = 1280
h = 720
FPS = 60
clock = pg.time.Clock()


GRAY = (230, 230, 230)
WHITE = (255, 255, 255)
VIOLET = (230, 61, 243)

player = pg.Rect(w - 20, h // 2, 10, 150)
opponent = pg.Rect(10, h // 2, 10, 150)
ball = pg.Rect(w // 2 - 15, h // 2 - 15, 30, 30)

pg.init()  # инициализируем pygame
screen = pg.display.set_mode((w, h))
pg.display.set_caption('Ping Pong | PyGame')  # создаем экран игры разрешением 1280х720px

while True:  # цикл игры
    clock.tick(FPS)
    for event in pg.event.get():  # обработчик событий pygame
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill(GRAY)
    pg.draw.rect(screen, VIOLET, player)
    pg.draw.rect(screen, VIOLET, opponent)
    pg.draw.aaline(screen, WHITE, [w // 2, 0], [w // 2, h])
    pg.draw.ellipse(screen, VIOLET, ball)
    pg.display.update()

import sys
import pygame as pg



def ball_move(obj):
    global speed_x, speed_y
    obj.x += speed_x
    obj.y += speed_y

    if obj.top <=0 or obj.bottom >= h:
        speed_y *= -1
    elif obj.left <= 0 or obj.right >= w:
        speed_x *= -1
    if obj.colliderect(player) or obj.colliderect(opponent):
        speed_x *= -1


def player_motion(obj, s):
    obj.y += s

    if obj.top <= 0:
        obj.top = 0
    if obj.bottom >= h:
        obj.bottom = h


def opponent_motion(obj, p_obj, s):
    if obj.top < p_obj.y:
        obj.y += s
    elif obj.bottom > p_obj.y:
        obj.y -= s

    if obj.top <= 0:
        obj.top = 0
    elif obj.bottom >= h:
        obj.bottom = h


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

speed = 7
p_speed = 0
o_speed = speed
ball_moving = False
speed_x = speed_y = speed


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

    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        p_speed -= speed
    elif keys[pg.K_DOWN]:
        p_speed += speed
    else:
        p_speed = 0


    ball_move(ball)
    player_motion(player, p_speed)
    opponent_motion(opponent, ball, o_speed)

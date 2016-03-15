'''
改寫 http://www.pygame.org/docs/ref/draw.html 的範例
'''

import pygame
from math import pi

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

going = True
screen = None
clock = None
font = None

def main():
    pygame.init()
    init()

    while going:
        update()
        draw()
        clock.tick(60)

    pygame.quit()


def init():
    global screen, clock, font
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("標題")
    clock = pygame.time.Clock()
    font = pygame.font.Font(r"C:\Windows\Fonts\consola.ttf", 24)


def update():
    global going
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            going = False


def draw():
    global screen, clock, font

    screen.fill((255, 255, 255))
    screen.blit(font.render("FPS: {0:.2F}".format(clock.get_fps()), True, BLACK), (10, 10))

    # 矩形
    # [x1, y1, w, h]
    pygame.draw.rect(screen, BLACK, [75, 50, 50, 150], 5)

    # 矩形(填滿)
    pygame.draw.rect(screen, BLACK, [130, 50, 50, 150], 0)

    # 圓形
    pygame.draw.circle(screen, BLUE, [60, 250], 40)
    pygame.draw.circle(screen, BLUE, [150, 250], 40, 5)

    # 橢圓
    pygame.draw.ellipse(screen, RED, [225, 100, 100, 50], 5)

    # 弧線
    rest = [200, 200, 150, 125]
    pygame.draw.arc(screen, BLACK, rest, 0, pi/2, 2)
    pygame.draw.arc(screen, GREEN, rest, pi/2, pi, 2)
    pygame.draw.arc(screen, BLUE,  rest, pi, 3*pi/2, 2)
    pygame.draw.arc(screen, RED,   rest, 3*pi/2, 2*pi, 2)

    # 多邊形
    pygame.draw.polygon(screen, RED, [[100, 300], [0, 400], [200, 400]], 5)

    # 線
    pygame.draw.line(screen, GREEN, [300, 50], [350, 80], 5)

    # 更多線
    # {3}: closed
    pygame.draw.lines(screen, BLACK, False, [[210, 400], [260, 450], [410, 450], [430, 400]], 5)

    # 圖片


    pygame.display.update()

if __name__ == '__main__':
    main()

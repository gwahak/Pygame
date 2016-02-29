import pygame

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

    screen.fill((0, 0, 0))
    screen.blit(font.render("FPS: {0:.2F}".format(clock.get_fps()), True, (255, 255, 255)), (10, 10))

    # 矩形
    # [x1, y1, w, h]
    pygame.draw.rect(screen, WHITE, [75, 50, 50, 150], 5)

    # 矩形(填滿)
    pygame.draw.rect(screen, WHITE, [130, 50, 50, 150], 0)

    # 圓形
    pygame.draw.circle(screen, BLUE, [60, 250], 40)
    pygame.draw.circle(screen, BLUE, [150, 250], 40, 5)

    pygame.display.update()

if __name__ == '__main__':
    main()

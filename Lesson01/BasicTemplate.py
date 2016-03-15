import pygame

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
    pygame.display.update()

if __name__ == '__main__':
    main()

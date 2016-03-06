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

grid = [
    'OXO',
    ' OX',
    '   '
]

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

    pygame.draw.line(screen, BLACK, [50, 70 + 150 + 2.5], [50 + 150 * 3 + 10, 70 + 150 + 2.5], 5)
    pygame.draw.line(screen, BLACK, [50, 70 + 150 + 5 + 150 + 2.5], [50 + 150 * 3 + 10,  70 + 150 + 5 + 150 + 2.5], 5)
    pygame.draw.line(screen, BLACK, [50 + 150 + 2.5, 70], [50 + 150 + 2.5, 70 + 150 * 3 + 10], 5)
    pygame.draw.line(screen, BLACK, [50 + 150 * 2 + 5 + 2.5, 70], [50 + 150 * 2 + 5 + 2.5, 70 + 150 * 3 + 10], 5)

    startX = 50
    startY = 70
    for r in range(3):
        for c in range(3):
            cell = grid[r][c]
            posX = startX + c * (150 + 5) + (150 + 5) // 2
            posY = startY + r * (150 + 5) + (150 + 5) // 2
            if cell == 'O':
                pygame.draw.circle(screen, BLACK, [posX, posY], 70, 5)
            elif cell == 'X':
                pygame.draw.line(screen, BLACK, [posX - 70, posY - 70], [posX + 70, posY + 70], 5)
                pygame.draw.line(screen, BLACK, [posX - 70, posY + 70], [posX + 70, posY - 70], 5)


    pygame.display.update()

if __name__ == '__main__':
    main()

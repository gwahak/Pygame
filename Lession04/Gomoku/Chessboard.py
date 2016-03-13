import pygame


class Chessboard:

    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self, screen):
        startX, startY = 30, 50
        grid_size = 25

        pygame.draw.rect(screen, (185, 122, 87),
                         [startX - 15, startY - 15,
                          (19 - 1) * grid_size + 30, (19 - 1) * grid_size + 30], 0)

        for r in range(19):
            y = startY + r * grid_size
            pygame.draw.line(screen, (0, 0, 0), [startX, y], [startX + grid_size * (19 - 1), y], 2)

        for c in range(19):
            x = startX + c * grid_size
            pygame.draw.line(screen, (0, 0, 0), [x, startY], [x, startY + grid_size * (19 - 1)], 2)

import pygame


class Chessboard:

    def __init__(self):
        self.grid_size = 25


    def draw(self, screen):
        startX, startY = 30, 50

        pygame.draw.rect(screen, (185, 122, 87),
                         [startX - 15, startY - 15,
                          (19 - 1) * self.grid_size + 30, (19 - 1) * self.grid_size + 30], 0)

        for r in range(19):
            y = startY + r * self.grid_size
            pygame.draw.line(screen, (0, 0, 0), [startX, y], [startX + self.grid_size * (19 - 1), y], 2)

        for c in range(19):
            x = startX + c * self.grid_size
            pygame.draw.line(screen, (0, 0, 0), [x, startY], [x, startY + self.grid_size * (19 - 1)], 2)

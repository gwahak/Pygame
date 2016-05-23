import pygame

from Lesson07.Chessboard import Chessboard


class ChessboardClient(Chessboard):

    def __init__(self):
        super().__init__()

        self.grid_size = 26
        self.start_x, self.start_y = 30, 50
        self.edge_size = self.grid_size / 2

    def is_in_area(self, x, y):
        return self.start_x <= x <= self.start_x + self.get_size() and \
               self.start_y <= y <= self.start_y + self.get_size()

    def get_size(self):
        return (self.grid_count - 1) * self.grid_size + self.edge_size * 2

    def get_r_c(self, x, y):
        origin_x = self.start_x - self.edge_size
        origin_y = self.start_y - self.edge_size
        x -= origin_x
        y -= origin_y
        r = int(y // self.grid_size)
        c = int(x // self.grid_size)
        return r, c

    def draw(self, screen):
        # 棋盤底色
        pygame.draw.rect(screen, (185, 122, 87),
                         [self.start_x - self.edge_size, self.start_y - self.edge_size,
                          (self.grid_count - 1) * self.grid_size + self.edge_size * 2,
                          (self.grid_count - 1) * self.grid_size + self.edge_size * 2], 0)

        for r in range(self.grid_count):
            y = self.start_y + r * self.grid_size
            pygame.draw.line(screen, (0, 0, 0), [self.start_x, y],
                             [self.start_x + self.grid_size * (self.grid_count - 1), y], 2)

        for c in range(self.grid_count):
            x = self.start_x + c * self.grid_size
            pygame.draw.line(screen, (0, 0, 0), [x, self.start_y],
                             [x, self.start_y + self.grid_size * (self.grid_count - 1)], 2)

        for r in range(self.grid_count):
            for c in range(self.grid_count):
                piece = self.grid[r][c]
                if piece != '.':
                    if piece == 'b':
                        color = (0, 0, 0)
                    else:
                        color = (255, 255, 255)

                    x = self.start_x + c * self.grid_size
                    y = self.start_y + r * self.grid_size
                    pygame.draw.circle(screen, color, [x, y], self.grid_size // 2)

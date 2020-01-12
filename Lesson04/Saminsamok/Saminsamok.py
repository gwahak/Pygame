import pygame

from Chessboard import Chessboard


class Saminsamok():

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("三人四子棋")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(r"C:\Windows\Fonts\consola.ttf", 24)
        self.going = True

        self.chessboard = Chessboard()
        self.colorname= {'b':"Black", 'w':"White", 'r':"Red"}
    def loop(self):
        while self.going:
            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()

    def update(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.going = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                self.chessboard.handle_key_event(e)

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.font.render("FPS: {0:.2F}".format(self.clock.get_fps()), True, (0, 0, 0)), (10, 10))

        self.chessboard.draw(self.screen)
        if self.chessboard.game_over:
            self.screen.blit(self.font.render("{0} Win".format(self.colordict[self.chessboard.winner]), True, (0, 0, 0)), (500, 10))

        pygame.display.update()


if __name__ == '__main__':
    game = Saminsamok()
    game.loop()

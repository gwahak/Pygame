import pygame

from Lesson07.GomokuClient.ChessboardClient import ChessboardClient


class GomokuClient():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("多人連線五子棋")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(r"C:\Windows\Fonts\consola.ttf", 24)
        self.going = True
        # 遊戲狀態
        # wait: 等待連線
        # wait_game: 等待遊戲開始
        # gaming: 遊戲進行中
        # game_over: 遊戲結束
        self.status = "wait"

        self.chessboard = ChessboardClient()

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
                # TODO: 計算座標，檢查是否可以下子，在送出封包
                pass

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.font.render("FPS: {0:.2F}".format(self.clock.get_fps()), True, (0, 0, 0)), (10, 10))

        self.chessboard.draw(self.screen)
        if self.chessboard.game_over:
            self.screen.blit(
                self.font.render("{0} Win".format("Black" if self.chessboard.winner == 'b' else "White"), True,
                                 (0, 0, 0)), (500, 10))

        pygame.display.update()


if __name__ == '__main__':
    game = GomokuClient()
    game.loop()

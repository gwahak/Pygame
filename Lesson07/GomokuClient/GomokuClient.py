from queue import Queue

import pygame

from Lesson07.GomokuClient.ChessboardClient import ChessboardClient

message_queue = Queue()


class GomokuClient:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("多人連線五子棋")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(r"C:\Windows\Fonts\SimHei.ttf", 24)
        self.going = True
        # 遊戲狀態
        # start_connect: 開始連線
        # wait_connect: 連線中...
        # wait_game: 等待遊戲開始
        # gaming: 遊戲進行中
        # game_over: 遊戲結束
        self.status = "start_connect"

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

        # 檢查 Queue
        # 有的話取一個來處理

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.font.render("FPS: {0:.2F}".format(self.clock.get_fps()), True, (0, 0, 0)), (10, 10))

        self.chessboard.draw(self.screen)
        if self.chessboard.game_over:
            self.screen.blit(
                self.font.render("{0} Win".format("Black" if self.chessboard.winner == 'b' else "White"), True,
                                 (0, 0, 0)), (600, 10))

        status_text = self.status
        if self.status == 'start_connect':
            status_text = '開始連線'
        elif self.status == 'wait_connect':
            status_text = '連線中...'
        elif self.status == 'wait_game':
            status_text = '等待遊戲開始'
        elif self.status == 'gaming':
            status_text = '遊戲進行中'
        elif self.status == 'game_over':
            status_text = '遊戲結束'

        self.screen.blit(self.font.render(status_text, True, (0, 0, 0)), (600, 40))

        pygame.display.update()


if __name__ == '__main__':
    game = GomokuClient()
    game.loop()

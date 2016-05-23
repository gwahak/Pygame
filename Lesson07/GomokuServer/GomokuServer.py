import socket
import threading
from queue import Queue

from Lesson07.Chessboard import Chessboard

message_queue = Queue()
status = None


def receive_message(client_socket):
    """接收玩家傳送的訊息"""
    while True:
        message = client_socket.recv(1024)
        if message == b'':
            break

        if status == 'game_start':
            print(message)
            message_queue.put(message)

    # 向queue發送連線中斷通知
    # TODO


def main():
    global status

    # 初始化 server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 23000))
    server_socket.listen(5)

    # 等待兩位玩家連線
    # 預設是0號玩家執黑子，1號玩家執白子
    players = []
    while len(players) < 2:
        (client_socket, address) = server_socket.accept()

        # 告知玩家連線成功，並告訴玩家執哪一子
        msg = client_socket.recv(1024)
        if msg == b'join_game':
            players.append(client_socket)
            if len(players) == 1:
                client_socket.send(b'0b')
            else:
                client_socket.send(b'0w')

            threading.Thread(target=receive_message, args=(client_socket,)).start()

    # 初始化棋盤
    # 變更遊戲狀態 -> 對戰中
    # 告知玩家開始遊戲
    # TODO
    board = Chessboard()
    status = 'game_start'
    players[0].send(b'1game_start')
    players[1].send(b'1game_start')

    # 不斷從 Queue 接收玩家下子的要求
    # 並發出更新到所有玩家
    while True:
        job = message_queue.get()

        if job[0] == ord('3'):
            pos_msg = job[1:].decode("utf-8")
            r, c = pos_msg.split(',')
            r = int(r)
            c = int(c)

            if board.set_piece(r, c):
                players[0].send(job)
                players[1].send(job)

if __name__ == '__main__':
    main()

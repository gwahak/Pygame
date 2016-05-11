import socket
import threading


def recv_message(clientsocket):
    while True:
        message = clientsocket.recv(1024)

        if message == b'':
            break

        print()
        print(message.decode('utf-8'))
    print('連線中斷')


def main():
    nickname = input('請輸入您的暱稱：')

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 23000))

    s.send(str.encode(nickname))

    threading.Thread(target=recv_message, args=(s,)).start()

    while True:
        message = input()

        if message == 'quit':
            break
        s.send(str.encode(message))

    s.shutdown(socket.SHUT_RDWR)
    s.close()


if __name__ == '__main__':
    main()

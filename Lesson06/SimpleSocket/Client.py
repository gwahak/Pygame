import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 23000))

msg = s.recv(50)
print(msg.decode('utf-8'))
s.close()

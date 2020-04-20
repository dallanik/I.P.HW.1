import socket

sock = socket.socket()
sock.connect(('localhost', 123))

data = sock.recv(1024)
sock.close()

print(data.decode("utf-8"))
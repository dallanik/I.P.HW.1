import socket
import Timechanger

with open("config.txt") as file:
    const = int(file.readline())
sock = socket.socket()
sock.bind(("", 123))
while True:
    sock.listen(1)
    conn, addr = sock.accept()
    byte_time = bytes(str(Timechanger.change_time(const)), "utf-8")
    conn.send(byte_time)
    conn.close()

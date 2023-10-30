import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.23.247", 6000))
s.send("Привет".encode('utf-8'))
s.close()
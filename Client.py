# Python chat application client

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('0.0.0.0', 8080))

try:
    while True:
        s.send(bytes(input(), encoding='utf8'))
except:
    s.close()

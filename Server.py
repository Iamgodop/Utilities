# Python chat application server

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 8080))
s.listen(10)

try:
    while True:
        (client, address) = s.accept()
        x = s.recv(100)
        print(x)
except Exception as e:
    print(e)
    s.close()
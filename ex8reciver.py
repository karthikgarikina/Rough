import socket
import random
import time

s = socket.socket()
s.connect(("localhost", 8020))

while True:
    msg = s.recv(1).decode()
    if not msg:
        break
    print("Received -->", msg)
    x = int(msg)
    time.sleep(random.uniform(0.5, 1.5))  # small delay to look realistic
    if x == 0:
        x = 1
        s.send(str(x).encode())
    else:
        x = 0
        s.send(str(x).encode())
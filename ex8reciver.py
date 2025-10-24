# ex8_receiver.py
# -------------------------
# Receiver side of Stop and Wait Protocol

import socket

# 1️⃣ Create a socket for communication
s = socket.socket()

# 2️⃣ Connect to sender (server)
s.connect(("localhost", 8021))   # use same port in sender

print("Receiver ready...\n")

# 3️⃣ Continuously receive and acknowledge frames
while True:
    msg = s.recv(1).decode()     # receive one frame
    if not msg:
        break                    # exit if no message received
    print("Received -->", msg)

    x = int(msg)
    # Alternate ACK between 0 and 1
    if x == 0:
        x = 1
    else:
        x = 0

    # Send acknowledgment back to sender
    s.send(str(x).encode())

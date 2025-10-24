# ex8_sender.py
# -------------------------
# Sender side of Stop and Wait Protocol

import socket
import time
import random

# 1️⃣ Create a socket (server)
s = socket.socket()

# Allow immediate reuse of same port after program ends
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 2️⃣ Bind to localhost and port (use same port as receiver)
s.bind(("localhost", 8021))
s.listen(1)

print("Waiting for receiver to connect...")
c, adr = s.accept()
print("Connection to", adr, "established.\n")

# 3️⃣ Take total number of frames from user
a = int(input("Enter total number of frames: "))
x = 0

# 4️⃣ Send first frame
print("Sending -->", x)
c.send(str(x).encode())

# 5️⃣ Continue sending until all frames are sent
while a > 1:
    timer = 5                # maximum wait time
    t = random.randint(1, 7) # random delay simulation
    msg = c.recv(1).decode() # receive ACK

    if timer > t:
        time.sleep(2)
        print("ACK -->", msg)
        x = int(msg)
        print("Sending -->", x)
        c.send(str(x).encode())
    else:
        time.sleep(2)
        print("Timeout")
        print("Sending again -->", x)
        c.send(str(x).encode())
        a = a + 1  # resend frame
    a = a - 1

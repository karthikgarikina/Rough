import socket
import time
import random

# Create TCP socket
s = socket.socket()
s.bind(("localhost", 8020))
s.listen(1)
print("Waiting for receiver to connect...")

c, adr = s.accept()
print("Connection established with", adr)

a = int(input("Enter total number of frames: "))
x = 0
print("sending -->", x)
c.send(str(x).encode())

while a > 1:
    timer = 5
    t = random.randint(1, 7)
    try:
        msg = c.recv(1).decode()
    except:
        msg = ''
    
    if not msg:
        print("No ACK received... (simulating loss)")
        msg = str(x)

    if timer > t:
        time.sleep(1)
        print("ack-->", msg)
        x = int(msg)
        print("sending -->", str(x))
        c.send(str(x).encode())
    else:
        time.sleep(1)
        print("timeout")
        print("sending again-->", x)
        c.send(str(x).encode())
        a = a + 1  # retransmit same frame
    
    a = a - 1

print("All frames sent successfully.")
c.close()
s.close()

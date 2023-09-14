import socket
from threading import Thread,Barrier
barrier=Barrier(2)
c = socket.socket()
print("socket created")

c.bind(("localhost", 999))
c.listen(1)
print("waiting for connections")
s, addr = c.accept()
print("connected with", addr)
msg_count = int(input("Enter the no of msgs : "))
s.send(bytes(str(msg_count), "utf-8"))
def chat(name):
    count = 1
    while count <= msg_count:
        if name == "sender":
            msg = f"msg {count}"
            s.send(bytes(msg, "utf-8"))
            print("msg send: ",msg)

        elif name == "receiver":
            reply = s.recv(1024).decode()
            print("reply received:",reply)

        count = count + 1
        barrier.wait()

sender = Thread(target=chat,args=("sender",))
receiver = Thread(target=chat,args=("receiver",))
sender.start()
receiver.start()





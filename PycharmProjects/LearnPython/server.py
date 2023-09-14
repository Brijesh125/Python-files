import socket
from threading import Thread,Barrier
barrier=Barrier(2)
s = socket.socket()
s.connect(("localhost",999))
reply_count = int(s.recv(1024).decode())
def chat(name):
    count = 1
    while count <= reply_count:
        if name == "receiver":
            msg = s.recv(1024).decode()
            if count < reply_count:
                print("msg received:",msg)

        elif name == "sender":
            reply = f"reply {count}"
            s.send(bytes(reply, "utf-8"))
            print("reply send: ",reply)

        count = count + 1
        barrier.wait()

receiver = Thread(target=chat,args=("receiver",))
sender = Thread(target=chat,args=("sender",))
msg = s.recv(1024).decode()
if msg:
    print("msg received :", msg)
    receiver.start()
    sender.start()


import socket

app2 = socket.socket()
app2.connect(("localhost",9999))
msg = app2.recv(1024).decode()
if msg:
    reply = ""
    for i in range(5):
        reply = reply+f"reply {i}\n"
    app2.send(bytes(reply, "utf-8"))
    print(msg)
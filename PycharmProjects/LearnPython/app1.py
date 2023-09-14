import socket

app1 = socket.socket()
print("socket created")

app1.bind(("localhost",9999))
app1.listen(1)
print("waiting for connections")

while True:
    app2,addr = app1.accept()
    print("connected with",addr)
    msg = ""
    for i in range(5):
        msg = msg + f"msg {i}\n"
    app2.send(bytes(msg, "utf-8"))
    reply = app2.recv(1024).decode()
    print(reply)
    app2.close()

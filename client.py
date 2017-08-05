import  socket

ip_port = ('localhost',50008)
client = socket.socket()
client.connect(ip_port)

client.send("hello,world!")
while True:
    cli_recv = client.recv(2048)
    print cli_recv
    requery = raw_input(">>: ").strip()
    client.send(requery)


client.close()


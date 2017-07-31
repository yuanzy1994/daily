import socket

server = socket.socket()
server.bind(('localhost',9999))
server.listen(5)


while True:
    print "Waiting connect ..."
    conn,addr = server.accept()
    print "addr:",addr
    print "Client Connect!"
    while True:
        data = conn.recv(1024)
        print "Received message:",data
        conn.send(data.upper())

server.close()
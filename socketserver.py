import SocketServer

class Mysoc(SocketServer.BaseRequestHandler):


    def handle(self):
        while True:
            print "New_client:",self.client_address
            data = self.request.recv(1024)
            print "Client Echo:",data.decode()
            self.request.send(data)


if __name__ == '__main__':
    Host, Port = 'localhost', 50008
    server = SocketServer.ThreadingTCPServer((Host,Port),Mysoc)

    server.serve_forever()


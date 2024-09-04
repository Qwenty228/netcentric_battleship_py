import socket
import json


class Network:
    def __init__(self, name="john doe") -> None:
        # AF_INET = IPv4, SOCK_STREAM = TCP
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = self.server, self.port = 'localhost', 55555
        self.player = self.connect(name)
        print(self.player)

    def connect(self, name):
        try:
            self.client.connect(self.addr)
            server_reply = json.loads(self.client.recv(2048))
            rep = self.send({"type": "init", "client": server_reply, "ships": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"], "name": name})
            print(rep)
            return server_reply
        except socket.error as e:
            print(str(e))

    def send(self, data):
        try:
            self.client.send(json.dumps(data).encode("utf-8"))
            return json.loads(self.client.recv(2048))
        except socket.error as e:
            print(str(e))


    
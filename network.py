import socket
import json


class Network:
    def __init__(self) -> None:
        # AF_INET = IPv4, SOCK_STREAM = TCP
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = self.server, self.port = 'localhost', 55555
        self.player = self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            return json.loads(self.client.recv(2048))
        except socket.error as e:
            print(str(e))

    def send(self, data):
        try:
            self.client.send(json.dumps(data))
            return json.loads(self.client.recv(2048))
        except socket.error as e:
            print(str(e))


    
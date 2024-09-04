# battle ship command line game
from network import Network
import time
import json


class Battleship:
    def __init__(self) -> None:
        self.client = Network() # game state init to server


    def start(self):
        while True:
            if self.client.ready:
                reply = self.client.send({"type": "game", "pos": input("Enter a position: ")})
                print(reply)

            else:
                print("Waiting for player to connect")
                self.client.ready = json.loads(self.client.receive())['ready'] # blocking A, wait until B connects

                
                
if __name__ == "__main__":
    Battleship().start()
# battle ship command line game
from network import Network


class Battleship:
    def __init__(self) -> None:
        self.client = Network() # game state init to server


    def start(self):
        while True:
            reply = self.client.send({"type": "game", "pos": input("Enter a position: ")})
            print(reply)


if __name__ == "__main__":
    Battleship().start()
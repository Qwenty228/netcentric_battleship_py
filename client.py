# battle ship command line game
from network import Network
import random
import json


class Battleship:
    def __init__(self, username: str = "") -> None:
        self.network = Network({"header": "init", "body": [str(i) for i in random.sample(range(64), 16)], "client": username}) # game state init to server     
        self.player_index = 1 if self.network.client_id == "A" else 0
        
    def game(self):
        # get round from server
        game_round = int(self.network.send({"header": "game", "body": "round"})['body'])

        print("Round:", game_round)
        if game_round % 2 == self.player_index:  # if round is odd, A plays, if round is even, B plays
            reply = self.network.send({"header": "game", "body": input("Enter a position: ")})
        else:
            # wait for opponent to play
            print("Waiting for opponent to play")
            reply = self.network.receive()
   
        print(reply)  # print game state
        # process game state and prepare for next round

    def start(self):
        while True:
            if self.network.ready:
                self.game()
            else:
                print("Waiting for player to connect")
                self.network.ready = json.loads(self.network.receive())['body'] # blocking A, wait until B connects
                print("Player connected")
                
                
if __name__ == "__main__":
    Battleship().start()
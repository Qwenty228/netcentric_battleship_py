# battle ship command line game
from network import Network
import time
import json


class Battleship:
    def __init__(self) -> None:
        self.client = Network() # game state init to server     
        self.player_index = 1 if self.client.player['client'] == "A" else 0


    def game(self):
        # get round from server
        game_round = int(self.client.send({"type": "game", "round": 0})['round'])

        print("Round:", game_round)
        if game_round % 2 == self.player_index:  # if round is odd, A plays, if round is even, B plays
            reply = self.client.send({"type": "game", "pos": input("Enter a position: ")})
        else:
            # wait for opponent to play
            print("Waiting for opponent to play")
            reply = self.client.receive()
   
        print(reply)  # print game state
        # process game state and prepare for next round

    def start(self):
        while True:
            if self.client.ready:
                self.game()
            else:
                print("Waiting for player to connect")
                self.client.ready = json.loads(self.client.receive())['ready'] # blocking A, wait until B connects
                print("Player connected")
                
                
if __name__ == "__main__":
    Battleship().start()
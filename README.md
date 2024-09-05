# 2190472 Netcentric: Project Battleship

Welcome to the **Battleship** project for the course **2190472 Netcentric**. This project implements a multiplayer version of the classic Battleship game using Python's socket library, allowing two players to play against each other via the command-line interface (CLI).


## Overview
The Battleship project simulates the classic board game, where two players position ships on a grid and attempt to sink each other's fleet. The game runs over a network, with one player acting as the server and the other as the client. Communication between the players is handled using **Python sockets**, making it a fully networked experience.

## Features
- **Multiplayer:** Two players can compete over a network.
- **Turn-Based Gameplay:** Players take turns attacking each other's grid.
- **CLI-based Gameplay:** Easy-to-use command-line interface for both the server and the client.
- **Socket Communication:** Uses TCP sockets to handle game state and communication between players.

## Project Structure

```
netcentric_battleship_py/
│
├── server.py         # Server-side script for hosting the game and game logic
├── client.py         # Client turnbase game loop
├── network.py        # Client-side script for connecting to a game
```


- **`server.py`**: Hosts the game. This script waits for a client to connect and initiates the game once both players are ready.
- **`client.py`**: Connects to the server. After connecting, the client can play the game, sending and receiving moves via the network.
- **`network.py`**: Communication handler for client init.

## Installation

### Prerequisites
- Python 3.x
- Basic understanding of networking (sockets) and Python

### Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Qwenty228/netcentric_battleship_py.git
   cd netcentric_battleship_py
   ```

2. **Install Dependencies**:
   There are no external dependencies beyond Python's standard libraries.

3. **Start the Server**:
   Open a terminal and run the server:
   ```bash
   python server.py
   ```

4. **Start the Client**:
   Open another terminal or a different machine and run the client:
   ```bash
   python client.py
   ```

5. **Start Playing!** Follow the on-screen prompts to start attacking your opponent.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


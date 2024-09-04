import socket
import json
from _thread import*
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = 'localhost'
port = 55555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server,port))
    
except socket.error as e:
    print(str(e))
    
s.listen(2)
s.settimeout(0.5)
print("Waiting for a connection")

currentId = "A"
all_clients = []
stateA = [0]*64
stateB = [0]*64   #-1 not hit #1 hit #0 no boat 
shipA = None    #send/recieve as strings.
shipB = None
game_round = 1


def threaded_client(conn):
    global currentId, pos, shipA, shipB, game_round
    
    for client in all_clients:
        client.sendall(json.dumps({"client": currentId, "ready": len(all_clients) == 2}).encode("utf-8"))

    currentId = "B"
    reply = {}
    while True:
        try:
            data = conn.recv(2048).decode('utf-8')
            if not data:
                print(currentId, "disconnected")
                break

            print("Received:",  fr'{data}')
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                continue
            
            if (data["type"] == "init"):
                if (data["client"] == "A"):
                    shipA = [int(ship) for ship in data['ships']]
                elif(data["client"] == "B"):
                    shipB = [int(ship) for ship in data['ships']]
                
            elif (data["type"] == "game"):
                if "round" in data:
                    reply = {"type": "game", "round": game_round}
                else:
                    target_pos = int(data["pos"])
                    # print(data)
                    game_round += 1
                    reply = {"type": "game", "pos": target_pos}
                    for client in all_clients:
                        if client != conn:
                            client.sendall(json.dumps(reply).encode("utf-8"))
                        
   

            conn.sendall(json.dumps(reply).encode("utf-8"))       
                    
        except socket.error as e:
            print(e)
            break
        
    print("Connection Closed")
    all_clients.remove(conn)
    conn.close()      


        
                       
                        
                        
                
                        
                        

while True:
    try:
        conn, addr = s.accept()
        all_clients.append(conn)
        print("Connected to: ", addr)
    
        start_new_thread(threaded_client, (conn,))
    except socket.timeout:
        continue

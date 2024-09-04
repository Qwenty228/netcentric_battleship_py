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

def threaded_client(conn):
    global currentId, pos, shipA, shipB
    
    conn.send(json.dumps({"client": current}).encode())
    currentId = "B"
    reply = 'funk u'
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
                        
                # elif(reply["type"] == "game"):
                #     target_pos = int(reply["pos"])
                #     reply = 0
                #     if(reply["client"] == "A" and stateB[target_pos] == 1):
                #         stateB[target_pos] == 1
                       
                #     elif(reply["client"] == "B" and stateA[target_pos] == 1):
                #         stateA[target_pos] == 1
                # elif(reply["type"] == "disconnect"):
                #     pass   

            conn.sendall(json.dumps(reply).encode("utf-8"))       
                    
        except socket.error as e:
            print(e)
            break
        
    print("Connection Closed")
    conn.close()      

        
                       
                        
                        
                
                        
                        

while True:
    try:
        conn, addr = s.accept()
        print("Connected to: ", addr)
    
        start_new_thread(threaded_client, (conn,))
    except socket.timeout:
        continue

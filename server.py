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

stateA = [0]*64
stateB = [0]*64   #-1 not hit #1 hit #0 no boat 
shipA = [0]*16    #send/recieve as strings.
shipB = [0]*16

def threaded_client(conn):
    global currentId, pos
    conn.send(str.encode(currentId))
    currentIndex = "B"
    reply = ''
    while True:
        try:
            data = conn.recv(2048)
            reply = json.loads(data)
            if not data:
                conn.send(str.encode("Goodbye"))
                break
            else:
                if (reply["type"] == "init"):
                    if (reply["client"] == "A"):
                        shipA = [1 if i in reply["ships"] else 0 for i in shipA]
                    elif(reply["client"] == "B"):
                        shipB = [1 if i in reply["ships"] else 0 for i in shipB]
                        
                # elif(reply["type"] == "game"):
                #     target_pos = int(reply["pos"])
                #     reply = 0
                #     if(reply["client"] == "A" and stateB[target_pos] == 1):
                #         stateB[target_pos] == 1
                       
                #     elif(reply["client"] == "B" and stateA[target_pos] == 1):
                #         stateA[target_pos] == 1
                # elif(reply["type"] == "disconnect"):
                #     pass   

                    
                    
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

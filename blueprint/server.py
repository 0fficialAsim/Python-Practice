import threading
import socket
import sqlite3


ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_binding = ('localhost', 9999)
ss.bind(server_binding)
ss.listen()

def start_connection(c):
    msg = "Welcome to Blueprint"
    c.send(msg.encode())

    response = c.recv(1024).decode()
    print("[S] Data recieved: " + response)

    #add more communication 
    msg2 = "Knock Knock!"
    c.send(msg2.encode())

    response2 = c.recv(1024).decode()
    print("[S] Data recieved: " + response2)

    print("Done!")

while(True):
    client, addr = ss.accept()
    t2 = threading.Thread(target=start_connection, args=(client,))
    t2.start()

    ss.close()
    exit()
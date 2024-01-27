import threading
import socket

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_binding = ("localhost", 9999)
cs.connect(server_binding)

data_from_server = cs.recv(1024)
msg = data_from_server.decode()

print("[C] Data recived: " + msg)

cs.send(input("Respond Here: ").encode())
msg2 = cs.recv(1024).decode() #Getting data from server, then decoding the mesage 

cs.send(input("Respond Here: ").encode())

#have more communication 
cs.close()
exit()
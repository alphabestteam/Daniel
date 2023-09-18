import socket

HOST = '127.0.0.1'
PORT = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

user_input = input("enter your massage")
s.send(bytes(user_input, 'utf-8'))
data = s.recv(1024)

print("The upper data:", data)




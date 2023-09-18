
import socket


HOST = '127.0.0.1'
PORT = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen()
print("listening")

while True:
    conn, addr = s.accept()
    print('Connect to', addr)
    data = conn.recv(1024)
    upper_data = data.upper()

    conn.sendall(upper_data)
    break

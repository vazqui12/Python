#!/usr/bin/env python3

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 1235)
server_socket.bind(server_address)

server_socket.listen(1)

while True: 
    
    client_socket, client_addr = server_socket.accept()
    data = client_socket.recv(1024)
    
    print(f"\n[+] Mensaje recibido por el cliente: {data.decode()}")
    print(f"\n[+] Informacion del cliente: {client_addr}")

    client_socket.sendall(f"Saludos Crack\n".encode())
    client_socket.close()



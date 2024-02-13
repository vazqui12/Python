#!/usr/bin/env python3

import socket

def start_chat_client():

    host = 'localhost'
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:

            data = input(f"\n[+] Mensaje para el server: ")
            s.sendall(data.encode())

            if data == 'bye':
                break

            server_message = s.recv(1024).strip().decode()
            print(f"\n[+] Mensaje del servidor: {server_message}")

start_chat_client()

        
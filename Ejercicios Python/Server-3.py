#!/usr/bin/env python3 

import socket

def start_chat_server():

    host = 'localhost'
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(1)
        conn, adrr = s.accept()

        print(f"\n[+] Se ha conectado el cliente: {adrr}")

        while True:
            data = conn.recv(1024).strip().decode()
            print(f"\n[+] El mensaje del cliente es: {data}")

            if data == 'bye':
                break

            server_message = input(f"\n[+] Mensaje para el cliente: ")
            conn.sendall(server_message.encode())

start_chat_server()

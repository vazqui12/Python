#!/usr/bin/env python3

import socket
import threading

class ClientThread(threading.Thread):

    def __init__(self, client_sock, client_addr):
        super().__init__()
        self.client_sock = client_sock
        self.client_addr = client_addr

        print(f"\n[+] nuevo cliente conectado: {client_addr}")

    def run(self):
        
        message = ''

        while True:
            data = self.client_sock.recv(1024)
            message = data.decode()

            if message.strip() == 'bye':
                break

            print(f"\n[+] Mensaje enviado por el cliente {message.strip()}")
            self.client_sock.send(data)

        print(f"\n[!] Cliente {self.client_addr} desconectado")
        self.client_sock.close()

HOST = 'localhost'
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    while True:
        s.listen(1)
        client_socket, client_addr = s.accept()
        new_treahd = ClientThread(client_socket, client_addr)
        new_treahd.start()

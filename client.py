#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, sys
cmd = sys.argv[1]
arg = sys.argv[2]

MAX_CONNECTIONS = 1
address_to_server = ('localhost', 8686)

clients = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(MAX_CONNECTIONS)]
for client in clients:
    client.connect(address_to_server)

for i in range(MAX_CONNECTIONS):
    clients[i].send(bytes(cmd + ' '+ arg, encoding='UTF-8'))

for client in clients:
    data = client.recv(1024)
    print(str(data.decode('UTF-8')))
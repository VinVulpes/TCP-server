import socket, sys

# Задаем адрес сервера
SERVER_ADDRESS = ('localhost', 8686)

# Настраиваем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADDRESS)
server_socket.listen(10)
number = 50 
cmd, arg = 0,0
print('server is running, please, press ctrl+c to stop')

# Слушаем запросы
while True:
    connection, address = server_socket.accept()
    print("new connection from {address}".format(address=address))

    data = connection.recv(1024)
    data = data.decode("utf-8")
    cmd_raw = data.split()
    if len(cmd_raw) == 2:
        cmd, arg = cmd_raw
    else:
        connection.send(bytes('incorect format', encoding='UTF-8'))
    if cmd == 'GUESS' and arg.isdigit():
        arg = int(arg)
        if arg > number:
            answer = 'LESS'
        elif arg < number:
            answer = 'MORE'
        else:
            answer = 'EQUAL'
        connection.send(bytes(answer, encoding='UTF-8'))
    else:
        connection.send(bytes('incorect command or arg', encoding='UTF-8'))


    connection.close()
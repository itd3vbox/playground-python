import socket

# TCP/IP Socket - Server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print('starting up on ', server_address, ' port ', server_address)
sock.bind(server_address)
sock.listen(1)

while True:
    print('Waiting for a connection ...')
    connection, client_address = sock.accept()

    try:
        print('Connection from: ', client_address)

        # RECEVE DATA
        while True:
            data = connection.recv(1000)
            print('received:\n', data.decode("utf-8"), '\n')
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no more data from', client_address)
                break
            
    finally:
        connection.close()
import socket

def server(host = '127.0.0.1', port=12345):
    data_payload = 2048 #The maximum amount of data to be received at once
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    # Enable reuse address/port 
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (host, port)
    print ("Iniciando um servidor de eco %s port %s" % server_address)
    sock.bind(server_address)
    # Listen to clients, argument specifies the max no. of queued connections
    sock.listen(5) 
    i = 0
    while True: 
        print ("Aguardando msg do cliente")
        client, address = sock.accept() 
        data = client.recv(data_payload) 
        if data:
            print ("Data: %s" %data)
            client.send(data)
            print ("sent %s bytes back to %s" % (data, address))
            # end connection
            client.close()
            i+=1
            if i>=3: break           

server()
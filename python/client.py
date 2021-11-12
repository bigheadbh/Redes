import socket

def client(host = '127.0.0.1', port=12345): 
    # Create a TCP/IP socket 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Connect the socket to the server 
    server_address = (host, port) 
    print ("Conectando no %s porta %s" % server_address) 
    sock.connect(server_address) 
    # Send data 
    try: 
        # Send data 
        message = "Mensagem de Teste. Isto sera ecoado" 
        print ("Enviando %s" % message) 
        sock.sendall(message.encode('utf-8')) 
        
        # Look for the response 
        amount_received = 0 
        amount_expected = len(message) 
        while amount_received < amount_expected: 
            data = sock.recv(64) 
            amount_received += len(data) 
            print ("Recebeu: %s" % data) 
    except socket.error as e: 
        print ("Socket error: %s" %str(e)) 
    except Exception as e: 
        print ("Other exception: %s" %str(e)) 
    finally: 
        print ("Closing connection to the server") 
        sock.close() 

client()
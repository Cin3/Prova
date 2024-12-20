import socket
def start_server():
    sock=socket.create_server(("0.0.0.0",8888))
    sock.listen()
    print("Server in ascolto su localhost")
    while True:
        client_socket, client_address = sock.accept()
        print(f"Connessione ricevuta da {client_address}")
        data = client_socket.recv(1024)
        if not data:
            print("Nessun dato ricevuto. Chiusura connessione.")
            client_socket.close()
            continue        
        print(f"Scritta ricevuta dal client: {data.decode()}")
        my_bytes=data.decode()
        my_bytes_up=my_bytes.upper()
        client_socket.send(my_bytes_up.encode())
        client_socket.close()
    
start_server()



            
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

delimeter = b'\n'


datatype = (b'card info'+delimeter)
datatostore = (b'123456789, 11/27, 875')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        s.sendall(datatype)
        s.sendall(datatostore)
        data = s.recv(1024)
    
    except Exception as e:
        print(f"An error occurred: {e}")
   
        

    
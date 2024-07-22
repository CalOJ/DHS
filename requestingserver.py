'''THIS IS AN EXAMPLE FILE TO IMITATE WHAT A ORGINIZATION WOULD REQUEST'''




import socket
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

delimeter = b'\n'

connectioncode = b'Afj3949jgj'


def encrypt():
    datatype = (b'card info'+delimeter)
    datatostore = (b'123456789, 11/27, 875')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:


        try:
            s.connect((HOST, PORT))
            s.sendall(b''+connectioncode+delimeter)
            

        except Exception as e:
            print(f"An error occurred: {e}")

        
        try:
        
            s.sendall(datatype)
            s.sendall(datatostore)
            data = s.recv(1024)
        
            print(data)
        except Exception as e:
            print(f"An error occurred: {e}")
    
            
def decrypt():
    datatype = (b'decrypt'+delimeter)
    encrytionkey = (b'MVRJIEdnj_a5wWtOyAmGA=')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:


        try:
            s.connect((HOST, PORT))
            s.sendall(b''+connectioncode+delimeter)
            

        except Exception as e:
            print(f"An error occurred: {e}")

        
        try:
        
            s.sendall(datatype)
            s.sendall(encrytionkey)
            data = s.recv(1024)
        
            print(data)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    encrypt()
    #decrypt()



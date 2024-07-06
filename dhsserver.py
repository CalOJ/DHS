import socket
import subprocess
import pickle



def server():
    HOST = '127.0.0.1'
    PORT = 65432

    delimeter = '\n'


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        conn, addr = s.accept()
        with conn:
            print(f'Established: {addr}')
            while True:
                data = conn.recv(1024)
                data = data.decode()
                if not data:
                    break
                
                else:
                    global info
                    info = data.split(delimeter)
                    print(info)
                    with open('data.pickle', 'wb') as f:
                        pickle.dump(info, f)
                    
                    subprocess.run(["python", "encryption.py"])


if __name__ =='__main__':
    server()


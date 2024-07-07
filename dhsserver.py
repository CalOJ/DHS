import socket
import subprocess
import pickle


#listens for connections
def startlisten():
    HOST = '127.0.0.1'
    PORT = 65432

    #First level of connection secuirity, verfies requesters ip adress is authorized
    authorizedusers = ['127.0.0.1','1.0.0.1.2']

    #binds host and port outside the loop because they are permenant and cannot be rebound
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    

    #server is always listening
    while True:
        s.listen()        
        global conn
        global addr

        conn, addr = s.accept()



        #checks if the ip is allowed to connect
        for i in range(len(authorizedusers)):
            if authorizedusers[i] == addr[0]:
                verification = True
                break
            else:
                verification = False


        if verification == True:
            objectname = addr[0]
            manager = server(conn, objectname)

        

            #if authorized recieves data
            manager.recievedata()
            
            #closes the connection but the loop is still listening for new ones
            manager.close_connection()

        else:
            print('unauthorized')

        

            


        


class server:

    def __init__(self, connection, name):
        self.connection = connection
        self.name = name
        self.data = b""

    def recievedata(self):
        try:
            self.data = self.connection.recv(1024)
            print(f"{self.name} received: {self.data.decode()}")
            delimeter = '\n'
        
            self.data = self.data.decode()
            global info
            self.info = self.data.split(delimeter)
            print(self.info)
            with open('data.pickle_'+str(self.name), 'wb') as f:
                pickle.dump(self.info, f)
        
            subprocess.run(["python", "encryption.py"])

        except Exception as e:
            print(f"An error occurred: {e}")
    
    
            
            

    


    def close_connection(self):
        self.connection.close()
        print(f"{self.name} connection closed")




if __name__ =='__main__':
    startlisten()


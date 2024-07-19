import socket
import subprocess
import pickle
import time
from cryptography.fernet import Fernet
import encryption
import tokengen
import emailsender


#listens for connections
def startlisten():
    HOST = '127.0.0.1'
    PORT = 65432

    #First level of connection secuirity, verfies requesters ip adress is authorized
    authorizedusers = ['127.0.0.1','1.0.0.1.2']

    #second level of connection defense
    global joincodes
    joincodes = {'127.0.0.1': 'Afj3949jgj'}

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
            storeunauth(addr)

def storeunauth(adress, attemptedcode=None):

    #checks whether ip or code is unauthorized
    if attemptedcode==None:   
        print(f'unauthorized join attempt by ip: {adress}')
        conn.sendall(b'YOU ARE NOT AUTHORIZED TO CONNECT')

        #stores unathorized join attempts
        with open('unathorized_join_attempts.txt', 'a') as f:
            f.write(str(f'Unathorized IP: {adress} attempted to connect at {time.asctime(time.gmtime())} UTC \n'))

    else:
         print(f'attempted use of {attemptedcode} as an authorization code')
         with open('unathorized_join_attempts.txt', 'a') as f:
            f.write(str(f'Authorized IP: {adress} attempted to connect with the incorrect acsess code {attemptedcode} at {time.asctime(time.gmtime())} UTC \n'))


    



        


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


            
            authcode = self.info[0]
            #checks if the joincode is correct
            if joincodes[str(self.name)] == authcode:

                
                del self.info[0]
                print(self.info)

                if 'decrypt' in self.info:
                    pass
                
                if 'card info' in self.info:

                    key = encryption.encrypt(str(self.info))
                   
                    link = tokengen.gentoken(key)
                    
                    emailsender.sendmail(link)
                   
                    self.connection.sendall(key)
                 


            #if joincode is not correct then it stores ip and attempted join code
            else:
                storeunauth(self.name, authcode)
                self.close_connection()

        except Exception as e:
            print(f"An error occurred: {e}")
    
    
            
            

    


    def close_connection(self):
        self.connection.close()
        print(f"{self.name} connection closed")




if __name__ =='__main__':
    startlisten()


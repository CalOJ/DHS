#for unpickling stored data
import pickle
import sys
# install cryptography package/lib
from cryptography.fernet import Fernet
import hashlib


# the DHS class just makes a list that will hold 'pairs' or just a hashed version of the encryption key and the
# encrypted password so that they can be found later in the list when supplied with the key
class DHS:

    def __init__(self):
        self._lst = []

    # used to encrypt a supplied password add it to the list then return the encryption key
    # Note: Fernet.encrypt and this encrypts are different methods same with decrypt
    def encrypt(self, password) -> bytes:
        # generate key
        key = Fernet.generate_key()
        # create an instance of the key
        fernet = Fernet(key)
        # encrypt the password(password has to be encoded first to work idk)
        encrypted_password = fernet.encrypt(password.encode())
        # create a new pair with hashed key and encrypted password then add it to the list
        self._lst.append(Pair(hash(key), encrypted_password))
        return key

    # decrypt and return the password
    def decrypt(self, key):
        return Fernet(key).decrypt(name.get(key)).decode()

    # gets the value at a specific key hash location
    def get(self, key):
        h = hash(key)
        for x in self._lst:
            if h == x.get_key():
                return x.get_value()


# creates a tuple of a key value pair which is then stored in the DHS class
class Pair:

    def __init__(self, key, value):
        self.pair = (key, value)

    def get_key(self):
        return self.pair[0]

    def get_value(self):
        return self.pair[1]

    def __str__(self):
        return f'{self.pair[0]}, {self.pair[1]}'



def unpickledata(name):
    with open('data.pickle_'+name, 'rb') as f:
        info = pickle.load(f)
        return str(info)


if __name__ == '__main__':
    #pulling unique data pertaining to stored information for encryption from dhsserver.py via command line
    identifier = sys.argv[1]
    name = DHS()
    key = name.encrypt(unpickledata(identifier))
    print(f"Encryption key: {key}")
    print(f"Encrypted password: {name.get(key)}")
    print(f"Decrypting password: {name.decrypt(key)}")

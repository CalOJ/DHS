import pickle
# install cryptography package/lib
from cryptography.fernet import Fernet
import hashlib
import requests


def encrypt(password) -> bytes:
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    m = hashlib.sha256()
    m.update(key)
    try:
        f = open('data', 'rb')
        dict = pickle.load(f)
        dict[str(m.hexdigest())] = encrypted_password
        f.close()
        cleared = open('data', 'wb')
        pickle.dump(dict, cleared)
    except:
        f = open('data', 'ab')
        dic = {str(m.hexdigest()): encrypted_password}
        pickle.dump(dic, f)
        f.close()
    return key


def get(key):
    f = open('data', 'rb')
    d = pickle.load(f)
    m = hashlib.sha256()
    m.update(key)
    hash_key = str(m.hexdigest())
    return d[hash_key]


def decrypt(key):
    return Fernet(key).decrypt(get(key)).decode()

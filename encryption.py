import pickle
# install cryptography package/lib
from cryptography.fernet import Fernet


def encrypt(password) -> bytes:
    # generate key
    key = Fernet.generate_key()
    # create an instance of the key
    fernet = Fernet(key)
    # encrypt the password(password has to be encoded first to work idk)
    encrypted_password = fernet.encrypt(password.encode())
    try:
        f = open('data', 'rb')
        dict = pickle.load(f)
        dict[key] = encrypted_password
        f.close()
        cleared = open('data', 'wb')
        pickle.dump(dict, cleared)
        print(file)
    except:
        f = open('data', 'ab')
        dic = {key: encrypted_password}
        pickle.dump(dic, f)
        f.close()
        return key


def get(key):
    f = open('data', 'rb')
    d = pickle.load(f)
    return d[key]


def decrypt(key):
    return Fernet(key).decrypt(get(key)).decode()


if __name__ == '__main__':
    key = encrypt(input("enter a password: "))
    file = open('data', 'rb')
    f = pickle.load(file)
    print(f'this is file: {f}')
    for keys in f:
        print(f'{keys} -> {f[keys]}')
    print(f"Encryption key: {key}")
    print(f"Encrypted password: {get(key)}")
    print(f"Decrypting password: {decrypt(key)}")

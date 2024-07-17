import random

from encryption import *

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()
count = 0
a = input("Would you like to generate new passwords? (y or n): ")
if a == 'y':
    print("generating passwords")
    f = open('data', 'w')
    f.close()
    for word in WORDS:
        # print(f'{count * 100 // len(WORDS)}%')
        key = encrypt(word.decode())
        if count == random.randint(0, 10000):
            print(f'This is a random key: {key.decode()}')
        count += 1
k = input("enter your key: ")
print("decrypting...")
print(f'This is your password: {decrypt(k.encode())}')


# key = encrypt(input("enter a password: "))
# file = open('data', 'rb')
# f = pickle.load(file)
# print(f'this is file: {f}')
# for keys in f:
#     print(f'{keys} -> {f[keys]}')
# print(f"Encryption key: {key}")
# print(f"Encrypted password: {get(key)}")
# print(f"Decrypting password: {decrypt(key)}")
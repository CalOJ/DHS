import base64
import urllib.parse


def gentoken(key):
    
    key = key.decode('utf-8')
    identify = 'ID:42453642'
    encryption_key = key+identify
    print(6)
    token = base64.urlsafe_b64encode(encryption_key.encode()).decode()

    urlbase = "http://127.0.0.1:5000/save_key"

    link = f'{urlbase}?token={urllib.parse.quote(token)}'

    return link

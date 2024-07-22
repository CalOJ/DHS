import base64
import urllib.parse


def gentoken(key):
    
    print(key)
    identify = 'ID:42453642'
    encryption_key = str(key)+'+n'+identify
    print(1)
    print(6)
    token = base64.urlsafe_b64encode(encryption_key.encode()).decode()
    print(token)
    urlbase = "http://127.0.0.1:5000/save_key"

    link = f'{urlbase}?token={urllib.parse.quote(token)}'
    print(link)
    return link



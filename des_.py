from pyDes import des, CBC, PAD_PKCS5
import binascii
from hashlib import md5
from base64 import b64encode, b64decode
from sys import exit
from time import sleep

md5_ = lambda t: md5(t.encode()).hexdigest()


def des_encrypt(s, key='password'):
    secret_key = key
    #iv = '12345678'
    iv = md5_(key)[:8]
    k = des(
        secret_key,
        CBC,
        iv,
        pad=None,
        padmode=PAD_PKCS5
    )
    en = k.encrypt(s.encode(), padmode=PAD_PKCS5)
    return binascii.b2a_hex(en).decode()


def des_descrypt(s, key='password'):
    secret_key = key
    #iv = '12345678'
    iv = md5_(key)[:8]
    k = des(
        secret_key,
        CBC,
        iv,
        pad=None,
        padmode=PAD_PKCS5
    )
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de.decode()

def rec_(s: str, st: int):
    ar = [(ord(c) + st) for c in s]
    sr = ''.join([chr(c) for c in ar])
    br = b64encode(sr.encode()).decode()
    return br

if __name__ == '__main__':
    s = 'Но он все никак не может борщ поесть, то'
    # sh_ = rec_(s, 67)
    # print(sh_)
    # print()
    # br = b64decode(sh_.encode()).decode()
    # print(br)
    # print()
    # sr = [(ord(c) - 67) for c in br]
    # ar = ''.join([chr(c) for c in sr])
    # print(ar)
    # exit()
    encry_s = des_encrypt(s)
    print('('+encry_s+')')
    descry_s = des_descrypt(
        encry_s
    )
    print(descry_s)
    print(b64decode(descry_s.encode()).decode())
    print(md5_(s)[:8])

from itertools import product
from hashlib import md5
from Crypto.Hash import MD4
import string
from time import time
from sys import exit
# Создаем список всех цифр
digits = ''
digits += string.ascii_lowercase
#digits += string.ascii_lowercase.upper()
digits += '0123456789'
#digits = 'cfgvhep'
#digits += '&#$%_-+/@*"\':;!?' 
digits += '_ !'
#digits += string.ascii_lowercase.upper()
#print(digits)

def md5_(t: str):
    return md5(
        t.encode('utf-8')
    ).hexdigest()

def ntlm_(t: str):
    return MD4.new(
        t.encode('utf-16le')
    ).hexdigest()

cint = False

#64f12cddaa88057e06a81b54e73b949b:Password1
# hash_ = 'd03b572b319e335ecd3e793412a28524'
# hash_ = ntlm_('u0_a214')
hash_ = md5_('aa0rt_')

def check_(t: str, h_: str, hf):
    if hf(t) == h_:
        return True
    print(t)
    return False

start = time()

for p in product(digits, repeat=6):
    pass_ = ''.join(p)
    if check_(pass_, hash_, md5_):
        print(f"password find: {pass_}")
        end = time()
        s = round(
            end - start, 2
        )
        print(
            f"time: {s} seconds"
        )
        break
    print(pass_)

exit()
def with_file(path_, hash_):
    with open(path_, 'r') as f:
        for pass_ in f:
            pass_ = pass_.strip()
            if check_(pass_, hash_, md5_):
                exit()
#with_file('downloads/3WiFi_WiFiKey.txt', hash_)
#with_file('Runiq.txt', hash_)
#with_file('LD.txt', hash_)
#exit()
for i in range(5, 10):
    combinations = product(digits, repeat=i)

    for combination in combinations:
        pass_ = ''.join(combination)
        pass_ = pass_[0]+pass_[1]+'_'+pass_[:-2]

        if cint:
            if pass_ != 'fcfttfat':
                continue
            else:
                cint = False
        if check_(pass_, hash_):
            exit()

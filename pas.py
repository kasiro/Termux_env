from itertools import product
from hashlib import md5
import string
from time import sleep
from sys import exit
# Создаем список всех цифр
digits = '0123456789'
#digits = string.ascii_lowercase
#digits = 'cfgvhep'
#digits += string.ascii_lowercase.upper()
#print(digits)

def md5_(t: str):
    return md5(
        t.encode('utf-8')
    ).hexdigest()

login_ = 'kasiro'
pass_ = 'C5ypted!'
#pass_ = '45105!45105!'
h_ = ''
i = 1

for l in pass_:
    h_ += md5_(
        l + md5_(
            str(ord(l))
        ) + md5_(
            login_
        ) + md5_(pass_)
    )
    i += 1

print(h_)
print('('+str(len(h_))+')')

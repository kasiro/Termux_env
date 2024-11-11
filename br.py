from itertools import product
from hashlib import md5
import string
from time import sleep
from sys import exit
# Создаем список всех цифр
digits = '0145!'
#digits = string.ascii_lowercase
#digits = 'cfgvhep'
#digits += string.ascii_lowercase.upper()
#print(digits)

def md5_(t: str):
    return md5(
        t.encode('utf-8')
    ).hexdigest()

hash_ = 'eb6642df776564db93c5135369b093fec4ca4238a0b923820dcc509a6f75849b63115fd6ed9119e9f92df2aaf8cec3c12913402ba1b3e811597e403168f743986667c9b63bbfbdc3120f4e47644b31fea7da902e3818f026e414349d943c7f2e5d395c88b543e23cd47c9dfc395e269b413c547e85990ae4716a374fae3896ec63115fd6ed9119e9f92df2aaf8cec3c1ac49049eb65a82a0d41cbf3f579d9e356831fd7062616de220cfc29f65343c9e35c18eb3b3e9765d833afa7f2b6bf65beb6642df776564db93c5135369b093fe3d0e983c5b34367ab32cc1b2e7403f3f63115fd6ed9119e9f92df2aaf8cec3c12c56d24ae0df8f3dbb13a7732fd668046667c9b63bbfbdc3120f4e47644b31fe86af67e10f36933c9d9b28c75142e4935d395c88b543e23cd47c9dfc395e269b70570cbb5d3a7830dbd4be19229d66a063115fd6ed9119e9f92df2aaf8cec3c1f055b40d8552e199110d390065a90d8e6831fd7062616de220cfc29f65343c9e6c5b3b4fb14889984ea7078fd61731a5'

login_ = 'kasiro'
#pass_ = 'Ctrypted!'
pass_ = '45105!45105!'
h_ = ''
def br_(login_: str, pass_: str):
    i = 1
    h_ = ''
    for l in pass_:
        h_ += md5_(
            l + md5_(
                str(ord(l))
            ) + md5_(
                login_
            ) + md5_(pass_)
        )
        i += 1
    return h_

for j in product(digits, repeat=6):
    pass_ = ''.join(j)
    pass_ += pass_
    if br_(login, pass_) == hash_:
        print()
        print(f'pass: {pass_}')
        exit()
    print(pass_)



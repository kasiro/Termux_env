from itertools import product
from random import shuffle as _sh
from sys import exit

def _(st: str, _from: str, _to: str):
    _st = st
    if len(_from) == len(_to):
        for i in range(len(_to)):
            _st.replace(
                    _from[i],
                    _to[i]
            )
    if _st == st:
        return None
    return _st

for i in range(0, 3):
    abc = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    a = list(abc)
    _sh(a)
    abc_ = ''.join(a)
    crypt = 'ОДУРГЭШБДД РЕКЦМЭЬРД'
    print(_(crypt, abc, abc_))

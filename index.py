from sys import argv
from hashlib import md5
from json import dumps as jdump
from json import loads as jload
from os.path import exists
from time import time

def md5_(t: str):
    return md5(
        t.encode('utf-8')
    ).hexdigest()

def get_(base_: dict, hash_: str):
    if hash_ in base_.keys():
        return base_[hash_].strip()
    return None


path_ = argv[1]
path_1 = path_.replace('.txt', '.json')
if not exists(path_1):
    with open(path_, 'r') as f:
        base_ = {}
        for pass_ in f:
            pass_ = pass_.strip()
            pass_.replace('\n', '')

            base_[md5_(pass_)] = pass_
        js = jdump(base_, indent = 4)
        with open(path_1, 'w') as f:
            f.write(js)
            f.close()
else:
    with open(path_1, 'r') as f:
        js = f.read()
        f.close()
        s = time()
        base_ = jload(js)
        e = time()
        bl = len(base_)
        print(
            'loaded:',
            f'{e - s:0.2f}',
            'items:', f'{bl:_}'
        )
        print('check validate data')
        i = 0
        for k, v in base_.items():
            if md5_(v) != k:
                print(f':"{v}" != {k}')
                i += 1
        if i > 0:
            print(f'invalid data: {i:_} in {bl:_}')


for i in range(1, 20):
    p = input('password >>> ')
    print(get_(base_, md5_(p)) == p)
    

from uuid import uuid4
from hashlib import md5
from itertools import product
import string
from time import time, sleep
from file_ import ff
import sys
from sys import exit
import tty
import termios
from termcolor import colored

md5_ = lambda t: md5(t.encode()).hexdigest() # noqa

def getpass(prompt='Password: '):
    """Получение пароля от пользователя без отображения введенных символов"""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(sys.stdin.fileno())
        sys.stdout.write(prompt)
        sys.stdout.flush()

        password = ""
        while True:
            char = sys.stdin.read(1)
            if char == "\r":
                break
            elif char == "\x7f" or char == "\x08":
                # Backspace или Ctrl+H
                if password:
                    password = password[:-1]
                    sys.stdout.write("\b \b")
                    sys.stdout.flush()
            elif char == "\x03":  # Ctrl+C
                raise KeyboardInterrupt
            else:
                password += char
                sys.stdout.write("*")
                sys.stdout.flush()

        sys.stdout.write("\n")
        return password.strip()

    finally:
        termios.tcsetattr(
            fd, termios.TCSADRAIN, old_settings
        )

def get_alf(s, alf):
    colored_alf = ''
    colored_letters = set()
    for l in alf: # noqa
        if l in s and l not in colored_letters:
            colored_alf += colored(l, 'green')
            colored_letters.add(l)
        else:
            colored_alf += l

    return colored_alf

def sha1_br(hash_s, charset, max_length=10):
    """Брутфорс SHA1 с солью"""
    attempts = 0
    start = time()
    hash_, salt = hash_s.split(':')

    for length in range(1, max_length + 1):
        for p in product(charset, repeat=length):
            attempts += 1
            pass_ = ''.join(p)
            
            print(pass_)
            if chek_(hash_, salt, pass_):
                end = time()
                print(f"{hash_s} -> {pass_}")
                print(f"попыток: {attempts:_}")
                print(
                    f"{end - start:0.2f} секунд"
                )
                return pass_

    print("Совпадение не найдено")
    return None

def hp_(password):
    # uuid используется для генерации случайного числа
    salt = uuid4().hex[:10]
    return md5_(
        salt + password
    ) + ':' + salt
    
def chek_(hash_ns, salt, pass_):
    return hash_ns == md5_(
        salt + pass_
    )

ch = string.digits + string.ascii_letters[:26]
for hash_ in ff('pases.txt').iter():
    sha1_br(hash_, ch, max_length=7)
    sleep(5)
exit()
p = getpass()
hash_ = hp_(p)
ff('pases.txt').put(hash_, append = True)
print('\r'+hash_)
al = string.ascii_letters[:26]
Al = string.ascii_letters[26:]
dl = string.digits

s = []
for l in p:
    if l in dl:
        s.append('0')
        dl = []
    if l in al:
        s.append('a')
        al = []
    if l in Al:
        s.append('A')
        Al = []
print()
print('len:', len(p))
print(', '.join(s))
ch = string.digits
for l in s:
    if l == 'a':
        ch += string.ascii_letters[:26]
    if l == 'A':
        ch += string.ascii_letters[26:]
if '0' not in s:
    ch = ch[10:]
print(ch)
s = input('start? (y/n) ')
if s == 'y':
    sha1_br(hash_, ch, len(p))

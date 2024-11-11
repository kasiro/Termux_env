import unittest
from termcolor import colored
import re
import string
from itertools import product
from sys import exit

def is_colored(let: str, string: str) -> bool:
    matches = get_colored(string)
    # Вывод результатов
    if matches:
        for match in matches:
            if match[0] == let:
                return True
        return False
    return None

def get_colored(string: str) -> bool:
    # Определение строки
    s = string

    # Паттерн для поиска окрашенных букв
    pattern = r"\033\[\d+m([0-9a-zA-Z])\033\[0m"

    # Поиск окрашенных букв
    return re.findall(pattern, s)

def get_alf(s, alf):
    colored_alf = ''
    colored_letters = set()

    for l in alf:
        if l in s and l not in colored_letters:
            colored_alf += colored(l, 'green')
            colored_letters.add(l)
        else:
            colored_alf += l

    return colored_alf

class TestStringColor(unittest.TestCase):

    def test_color(self):
        charset = string.digits
        charset += string.ascii_letters[:26]
        length = 5
        for p in product(charset, repeat=length):
            al = charset
            pass_ = ''.join(p)
            al = get_alf(pass_, al)
            print(pass_, al) 
            self.assertEqual(
                set(get_colored(al)), set(pass_)
            )

if __name__ == '__main__':
    unittest.main()

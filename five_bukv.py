# найди откуда брать слова
# как их красить ты уже знаешь
# через циклы
# длинна разная
# колличество попыток хз
# длинну обозначаем:
#
# *****
#print
#input
from random import choice
from termcolor import colored

worlds = [
    'hello',
    'word',
    'wants',
    'play'
]
word = choice(worlds)
print('*' * len(word))
for i in range(5):
    wr = input('')
    wr_ = ''
    for i, w in enumerate(word):
        cwr = wr[i]
        if cwr == w:
            wr_ += colored(w, 'green')
        else:
            if cwr in word:
                wr_ += colored(cwr, 'yellow')
            else:
                wr_ += cwr
    if wr != word:
        print(wr_.strip(), end='\r')
    else:
        print('word is: %s' % wr)
        break

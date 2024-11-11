from itertools import product
from sys import exit
from file_ import ff
from rich.pretty import pprint
import pymorphy3 # type: ignore

from ruwordnet import RuWordNet
wn = RuWordNet()
for sense in wn.get_senses('замок'):
    print(sense.synset)
exit()

al_ = 'атвшрку'

def generate_words(letters, repeatable_letters, max_len_):
    # Генерируем все возможные перестановки с учетом повторяемых букв
    comb = set()
    for combination in product(letters, repeat=max_len_):
        # Проверяем, что в комбинации не больше одного вхождения букв, которые не могут повторяться
        if all(combination.count(letter) <= (repeatable_letters.count(letter) + 1) for letter in set(combination)):
            comb.add(''.join(combination))
    return comb

morph = pymorphy3.MorphAnalyzer()

def is_russian_word(word):
    try:
        parsed_word = morph.parse(word)[0]
        print(parsed_word)
        return parsed_word.normal_form == word
    except Exception:
        return False

def main():
    letters = al_.strip()
    repeatable_letters = 'а'.strip()
    max_len_ = 5

    # Генерируем слова
    comb = generate_words(letters, repeatable_letters, max_len_)
    comb = set(comb)
    
    count_ = 0
    for word in sorted(comb):
        if is_russian_word(word):
            print(word)
            count_ += 1
            exit()
    print(f'count: {count_:_}')

if __name__ == "__main__":
    main()

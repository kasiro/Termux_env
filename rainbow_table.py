from hashlib import sha256
from itertools import product
import string
import pickle
from os.path import exists
from file_ import ff
from time import time, sleep

def sha256_(pass_: str) -> str:
    return sha256(pass_.encode()).hexdigest()

def create_rainbow_table(max_length=10):
    """
    Создание радужной таблицы.

    :param max_length: Максимальная длина пароля
    :return: Радужная таблица
    """
    rainbow_table = {}
    for length in range(1, max_length + 1):
        al_ = string.ascii_letters + string.digits
        for attempt in product(al_, repeat=length):
            attempt = ''.join(attempt)
            hash_ = sha256_(attempt)
            rainbow_table[hash_] = attempt
            print(attempt)
    return rainbow_table

def save_rainbow_table(rainbow_table, filename):
    """
    Сохранение радужной таблицы в файл.

    :param rainbow_table: Радужная таблица
    :param filename: Имя файла
    """
    with open(filename, 'wb') as f:
        pickle.dump(rainbow_table, f)

def load_rainbow_table(filename):
    """
    Загрузка радужной таблицы из файла.

    :param filename: Имя файла
    :return: Радужная таблица
    """
    with open(filename, 'rb') as f:
        return pickle.load(f)

def dictionary_attack(hash_, dictionary):
    """
    Словарная атака.

    :param hash: Хеш для взлома
    :param dictionary: Словарь паролей
    :return: Пароль, если найден, None иначе
    """
    for password in dictionary:
        if sha256_(password) == hash_:
            return password
    return None

def rainbow_attack(hash_, rainbow_table):
    """
    Радужная атака.

    :param hash: Хеш для взлома
    :param rainbow_table: Радужная таблица
    :return: Пароль, если найден, None иначе
    """
    return rainbow_table.get(hash_)

# Пример использования
hash_ = sha256_('pa55q')

if not exists('rainbow_table.pkl'):
    # Создание радужной таблицы
    rainbow_table = create_rainbow_table(max_length=5)

    # Сохранение радужной таблицы в файл
    save_rainbow_table(rainbow_table, 'rainbow_table.pkl')
else:
    # Загрузка радужной таблицы из файла
    print('[load] rainbow table...')
    rainbow_table = load_rainbow_table('rainbow_table.pkl')

print('[load] 3wifikey base...')
# Словарная атака
dictionary = [
    l for l in ff('downloads/3WiFi_WiFiKey.txt').iter()
]
print('[check] 3wifikey base...')
password = dictionary_attack(hash_, dictionary)
if password:
    print("Пароль найден:", password)
else:
    print("Пароль не найден")

print('[check] rainbow table...')
# Радужная атака
password = rainbow_attack(hash_, rainbow_table)
if password:
    print("Пароль найден:", password)
else:
    print("Пароль не найден")

from itertools import product

def get(s: str) -> int:
    i = 0
    for c in s:
        i += ord(c)

    return i

def get_key(text: str):
    s = ''
    for i, c in enumerate(text):
        s += hex(
            get(c) ^ (i+1) ^ len(text)
        ).replace('0x', chr(get(c) ^ (i+1)))

    return s

d = {}

for p in product('pasword0123456789', repeat=3):
    t = ''.join(p)
    d[t] = get_key(t)

# Найдите не уникальные значения
for value in d.values():
  if list(d.values()).count(value) > 1:
    print(value)

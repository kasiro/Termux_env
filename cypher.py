def split_len(seq, length):
   return [seq[i:i + length] for i in range(0, len(seq), length)]

def encode(key, plaintext):
    order = {
        int(val): num for num, val in enumerate(key)
    }
    ciphertext = ''
    for index in sorted(order.keys()):
        for part in split_len(plaintext, len(key)):
            try:
                ciphertext += part[order[index]]
            except IndexError:
                continue
    return ciphertext
print(encode('3214', 'ПРИВЕТ, КАК У ТЕБЯ ДЕЛА'))
print(encode('1234', 'И,КТ АРТА ЯЛПЕКУБЕВ  ЕД'))
print(
    split_len('ПРИВЕТ, КАК У ТЕБЯ ДЕЛА', 4)
)

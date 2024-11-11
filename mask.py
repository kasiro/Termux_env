from random import choice as ch_
from string import ascii_lowercase as alf_low
from string import digits
from hashlib import md5

md5_ = lambda x: md5(x.encode()).hexdigest()

def get_count(mask: str):
    count = 0

    for i, char in enumerate(list(mask)):
        prev_char = ''
        if char == '?':
            prev_char = '?'
            continue
        
        if char == '*' and prev_char == '?':
            count += 1
        
        if i > 0:
            prev_char = mask[i-1]
        else:
            prev_char = ''

        if char == 'd' and prev_char == '?':
            count += 1

        if char == 'l' and prev_char == '?':
            count += 1
        
        if char == 'u' and prev_char == '?':
            count += 1

    return count

def mask_(mask: str, alf_: str = 'dlu'):
    res = []
    
    alf = ''
    if '?l' in mask:
        alf += alf_low

    if '?u' in mask:
        alf += alf_low.upper()

    if '?d' in mask:
        alf += digits

    if '?*' in mask:
        if alf_low not in alf and 'l' in alf_:
            alf = alf_low

        if alf_low.upper() not in alf and 'u' in alf_:
            alf += alf_low.upper()

        if digits not in alf and 'd' in alf_:
            alf += digits

    for i, char in enumerate(list(mask)):
        prev_char = ''
        if char == '?':
            prev_char = '?'
            continue
        
        if char == '*' and prev_char == '?':
            res += ch_(alf)
        
        if i > 0:
            prev_char = mask[i-1]
        else:
            prev_char = ''

        if char == 'd' and prev_char == '?':
            res += ch_(digits)
        
        if char == 'l' and prev_char == '?':
            res += ch_(alf_low)

        if char == 'u' and prev_char == '?':
            res += ch_(alf_low.upper())

        if char != '?':
            if prev_char != '?':
                if char != '*':
                    res += char
    return ''.join(res)

m = '?*?*?*-?*?*?*?*-?*?*?*?*-?*?*?*'
print(mask_(m, 'du'), f'(\n    {m}\n)')

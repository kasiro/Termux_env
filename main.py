from typing import Callable
import re
from icecream import ic
# from file_ import ff

class _:

    def __init__(self, settings: dict) -> None:
        self.settings = settings

    def _set(self, callback: Callable) -> str:
        settings = self.settings
        if 'regex_' in settings.keys():
            regex_ = settings['regex_']
        if 'code' in settings.keys():
            code = settings['code']
        if 'flags' in settings.keys():
            flags = settings['flags']
        if not isinstance(flags, str): # type: ignore
            matches = re.search(
                regex_, # type: ignore
                code, # type: ignore
                flags=flags # type: ignore
            )
        return callback(matches, code, regex_) # type: ignore


code = """
name = 'fill'
age = 18

print(f'test: {name}')
print(f'text: {text} to main: {main}')

nl('123')

_get = lambda<str> [matches, code, regex_]: {
    print()
    gets(opt)
    for i in range(1, 11):
        print(i)

    code = callback(matches, code, regex_)
    code
}
"""

def _sets(d: str, callback: Callable):
    match = 1
    def getcode():
        return 'text'
    regex_ = r'123'
    return callback(match, getcode, regex_)

m = lambda x: _sets('', x)

_sets('', lambda x: x > 0)

def _main(matches, getcode, regex_):
    print(getcode())
    m = list(map(lambda x: len(x) > 0, matches))

_sets('test', _main)

lower_ = lambda t: t.lower()

def _a(matches, code, regex_):
    return code.replace(
        'nl(%s)' % matches[1],
        'print(%s)' % matches[1]
    )

new_code = _({
    'regex_': r'nl\((.*?)\)',
    'code': code,
    'flags': re.DOTALL | re.MULTILINE
})._set(_a)

def _b(matches, code, regex_):
    for matches_ in re.findall(regex_, code):
        text = matches_
        m = re.findall('\{(.*?)\}', text)
        for v in m:
            text = text.replace('{' + v + '}', '%s')
        res = text[1:] + f' % ({", ".join(m)})'
        if m:
            code = code.replace(
                'print(%s)' % matches_,
                'print(%s)' % res
            )
    return code

new_code = _({
    'regex_': r"print\((.*?)\)",
    'code': new_code,
    'flags': re.DOTALL | re.MULTILINE
})._set(_b)

def _c(matches, code: str, regex_) -> str:
    li = matches[len(matches.groups())].split('\n')
    cur = 0
    for i in range(1, len(li) - 1):
        t = li[len(li) - i]
        if check_(t.strip()):
             cur = i
             break
    pt = li[len(li) - cur]
    res = li[len(li) - cur].replace(
        pt.strip(),
        'return ' + pt.strip()
    )
    li[len(li) - cur] = res
    res = '\n'.join(li)
    # print(res)
    code = code.replace(
        matches[0],
        'def %s(%s) -> %s:%s' % (
            matches[1],
            matches[3],
            matches[2],
            res
        )
    )
    return code

# checked 1
def check_(text: str) -> bool:
    if len(text) == 0:
        return False
    if '(' in text or '(' in text and ')' in text:
         return True
    if re.match('[^\n\s{4,}\t]*$', text, flags=re.MULTILINE):
         return True
    return False

new_code = _({
    'regex_': r'([\w_]*?) = lambda<(.*?)> \[(.*?)\]: \{(.*?)\}',
    'code': new_code,
    'flags': re.DOTALL | re.MULTILINE
})._set(_c)
print(new_code)

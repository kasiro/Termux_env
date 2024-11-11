import requests as rq
from pyquery import PyQuery as pq
from sys import argv, exit
from rich.pretty import pprint
from os import system
import re
from subtime import _
from icecream import ic

def clear(code: str, tagnames: list):
    befcode = code
    founds_ = []
    for e in tagnames:
        if '.' not in e:
            reg_ = [
                r'<$1.*?>(.*?</$1>)?'
            ]
            for t in reg_:
                e_ = _(t).dict_replace({
                    '$1': e
                })
                m = re.search(
                    e_,
                    code,
                    flags=re.DOTALL
                )
                if m != None:
                    founds_.append(e)
                    code = re.sub(
                        e_,
                        '',
                        code,
                        flags=re.DOTALL
                    )
                    if befcode == code:
                        print('tag %s not found' % e_)
        else:
            e, class_ = e.split('.')
            reg_ = [
                r'<$_.*?class="(.*?)".*?>.*?</$_>'
            ]
            for t in reg_:
                e_ = _(t).dict_replace({
                    '$_': e
                })
                m_ = re.finditer(
                    e_,
                    code,
                    flags=re.DOTALL
                )
                for m in m_:
                    if m != None:
                        found_class = m.group(1)
                        # ic(e+'.'+found_class)
                        if class_ in found_class or class_ == found_class:
                            # ic(m[0])
                            founds_.append(e+'.'+class_)
                            code = code.replace(
                                m[0], ''
                            )
    pprint(founds_)
    return code

class pip_search:

    def __init__(self, lib_: str, page: int = 0) -> None:
        # ?o=&q=medusa&page=2
        root_ = 'https://pypi.org/'
        project_ = root_ + 'project/%s'
        self.lib_ = lib_
        if page == 1:
            res = rq.get(
                '%ssearch/?q=%s' % (
                    root_, lib_
                )
            )
        else:
            res = rq.get(
                root_ + 'search/?q=%s&page=%s' % (
                    lib_, page)
            )
        if res.status_code == 200:
            self.d = pq(res.text)
            t = clear(res.text, [
                'img',
                'script',
                'link',
                'footer',
                # 'div.language-switcher',
                'div.sponsors__divider',
                # 'div.sponsors',
                'meta',
                'noscript'
            ])
            # print(t)
            # print('<div class="sponsors__divider"></div>' in t)
            # self.max_pages = self.get_max_pages()

    def get_max_pages(self) -> int:
        a = []
        for e in self.d('[href*="/search/?q="]'):
            h_ = pq(e).attr('href')
            if '/search/' in h_: # type: ignore
                a.append(
                    int(h_.replace( # type: ignore
                        '/search/?q=%s&page=' % self.lib_,
                        ''
                    ))
                )
        return int(max(a))
        
    def get_lib(self) -> list[str]:
        return self.d(
            '.package-snippet__name'
        ).text().split(' ') # type: ignore

del argv[0]

page_ = 1
is_all = False
if len(argv) > 2:
    for i, a in enumerate(argv):
        if a == '--page' or a == '-p':
            page_ = int(argv[i+1])
        if a == '-all' or a == '-a':
            is_all = True
            
if argv[0] == 'search':
    lib_ = argv[1]
    if not is_all:
        if '==' in lib_:
            lib_, version_ = lib_.split('==')
        ps = pip_search(lib_, page_)
        # exit()
        r = ps.get_lib()
        if r != ['']:
            pprint(
                list(filter(lambda x: lib_ in x, r))
            )
            print('pages: %s' % ps.get_max_pages())
        else:
            print('[pip] not found...')
    else:
        ...
        # TODO: дописать показ всех страниц
        # в одном массиве через флаг -a
        # ps = pip_search(lib_, page_)
        # for p in range(1, ps.get_max_pages()):
        #     all_ = []
        #     r = ps.get_lib()
        #     if r != ['']:
        #         pprint(
        #             list(filter(lambda x: lib_ in x, r))
        #         )
        #         print('page:', p)
        #         print('pages: %s' % ps.get_max_pages())
        #     else:
        #         print('[pip] not found...')
else: 
    a = ' '.join(argv)
    system('pip %s' % a)

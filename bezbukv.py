import requests as rq
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
# from icecream import ic
from rich.pretty import pprint
# import re
# from subtime import _
# from sys import exit

def html_pretty(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.prettify()

def tolower(incor: list):
    return list(map(lambda w: w.lower(), incor))
        
headers = {
    # "accept": "text/css,*/*;q=0.1",
    # "accept-encoding": "gzip, deflate, br",
    # "accept-language": "ru,en;q=0.9,ru-RU;q=0.8,en-US;q=0.7",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}

class mask:

    def __init__(self, mask: str) -> None:
        self.mask = mask
        self.black_list = []
        self.white_list = []

    def setBlackList(self, blist: str) -> None:
        self.black_list = tolower(
            list(blist)
        )
        self.black_list = list(
            filter(lambda w: w not in self.mask, self.black_list)
        )

    def setWhiteList(self, wlist: str) -> None:
        self.white_list = tolower(
            list(wlist)
        )

    def getMask(self) -> str:
        return self.mask

    def getBlackList(self) -> list:
        return self.black_list
    
    def getWhiteList(self) -> list:
        return self.white_list


mask_ = mask('с****')
mask_.setBlackList('ловарбуземья')
mask_.setWhiteList('')

url = 'https://bezbukv.ru/mask/'

def filt(e):
    sym_ = ['.', '-']
    i = 0
    for s in sym_:
        if s not in e:
            i += 1

    if i == len(sym_):
        return e

def fdel(e):
    for l in list(e): # noqa
        if l in mask_.getBlackList():
            return None
    return e

def is_(e):
    white_list = mask_.getWhiteList()
    res = set(
        l for l in list(e) if l in white_list
    )
    if len(res) > 1:
        if res == set(white_list):
            return e

def filter_words(words_, letters):
    return [
        word for word in words_ if all(
            letter in word for letter in letters
        )
    ]

class bezbukv:

    def __init__(self, link: str, mask_: mask) -> None:
        html = rq.get(
            link + mask_.getMask(),
            headers=headers,
            timeout=10
        )
        if html.status_code == 200:
            d = pq(html.text)
            self.all = d('.view').text().split(' ') # type: ignore
        else:
            raise Exception('STATUS CODE: %s' % html.status_code)
    
    def in_world(self, words: str):
        w = filter_words(
            self.all,
            list(words)
        )
        pprint(w)

    def get(self):
        all = self.all
        res = list(
            filter(filt, all)
        )
        pprint(res)
        res = list(
            filter(fdel, res)
        )
        pprint(res)
        res = list(
            filter(is_, res)
        )
        pprint(res)
        # if len(res) > 0:
        #     print('\n'.join(res))
        # else:
        #     print('not found')

bezbukv(url, mask_).get()
# bezbukv(url, mask_).in_world('в')
# pprint(filter_words(
#     [
#         'видео', 'вода', 'функция',
#         'ведро', '', '',
#         '', '', ''
#     ], ['о']
# ))

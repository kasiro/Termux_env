import requests as rq
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import re
from subtime import _
from sys import exit

def html_pretty(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.prettify()

def variable_(bl: list) -> list:
    nl = []
    for e in bl:
        if '(' in e:
            if not e.startswith('#'):
                nl.append(
                    re.sub(r'\(.*?\)', '', e)
                )
                nl.append(
                    _(e)._once('', ['(', ')'])
                )
            else:
                nl.append(e[1:])
        else:
             nl.append(e)
    return nl

def vacancy_link(link: str):
    if '_' in link and link[-10:].isdigit():
        return True
    return False
        
def correct(title: str, bl: list) -> bool:
    title = _(title)._once(
        '', [',', '.', ':']
    )._once(' ', ['/', '-']) # type: ignore
    tlist = title.split(' ')
    for e in tlist:
        if e in bl:
            return False
    return True

# &p=1 - page
get_params = {
    'district': '807',
    'radius': '0',
    'presentationType': 'serp',
    'f': 'ASgBAQICAUTs0hICAUCQCySKngH49wE'
}

headers = {
    "accept": "text/css,*/*;q=0.1",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ru,en;q=0.9,ru-RU;q=0.8,en-US;q=0.7",
    "if-modified-since": "Wed, 10 May 2023 14:32:37 GMT",
    "referer": "https://www.avito.ru/",
    "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "x-client-data": "CJC2yQEIorbJAQipncoBCOfaygEIlqHLAQiFoM0BCIunzQEIx6rNAQ=="
}

black_list = variable_([
    'такси',
    'курьер',
    'уборщик',
    'уборщица',
    'грузчик(и)',
    'шофёр',
    'няня',
    'водитель',
    'учитель',
    'промоутер',
    'клинер'
])


avito = 'https://www.avito.ru'
url = '/novosibirsk/vakansii/podrabotka-ASgBAgICAUTs0hIC'

class Vacancy:

    def __init__(self, link: str) -> None:
        html = rq.get(
            link,
            headers=headers,
            params=get_params,
            timeout=10
        )
        if html.status_code == 200:
            self.d = pq(html.text)
        else:
            Exception('STATUS CODE: %s' % html.status_code)

    def price(self):
        ...
        # print(self.d)

    def exp(self):
        ...

html = rq.get(
    avito + url,
    headers=headers,
    params=get_params,
    timeout=10
)
if html.status_code != 200:
    print(html.status_code)
    # print(html.text)
d = pq(html.text)
pag_count = 0
pag = d('a.pagination-page:last').attr(
    'href'
).split('&') # type: ignore
pag = int(
    [
        p for p in pag if 'p=' in p
    ][0].split('=')[1]
)
print(
    pag
)
exit()
for v in d('a[href*="/novosibirsk/vakansii"]'):
    h = pq(v).html()
    full_link = avito + pq(v).attr('href') # type: ignore
    if len(h) > 0 and vacancy_link(full_link): # type: ignore
        title = pq(h).text()
        title_low = title.lower().strip() # type: ignore
        if correct(title_low, black_list):
            # print(html_pretty(h))
            print(title.strip()) # type: ignore
            # print(full_link)
            Vacancy(full_link).price()
            print('-'*30)
            break

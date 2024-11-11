# from icecream import ic
from jsonpath_ng.ext import parse as ps
import re

data_ = [
    {
        'name': 'Kasiro',
        'age': 20
    },
    {
        'name': 'Vasiro',
        'age': 21
    },
    {
        'name': 'Jasiro',
        'age': 22
    },
]
for match_ in ps("$[?(@.age >= 20)]").find(data_):
    val = match_.value
    print(val)
    # if re.match(r'.*\/\d\/.*', val):
    #     print(val)

import enum
import json
from pathlib import Path
from os import remove as unlink
from time import sleep
from rich.console import Console
import re

console = Console()

class Modes(enum.Enum):
    FIRST = 'first'
    LAST = 'last'
    ALL = 'all'
    LINE_NUMBER = 'line'

class File_:

    def __init__(
        self,
        file_: str,
        Unions: list,
        create_if_not_exists: bool = True 
    ):
        self.file_: str = file_
        self.Unions: list = Unions
        if create_if_not_exists:
            if not Path(file_).exists():
                with open(file_, 'w') as f:
                    f.write('')
                    f.close()
    def exists(self):
        return Path(self.file_).exists()

    def iter(self, mode: str = 'r'):
        return open(self.file_, mode)

    def get_lines_count(self):
        with open(self.file_, 'r') as f:
            le = len([l for l in f]) # noqa
            f.close()
        return le
    
    def set_line(self, LineNumber: int, line_content: str):
        r = self.iter()
        data = r.readlines()
        data[LineNumber - 1] = line_content + '\n'
        r.close()
        w = self.iter(mode = 'w')
        w.writelines(data)
        w.close()

    def get(self, m_: Modes = Modes.ALL, line_: int = 1):
        with open(self.file_, 'r') as f:
            if m_ == Modes.FIRST:
                for l in f:
                    return l.strip().replace('\n', '')
            if m_ == Modes.LAST:
                li = []
                for l in f:
                    li.append(l)
                    if len(li) > 1:
                        li.pop(0)
                return li[0].strip().replace('\n', '')
            if m_ == Modes.ALL:
                with open(self.file_, 'r') as _:
                    data = _.read()
                    _.close()
                return data
            if m_ == Modes.LINE_NUMBER:
                for i, l in enumerate(f):
                    if (i+1) == line_:
                        return l
                return None
            f.close()
    
    def deleteFile(self):
        unlink(self.file_)

    def deleteLine(self, LineNumber: int):
        all = self.get(Modes.ALL)
        li_ = all.split('\n') # type: ignore
        del li_[LineNumber - 1]
        all = '\n'.join(li_)
        self.put(all)

    def put(
            self,
            con_,
            append: bool = False,
            list_sep: str = ' ',
            handler = None
    ):
        if append:
            m = 'a'
        else:
            m = 'w'
        with open(self.file_, m) as f:
            if type(con_) in self.Unions:
                if type(con_) is int:
                    f.write(str(con_)+'\n')
                if type(con_) is str:
                    f.write(con_+'\n')
                if type(con_) is list:
                    if handler == None:
                        f.write(
                            list_sep.join(con_) + '\n'
                        )
                    else:
                        l_ = handler(con_)
                        f.write(list_sep.join(l_)+'\n')
                if type(con_) is dict:
                    f.write(json.dumps(con_) + '\n')
            else:
                print(self.Unions)
                raise TypeError(
                    str(
                        type(con_)
                    )[8:-2]+': type not support'
                )
            f.close()
def ff(FilePath: str, y=[int, str, list, dict]):
    return File_(FilePath, y)

def _sleep(secs: int):
    i = 0
    min_ = 0
    if secs >= 60:
        min_ = secs / 60
        s = secs % 60
        if s > 0 and s <= 60:
            i = s
        dots_ = str(min_).split('.')[1]
        if len(dots_) > 1:
            min_ = int(
                str(min_)[:-(len(dots_)+1)]
            )
        else:
            min_ = int(
                str(min_)[:-2]
            )
    def timer(status, secs: int):
        nonlocal i, min_
        exp_min = min_ > 0
        exp = secs > 0
        while exp_min or exp:
            exp_min = min_ > 0
            exp = secs > 0
            if min_ <= 0:
                status.update(
                    'Timer: %s' % secs
                )
            else:
                if i <= 0:
                    i = 60
                    min_ = min_ - 1
                status.update(
                    'Timer: %s:%s' % (min_, i)
                )
            sleep(1)
            if secs > 0:
                secs = secs - 1
                i = i - 1
                
    with console.status('') as st:
        timer(st, secs)

class _(str):

    def dict_replace(self, replacements: dict) -> str:
        pattern = re.compile(
            "|".join(
                map(
                    re.escape,
                    replacements.keys()
                )
            )
        )
        def replace(match):
            return replacements[match.group(0)]
        return pattern.sub(replace, self)

    def _once(self, s: str, rep: list) -> str:
        st = self
        for e in rep:
            st = st.replace(e, s)
        return _(st)


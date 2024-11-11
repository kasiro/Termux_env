#!/data/data/com.termux/files/usr/bin/python
from os import (
    getcwd,
    listdir,
    system
)
from os.path import join as _join
from random import choice
from file_ import ff, _sleep
from rich.console import Console
import click

console = Console()

def set_(wall: str):
    system('termux-wallpaper -f %s' % wall)

@click.command()
@click.option(
    '-s', '--sec', 's', type=int
)
@click.option(
    '-m',
    '--min',
    'm',
    required=True,
    type=int
)
def main(s, m):
    path_ = '/storage/shared/Pictures/100PINT/Pins/'
    path_ = getcwd() + path_
    while True:
        base = ''
        prev_base = ''
        while base == prev_base:
            walls_ = []
            for f in listdir(path_):
                if not f.startswith('.'):
                    walls_.append(f)
            base = choice(walls_).strip()
            wp = _join(path_, base)
            ff_ = ff('curr_walp.txt')
            prev_base = ff_.get().strip() # type: ignore
            if base != prev_base:
                ff_.put(base)
                set_(wp)
        if m:
            m = int(m)
            if s:
                s = int(s)
                if s > 60:
                    s = 60
                _sleep((60 * m) + s)
            else:
                _sleep((60 * m))

if __name__ == '__main__':
    main()

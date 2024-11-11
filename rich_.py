from os.path import isdir
from rich.console import Console
from time import sleep
from os import listdir

console = Console()

i_ = 0
ind = ''
def stat(status, path):
    global ind
    res = listdir(path)
    i = 1
    for file in res:
        curr = path + '/' + file
        if len(path.split('/')) > 2:
            print_path = path.split('/')
            print_path.pop(0)
            print_path.pop(0)
            print_path = '/'.join(print_path) + '/' + file
        else:
            print_path = file
        status.update(
            '[deleting][%s/%s]: %s' % (
                i, len(res), file
            )
        )
        if isdir(curr):
            print(ind + print_path + ' [folder]')
            # ind += '  '
            stat(status, curr)
            # ind = ind[:-2]
        else:
            print(ind + print_path)
        i += 1
        sleep(0.05)

i_2 = 0
ind_2 = ''
def stat_prog(status, path):
    global ind
    res = listdir(path)
    i = 1
    for file in res:
        curr = path + '/' + file
        if len(path.split('/')) > 2:
            print_path = path.split('/')
            print_path.pop(0)
            print_path.pop(0)
            print_path = '/'.join(print_path) + '/' + file
        else:
            print_path = file
        status.update(
            '[deleting][%s/%s]: %s' % (
                i, len(res), file
            )
        )
        if isdir(curr):
            print(ind + print_path + ' [folder]')
            # ind += '  '
            stat(status, curr)
            # ind = ind[:-2]
        else:
            print(ind + print_path)
        i += 1
        sleep(0.05)


with console.status('in proccess...') as s:
    stat(s, './.cache')

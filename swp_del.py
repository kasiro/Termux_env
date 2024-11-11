from os import listdir, remove, rmdir
from os.path import exists

d_ = '.local/state/nvim/swap'

if exists(d_):
    for s in listdir(d_):
        remove('%s/%s' % (d_, s))
        print('[%s] deleted...' % s)
    rmdir(d_)

if not exists(d_):
    print('[folder][swap] is clear...')

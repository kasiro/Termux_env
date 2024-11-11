from git import Repo
from rich.console import Console
from time import sleep
from icecream import ic
from sys import exit
from file_ import _sleep
from subprocess import check_output
from file_ import ff

console = Console()

aliases_ = {
    'dy': '~/dy',
    'nvim': '~/.config/nvim',
    'fish': '~/.config/fish',
    'obsidian': '/'.join([
        '~',
        'storage',
        'shared',
        'Documents',
        'obsidian'
    ])
}

def upd(repos: list[str], status):
    i = 0
    for rep in repos:
        repo_path = aliases_[rep]
        repo = Repo(repo_path)
        i += 1
        
        rep_url = [
            u for u in repo.remotes[0].urls
        ][0].split(':')[1]

        rep_url = rep_url.split('/')[1]
        if rep_url.endswith('.git'):
            rep_url = rep_url[:-4]

        if repo.is_dirty(untracked_files=True):
            repo.git.add(all=True)
            console.log('%s has update...' % rep_url)
            repo.remotes.origin.pull()
            repo.index.commit('auto upd')
            repo.remotes.origin.push()
            status.update(
                'updated %s [%s/%s]' % (
                    rep_url,
                    i,
                    len(repos)
                )
            )
            sleep(3)
        else:
            status.update(
                'skipped %s' % rep_url
            )
            sleep(0.99)
            console.log(rep_url)

while True:
    with console.status('starting...') as stat_:
        upd([
            'dy',
            'nvim',
            'fish',
            'obsidian'
        ], stat_)
        out = check_output('python -m pip freeze'.split(' ')).decode()
        pkgs = []
        pkgs_ = []
        for li_ in out.split('\n'):
            if li_ != '':
                name = li_.split('==')[0]
                pkgs.append(name)
        console.log('pip libs saved')
        console.print(
            '-' * 100,
            overflow='crop'
        )
        ff('pip_libs.txt').put('\n'.join(pkgs))
        exit()
    # _sleep((60 * 30))

"""
gul is a poetry analog

gul init <config_file>
  - create <config_file>.pyreq
  ex: gul init gc_alias

gul add <config_file> <package...>
  - add a depencity for file
  - ex: gc_alias.py ->
    gul add -c gc_alias.pyreq requests
      add depencity to .pyreq file

gul install <config_file> <package>
    create <config_file> if not exist
    add to gc_alias.pyreq requests ->
      1| requests
    run: pip install requests

gul install .
  find all files .pyreq in current dir
  and install
  run: pip install <all-packages with <space>>
  or:
      for package in packages:
          pip install package
"""

import click
from file_ import ff
from glob import glob
from subprocess import check_output, run
from rich.console import Console
from rich.pretty import pprint

console = Console()

def package_exist(config_file: str, package: str):
    return package in ff(config_file).get().split('\n') # type: ignore

def file_(config_file: str):
    if config_file.endswith('.pyreq'):
        return config_file
    else:
        return '%s%s' % (config_file, '.pyreq')

def is_install(package: str, ignore: bool = False) -> bool|list:
    if not ignore:
        out = check_output('python -m pip freeze'.split(' ')).decode()
        pkgs = []
        pkgs_ = []
        for li_ in out.split('\n'):
            if li_ != '':
                name = li_.split('==')[0]
                pkgs.append(name)
                pkgs_.append(name.replace('-', '_'))
        return package in pkgs or package in pkgs_
    else:
        out = check_output('python -m pip freeze'.split(' ')).decode()
        pkgs = []
        for li_ in out.split('\n'):
            if li_ != '':
                name = li_.split('==')[0]
                if package in name or package in name.replace('-', '_'):
                    pkgs.append(name)
        if len(pkgs) > 0:
            return pkgs
        return False

@click.group()
def gul():
    ...

@gul.command()
@click.argument('config_file')
def init(config_file):
    "<config_file>"
    cf_ = file_(config_file)
    if not ff(cf_).exists():
        run('touch %s' % cf_, shell=True)
    else:
        print('%s is exists' % cf_)

@gul.command()
@click.argument('config_file')
@click.argument('package', default='<package>')
def install(config_file, package):
    "<config_file | .> <package | >"
    if config_file == '.':
        all_ = set()
        for f_ in glob('*.pyreq'):
            for lib_ in ff(f_).iter():
                all_.add(lib_.strip())
        all_ = list(all_)
        print(all_)
    else:
        cf_ = file_(config_file)
        if not ff(cf_).exists():
            run('touch %s' % cf_, shell=True)

        if not package_exist(cf_, package):
            ff(cf_).put(package, append=True)

        if not is_install(package):
            check_output(('pip install %s' % package).split(' '))
            print('[%s] installing...' % package)
            if is_install(package):
                print('[%s] is installed...' % package)
        else:
            if package_exist(cf_, package):
                print('[%s] in %s...' % (package, cf_))
            print('[%s] is installed...' % package)

@gul.command()
@click.argument('package')
@click.option('-a', '--all', 'a', is_flag=True)
def check(package, a):
    "<package | .> check is install"

    if package == '.':
        out = check_output('python -m pip freeze'.split(' ')).decode()
        print(
            '\n'.join(list(filter(lambda x: len(x) > 0, [l_.split('==')[0] for l_ in out.split('\n')])))
        )
        return

    if is_install(package) and not a:
        print('[%s] installed...' % package)
    else:
        res = is_install(package, a)
        if res != False:
            if len(res) > 0: # type: ignore
                pprint(res)
        else:
            print('[gul] not found...')

@gul.command()
@click.argument('config_file')
@click.argument('package')
def add(config_file, package):
    "<config_file> <package>"
    cf_ = file_(config_file)
    if not package_exist(cf_, package):
        ff(cf_).put(package, append=True)
        if package in ff(cf_).get():
            print(
                '[%s] %s as added a depencity...' % (
                    cf_, package
                )
            )
    else:
        print('[%s] %s exists' % (cf_, package))

if __name__ == '__main__':
    gul()

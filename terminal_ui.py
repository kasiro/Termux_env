# сделать что то похожее на команду zi
# в тенминале, или на nvim
from rich.console import Console
console = Console()

try:
    from rich.progress import track
    from time import sleep
    from os import listdir
    from os.path import isdir

    import sys

    from rich import print
    from rich.columns import Columns

    if len(sys.argv) < 2:
        print("(ls) Usage: python columns.py DIRECTORY")
    else:
        directory = listdir(sys.argv[1])
        columns = Columns(directory, equal=True, expand=True)
        print(columns)

except Exception:
    console.print_exception()

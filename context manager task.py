# Make this code work
import os
from pathlib import Path
from contextlib import contextmanager


@contextmanager
def pushd(path):
    cwd = os.getcwd()
    cwd_obj = Path(cwd)

    os.chdir(path)

    try:
        yield cwd_obj

    finally:
        os.chdir(cwd)


cwd = Path('.').resolve()

with pushd('..') as old:
    assert Path('.').resolve() == old.parent

assert Path('.').resolve() == cwd

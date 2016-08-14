__title__ = 'pyChat Functions'
__version__ = 0.1
__author__ = 'nitros'
__license__ = 'MIT License'

from os import listdir
from os.path import isfile, join, realpath, splitext, dirname, basename

path = dirname(realpath(__file__))

__all__ = [str(splitext(f)[0]) for f in listdir(path) if (isfile(join(path,f)) and splitext(f)[1] == '.py' and f != basename(__file__))]

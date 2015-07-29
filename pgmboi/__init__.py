from os import getcwdu

__version__ = '0.0.1'

# The directory where the application was called
working_dir = getcwdu()

from config import Config
config = Config()


def parse_dir(*args, **kwargs):
    '''Generates  a directory path string'''

    slash = '/'
    _path = working_dir
    for arg in args:
        _path += slash + arg

    if 'ext' in kwargs:
        _path += '.' + kwargs['ext']

    return _path

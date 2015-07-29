from . import working_dir


def parse_dir(*args, **kwargs):
    '''Generates  a directory path string'''

    slash = '/'
    _path = working_dir
    for arg in args:
        _path += slash + arg

    if 'ext' in kwargs:
        _path += '.' + kwargs['ext']

    return _path

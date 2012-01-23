# -*- encoding: utf-8 -*-
from __future__ import print_function

import __builtin__
import sys

__all__ = ['print', '__version__']
__version__ = '0.1'

_colors = {
    'grey': 30,  'red': 31,
    'green': 32, 'yellow': 33,
    'blue': 34,  'magenta': 35,
    'cyan': 36,  'white': 37,
}

_backgrounds = {
    'grey': 40,  'red': 41,
    'green': 42, 'yellow': 43,
    'blue': 44,  'magenta': 45,
    'cyan': 46,  'white': 47,
}

_formats = {
    'bold': 1, 'dark': 2,
    'underline': 4, 'blink': 5,
    'reverse': 7, 'concealed': 8,
}

def print(*args, **kwargs):
    '''print(value, ..., sep=' ', end='\n', file=sys.stdout, color=None, background=None, format=None)

    Prints the values to a stream, or to sys.stdout by default.

    Optional keyword arguments:
    file: a file-like object (stream); defaults to the current sys.stdout.
    sep:  string inserted between values, default a space.
    end:  string appended after the last value, default a newline.

    Additional keyword arguments:
    color: prints values in specified color:
        grey red green yellow blue magenta cyan white
    background: prints values on specified color (same as color)
    format: prints values using specifiend format(s) (can be string or list):
        bold dark underline reverse concealed'''
    color = kwargs.pop('color', None)
    background = kwargs.pop('background', None)

    formats = kwargs.pop('format', [])
    if isinstance(formats, basestring):
        formats = [formats]

    file = kwargs.get('file', sys.stdout)

    if color or background:
        end = kwargs.pop('end', "\n")
        kwargs['end'] = ""

        if color:
            __builtin__.print('\033[%dm' % _colors[color], file=file, end='')
        if background:
            __builtin__.print('\033[%dm' % _backgrounds[background], file=file, end='')
        for format in formats:
            __builtin__.print('\033[%dm' % _formats[format], file=file, end='')

        __builtin__.print(*args, **kwargs)
        __builtin__.print('\033[0m', file=file, end=end)
    else:
        __builtin__.print(*args, **kwargs)

if __name__ == '__main__':
    print('Hello', 'world', color='white', background='blue', format='underline', end='', sep=', ')
    print('!', color='red', format=['bold', 'blink'])

#!/usr/bin/env python
from distutils.core import setup
import colorprint

setup(
    name='colorprint',
    version="0.1",
    license="BSD",
    description="Python module to print in color using py3k-style print function",
    long_description="""Python module to print in color using py3k-style print function. It uses
    funny hack, which allow to create print function instead standard print
    routine and give it some "black" magic.""",
    author="Aleksey Rembish",
    author_email="alex@rembish.ru",
    url="https://github.com/don-ramon/colorprint",
    py_modules = ["colorprint"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Programming Language :: Python :: 2 :: Only",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Operating System :: POSIX :: Linux",
    ],
    keywords='color colour print console py3k'
)

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import io
import os
import sys
from pgmboi import __version__ as version

here = os.path.abspath(os.path.dirname(__file__))


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(*filenames, **kwargs):

    encoding = kwargs.get('encoding', 'utf-8')

    sep = kwargs.get('sep', '\n')
    buf = []

    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README')


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


setup(
    name='pgmboi',
    version=version,

    packages=find_packages(),
    include_package_data=True,
    install_requires=['psycopg2', 'click'],

    tests_require=['pytest'],
    cmdclass={'test': PyTest},

    author='Jose Maria Dominguez',
    description='Dump a PostgreSQL database schema for easy revision control.',
    long_description=long_description,

    # test_suite='sandman.test.test_sandman',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Linux',
        'Topic :: PostgreSQL utility',
        'Environment :: Console'
    ],
    extras_require={
        'testing': ['pytest'],
    },
    entry_points='''
        [console_scripts]
        pgmboi=pgmboi.cli:main
    '''
)

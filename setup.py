#!/usr/bin/env python

import re
import sys
import os
from os.path import abspath, dirname, join
from setuptools import setup

CURDIR = dirname(abspath(__file__))
REQUIREMENTS = ['robotframework >= 3.0']
if not sys.platform.startswith('java'):
    REQUIREMENTS.append('paramiko >= 1.15.3')
    REQUIREMENTS.append('scp >= 0.13.0')
    if sys.version_info[0] < 3 and os.name == 'nt':
        REQUIREMENTS.append('win_inet_pton >= 1.1.0')
CLASSIFIERS = '''
Development Status :: 5 - Production/Stable
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Topic :: Software Development :: Testing
Framework :: Robot Framework
Framework :: Robot Framework :: Library
'''.strip().splitlines()

setup(
    name='robotframework-dummyproject',
    description='Robot Framework test library for SSH and SFTP',
    author='Robot Framework Developers',
    author_email='ayushgoswami21@gmail.com',
    url='https://github.com/ayushgoswami/Dummyproject',
    license='Apache License 2.0',
    keywords='robotframework testing testautomation ssh sftp',
    platforms='any',
    classifiers=CLASSIFIERS,
    install_requires=REQUIREMENTS,
    package_dir={'': '.'},
    packages=['DummyLibrary']
)

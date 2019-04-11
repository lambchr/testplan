#!/usr/bin/env python
'''
Setup testplan and dependencies.
'''

import sys

from setuptools import setup, find_packages


REQUIRED = [
    'sphinx',
    'sphinx_rtd_theme',
    'setuptools',
    'pytest',
    'py',
    'psutil',
    'six',
    'future',
    'schema',
    'pytz',
    'lxml',
    'python-dateutil',
    'reportlab',
    'marshmallow==3.0.0b2',
    'mock',
    'termcolor',
    'colorama',
    'enum34',
    'pyzmq',
    'terminaltables',
    'pyparsing',
    'cycler',
    'scipy',
    'scikit-learn',
    'numpy',
    'matplotlib',
    'requests>=2.4.3',
    'flask',
    'flask_restplus',
    'cheroot'
]


setup(name='Testplan',
  version='1.0',
  description='Testplan testing framework',
  author='',
  author_email='eti-testplan@morganstanley.com',
  url='https://github.com/Morgan-Stanley/testplan',
  packages=['testplan'] + find_packages(),
  include_package_data=True,
  install_requires=REQUIRED,
  scripts=['install-testplan-ui']
 )


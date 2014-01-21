# -*- coding: utf-8 -*-
"""
orgco

Copyright (c) 2013-2014, Friedrich Paetzke (f.paetzke@gmail.com)
All rights reserved.

"""
from setuptools import setup, find_packages


setup(name='orgco',
      py_modules=['orgco'],
      description='With orgco you can convert Emacs\' orgmode to other formats.',
      long_description=(open('README.rst').read()),
      version='0.1.1',
      author='Friedrich Paetzke',
      author_email='f.paetzke@gmail.com',
      license='BSD',
      url='https://github.com/paetzke/orgco',
      packages=find_packages(exclude=['tests*']),
      entry_points={
          'console_scripts': ['orgco = orgco.orgco:main']
      },
      install_requires=open('requirements/package.txt').read().splitlines(),
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Text Editors :: Emacs',
          'Topic :: Text Processing',
      ])

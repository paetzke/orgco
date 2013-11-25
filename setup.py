"""
orgco

Copyright (c) 2013, Friedrich Paetzke (f.paetzke@gmail.com)
All rights reserved.

"""
import os
from distutils.core import setup

from orgco import convert_rst


pathname = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(pathname, 'README.org')) as f:
    long_description = convert_rst(f.read())


setup(name='orgco',
      description='orgco is tool/library for converting emacs` orgmode to other formats.',
      long_description=long_description,
      version='0.0.3',
      author='Friedrich Paetzke',
      author_email='f.paetzke@gmail.com',
      license='BSD',
      url='https://github.com/paetzke/orgco',
      packages=['orgco'])

"""
orgco

Copyright (c) 2013, Friedrich Paetzke (f.paetzke@gmail.com)
All rights reserved.

"""
import os
from distutils.core import setup


pathname = os.path.abspath(os.path.dirname(__file__))
try:
    from orgco import convert_rst

    with open(os.path.join(pathname, 'README.org')) as org_file:
        with open(os.path.join(pathname, 'README.rst'), 'w') as rst_file:
            rst_file.write(convert_rst(org_file.read()))
except (FileNotFoundError, ImportError):
    pass

with open(os.path.join(pathname, 'README.rst')) as f:
    long_description = f.read()


setup(name='orgco',
      description='orgco is tool/library for converting emacs` orgmode to other formats.',
      long_description=long_description,
      version='0.0.4',
      author='Friedrich Paetzke',
      author_email='f.paetzke@gmail.com',
      license='BSD',
      url='https://github.com/paetzke/orgco',
      packages=['orgco'])

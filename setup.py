"""
orgco

Copyright (c) 2013, Friedrich Paetzke (f.paetzke@gmail.com)
All rights reserved.

"""
import os

from setuptools import setup, find_packages


pathname = os.path.abspath(os.path.dirname(__file__))
try:
    from orgco import convert_rst

    with open(os.path.join(pathname, 'README.org')) as org_file:
        with open(os.path.join(pathname, 'README.rst'), 'w') as rst_file:
            rst_file.write(convert_rst(org_file.read()))
except:
    print('Error converting .org')


setup(name='orgco',
      py_modules=['orgco'],
      description='With orgco you can convert Emacs\' orgmode to other formats.',
      long_description=(open('README.rst').read()),
      version='0.0.7',
      author='Friedrich Paetzke',
      author_email='f.paetzke@gmail.com',
      license='BSD',
      url='https://github.com/paetzke/orgco',
      packages=find_packages(exclude=['test*']),
      entry_points={
          'console_scripts': ['orgco = orgco.orgco:main']
      })

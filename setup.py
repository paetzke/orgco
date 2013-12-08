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
      version='0.0.9',
      author='Friedrich Paetzke',
      author_email='f.paetzke@gmail.com',
      license='BSD',
      url='https://github.com/paetzke/orgco',
      packages=find_packages(exclude=['test*']),
      entry_points={
          'console_scripts': ['orgco = orgco.orgco:main']
      },
      install_requires=[
          'pygments',
      ],
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Text Editors :: Emacs',
          'Topic :: Text Processing',
      ])

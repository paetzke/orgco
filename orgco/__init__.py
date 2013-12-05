"""
orgco

Copyright (c) 2013, Friedrich Paetzke (f.paetzke@gmail.com)
All rights reserved.

"""
from .convert import convert
from .orgalyzer import OrgDoc

__version__ = '0.0.6'
__author__ = 'Friedrich Paetzke'
__license__ = 'BSD'
__copyright__ = 'Copyright 2013 Friedrich Paetzke'


def _convert(content, outputtye, **kwargs):
    orgdoc = OrgDoc(content)
    result = convert(orgdoc, outputtye, **kwargs)
    return '\n'.join(result)


def convert_html(content, header=False):
    return _convert(content, 'html', header=header)


def convert_rst(content):
    return _convert(content, 'rst')

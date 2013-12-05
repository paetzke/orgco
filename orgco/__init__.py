"""
orgco

Copyright (c) 2013, Friedrich Paetzke (f.paetzke@gmail.com)
All rights reserved.

"""
from .convert import convert
from .orgalyzer import OrgDoc


def _convert(content, outputtye, **kwargs):
    orgdoc = OrgDoc(content)
    result = convert(orgdoc, outputtye, **kwargs)
    return '\n'.join(result)


def convert_html(content, header=False):
    return _convert(content, 'html', header=header)


def convert_rst(content):
    return _convert(content, 'rst')

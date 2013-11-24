"""
orgco

Copyright (c) 2013, Friedrich Paetzke (f.paetzke@gmail.com)
All rights reserved.

"""
from orgco.convert import convert
from orgco.orgalyzer import OrgDoc


def _convert(content, outputtye):
    orgdoc = OrgDoc(content)
    result = convert(orgdoc, outputtye)
    return result


def convert_html(content):
    return _convert(content, 'html')


def convert_rst(content):
    return _convert(content, 'rst')

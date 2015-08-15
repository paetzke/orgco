# -*- coding: utf-8 -*-
"""
orgco

Copyright (c) 2013-2014, Friedrich Paetzke (paetzke@fastmail.fm)
All rights reserved.

"""
from orgco import convert_html

from . import load, load_data


def test_html_shortcut():
    html = convert_html(load_data('table03.org'))
    expected = '\n'.join(load('table03.html'))
    assert html == expected


def test_html_with_highlight():
    html = convert_html(load_data('code01.org'), highlight=True)
    expected = '\n'.join(load('code01.html'))
    assert html == expected


def test_html_with_header_shortcut():
    html = convert_html(load_data('table03.org'), header=True)
    expected = '\n'.join(load('html_with_header.html'))
    assert html == expected

# -*- coding: utf-8 -*-
"""
orgco

Copyright (c) 2013-2014, Friedrich Paetzke (paetzke@fastmail.fm)
All rights reserved.

"""
from orgco.convert import convert
from orgco.orgalyzer import OrgDoc

from . import load, load_data


def assertOrgAndHtmlEqual(orgfile, htmlfile):
    html = convert(OrgDoc(load_data(orgfile)), 'html')
    expected = load(htmlfile)
    assert html == expected


def test_definition01():
    assertOrgAndHtmlEqual('definition01.org', 'definition01.html')


def test_header00():
    html = convert(OrgDoc(load_data('header00.org')), 'html')
    expected = ['<h1>header1</h1>', '']
    assert html == expected


def test_header01():
    assertOrgAndHtmlEqual('header01.org', 'header01.html')


def test_images00():
    assertOrgAndHtmlEqual('images00.org', 'images00.html')


def test_list01():
    assertOrgAndHtmlEqual('list01.org', 'list01.html')


def test_list03():
    assertOrgAndHtmlEqual('list03.org', 'list03.html')


def test_list04():
    assertOrgAndHtmlEqual('list04.org', 'list04.html')


def test_list05():
    assertOrgAndHtmlEqual('list05.org', 'list05.html')


def test_list06():
    assertOrgAndHtmlEqual('list06.org', 'list06.html')


def test_list07():
    assertOrgAndHtmlEqual('list07.org', 'list07.html')


def test_paragraph00():
    assertOrgAndHtmlEqual('paragraph00.org', 'paragraph00.html')


def test_paragraph01():
    assertOrgAndHtmlEqual('paragraph01.org', 'paragraph01.html')


def test_table02():
    assertOrgAndHtmlEqual('table02.org', 'table02.html')


def test_table03():
    assertOrgAndHtmlEqual('table03.org', 'table03.html')


def test_text00():
    assertOrgAndHtmlEqual('text00.org', 'text00.html')

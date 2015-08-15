# -*- coding: utf-8 -*-
"""
orgco

Copyright (c) 2013-2014, Friedrich Paetzke (paetzke@fastmail.fm)
All rights reserved.

"""
from orgco.convert import convert
from orgco.orgalyzer import OrgDoc

from . import load, load_data


def assertOrgAndRstEqual(orgfile, rstfile):
    rst = convert(OrgDoc(load_data(orgfile)), 'rst')
    expected = load(rstfile)
    assert rst == expected


def test_code00():
    assertOrgAndRstEqual('code00.org', 'code00.rst')


def test_definition00():
    assertOrgAndRstEqual('definition00.org', 'definition00.rst')


def test_header00():
    rst = convert(OrgDoc(load_data('header00.org')), 'rst')
    expected = ['header1', '=======', '']
    assert rst == expected


def test_header01():
    assertOrgAndRstEqual('header01.org', 'header01.rst')


def test_images00():
    assertOrgAndRstEqual('images00.org', 'images00.rst')


def test_list00():
    assertOrgAndRstEqual('list00.org', 'list00.rst')


def test_list01():
    assertOrgAndRstEqual('list01.org', 'list01.rst')


def test_list02():
    assertOrgAndRstEqual('list02.org', 'list02.rst')


def test_list03():
    assertOrgAndRstEqual('list03.org', 'list03.rst')


def test_list05():
    assertOrgAndRstEqual('list05.org', 'list05.rst')


def test_list06():
    assertOrgAndRstEqual('list06.org', 'list06.rst')


def test_paragraph00():
    assertOrgAndRstEqual('paragraph00.org', 'paragraph00.rst')


def test_paragraph01():
    assertOrgAndRstEqual('paragraph01.org', 'paragraph01.rst')


def test_text00():
    assertOrgAndRstEqual('text00.org', 'text00.rst')

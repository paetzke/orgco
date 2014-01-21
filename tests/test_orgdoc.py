# -*- coding: utf-8 -*-
"""
orgco

Copyright (c) 2013-2014, Friedrich Paetzke (f.paetzke@gmail.com)
All rights reserved.

"""
import unittest

from orgco.orgalyzer import OrgDoc

from . import load_data


def test_code00():
    org = OrgDoc(load_data('code00.org'))
    expected = '(defun org-xor (a b)\n  "Exclusive or."\n  (if a (not b) b))'
    assert len(org.things) == 1
    assert org.things[0].language == 'emacs-lisp'
    assert str(org.things[0]) == expected


def test_definition00():
    org = OrgDoc(load_data('definition00.org'))

    assert len(org.things) == 1
    assert len(org.things[0].things) == 3
    assert org.things[0].things[0].term == 'short1'
    assert org.things[0].things[0].description == 'long1'
    assert org.things[0].things[1].term == 'short2'
    assert org.things[0].things[1].description == 'long2'
    assert org.things[0].things[2].term == 'short3'
    assert org.things[0].things[2].description == 'long3'


def test_definition01():
    org = OrgDoc(load_data('definition01.org'))

    assert len(org.things) == 1
    assert len(org.things[0].things) == 3
    assert len(org.things[0].things[1].things) == 4


def test_header00():
    org = OrgDoc(load_data('header00.org'))

    assert len(org.things) == 1
    assert org.things[0].level == 1
    assert org.things[0].text == 'header1'


def test_header01():
    org = OrgDoc(load_data('header01.org'))

    assert (len(org.things) == 3)
    assert (org.things[0].level == 1)
    assert (org.things[0].text == 'header11')
    assert (org.things[1].level == 1)
    assert (org.things[1].text == 'header12')
    assert (org.things[2].level == 2)
    assert (org.things[2].text == 'header21')


def test_list00():
    org = OrgDoc(load_data('list00.org'))

    assert len(org.things) == 1
    assert len(org.things[0].things) == 3
    assert str(org.things[0].things[0]) == 'item1'
    assert str(org.things[0].things[1]) == 'item2'
    assert str(org.things[0].things[2]) == 'item3'


def test_list02():
    org = OrgDoc(load_data('list02.org'))

    assert len(org.things) == 1
    lst = org.things[0]
    assert len(lst.things) == 7
    assert len(lst.things[1].things) == 2
    assert len(lst.things[4].things) == 2
    assert len(lst.things[6].things) == 1


def test_list03():
    org = OrgDoc(load_data('list03.org'))

    assert len(org.things) == 1
    lst = org.things[0]
    assert lst.ordered == True
    assert len(lst.things) == 4
    assert str(lst.things[0]) == 'item1'
    assert str(lst.things[1]) == 'item2'
    assert str(lst.things[2]) == 'item3'
    assert str(lst.things[3]) == 'item4'


def test_paragraph00():
    org = OrgDoc(load_data('paragraph00.org'))

    assert len(org.things) == 4
    assert len(org.things[0].lines) == 4
    assert len(org.things[1].lines) == 6
    assert len(org.things[2].lines) == 6
    assert len(org.things[3].lines) == 6


def test_table00():
    org = OrgDoc(load_data('table00.org'))

    assert len(org.things) == 1
    table = org.things[0]
    assert len(table.things) == 2
    assert table.things[0].cols[0] == 'td11'
    assert table.things[0].cols[1] == 'td12'
    assert table.things[1].cols[0] == 'td21'
    assert table.things[1].cols[1] == 'td22'


def test_table01():
    org = OrgDoc(load_data('table01.org'))

    assert len(org.things) == 2
    assert len(org.things[0].things) == 2
    assert len(org.things[1].things) == 2


def test_table02():
    org = OrgDoc(load_data('table02.org'))

    assert len(org.things) == 3
    assert len(org.things[0].things) == 2
    assert len(org.things[1].things) == 3
    assert len(org.things[2].things) == 2


def test_table03():
    org = OrgDoc(load_data('table03.org'))

    assert len(org.things) == 1
    assert len(org.things[0].things) == 2
    assert org.things[0].things[0].is_header == True
    assert org.things[0].things[0].cols[0] == 'th1'
    assert org.things[0].things[0].cols[1] == 'th2'
    assert org.things[0].things[1].is_header == False
    assert org.things[0].things[1].cols[0] == 'td1'
    assert org.things[0].things[1].cols[1] == 'td2'

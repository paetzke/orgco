#! /usr/bin/env python3
"""
orgco

Copyright (c) 2013, Friedrich Paetzke (f.paetzke@gmail.com)
All rights reserved.

"""

import sys
import os
import unittest

BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, BASE_DIR)

from orgco import convert_html
from orgco.convert import convert
from orgco.orgalyzer import OrgDoc


def load_data(filename):
    filename = os.path.join(BASE_DIR, 'test/data', filename)
    with open(filename, 'r') as f:
        return f.read()


def load(filename):
    return load_data(filename).split('\n')[0:-1]


class TestOrgDoc(unittest.TestCase):

    def test_code00(self):
        org = OrgDoc(load_data('code00.org'))
        expected = '(defun org-xor (a b)\n  "Exclusive or."\n  (if a (not b) b))'
        self.assertEqual(len(org.things), 1)
        self.assertEqual(org.things[0].language, 'emacs-lisp')
        self.assertEqual(str(org.things[0]), expected)

    def test_definition00(self):
        org = OrgDoc(load_data('definition00.org'))

        self.assertEqual(len(org.things), 1)
        self.assertEqual(len(org.things[0].things), 3)
        self.assertEqual(org.things[0].things[0].term, 'short1')
        self.assertEqual(org.things[0].things[0].description, 'long1')
        self.assertEqual(org.things[0].things[1].term, 'short2')
        self.assertEqual(org.things[0].things[1].description, 'long2')
        self.assertEqual(org.things[0].things[2].term, 'short3')
        self.assertEqual(org.things[0].things[2].description, 'long3')

    def test_definition01(self):
        org = OrgDoc(load_data('definition01.org'))

        self.assertEqual(len(org.things), 1)
        self.assertEqual(len(org.things[0].things), 3)
        self.assertEqual(len(org.things[0].things[1].things), 4)

    def test_header00(self):
        org = OrgDoc(load_data('header00.org'))

        self.assertEqual(len(org.things), 1)
        self.assertEqual(org.things[0].level, 1)
        self.assertEqual(org.things[0].text, 'header1')

    def test_header01(self):
        org = OrgDoc(load_data('header01.org'))

        self.assertEqual(len(org.things), 3)
        self.assertEqual(org.things[0].level, 1)
        self.assertEqual(org.things[0].text, 'header11')
        self.assertEqual(org.things[1].level, 1)
        self.assertEqual(org.things[1].text, 'header12')
        self.assertEqual(org.things[2].level, 2)
        self.assertEqual(org.things[2].text, 'header21')

    def test_list00(self):
        org = OrgDoc(load_data('list00.org'))

        self.assertEqual(len(org.things), 1)
        self.assertEqual(len(org.things[0].things), 3)
        self.assertEqual(org.things[0].things[0].text, 'item1')
        self.assertEqual(org.things[0].things[1].text, 'item2')
        self.assertEqual(org.things[0].things[2].text, 'item3')

    def test_list02(self):
        org = OrgDoc(load_data('list02.org'))

        self.assertEqual(len(org.things), 1)
        lst = org.things[0]
        self.assertEqual(len(lst.things), 7)
        self.assertEqual(len(lst.things[1].things), 2)
        self.assertEqual(len(lst.things[4].things), 2)
        self.assertEqual(len(lst.things[6].things), 1)

    def test_list03(self):
        org = OrgDoc(load_data('list03.org'))

        self.assertEqual(len(org.things), 1)
        lst = org.things[0]
        self.assertTrue(lst.ordered)
        self.assertEqual(len(lst.things), 4)
        self.assertEqual(str(lst.things[0]), 'item1')
        self.assertEqual(str(lst.things[1]), 'item2')
        self.assertEqual(str(lst.things[2]), 'item3')
        self.assertEqual(str(lst.things[3]), 'item4')

    def test_paragraph00(self):
        org = OrgDoc(load_data('paragraph00.org'))

        self.assertEqual(len(org.things), 4)
        self.assertEqual(len(org.things[0].lines), 4)
        self.assertEqual(len(org.things[1].lines), 6)
        self.assertEqual(len(org.things[2].lines), 6)
        self.assertEqual(len(org.things[3].lines), 6)

    def test_table00(self):
        org = OrgDoc(load_data('table00.org'))

        self.assertEqual(len(org.things), 1)
        table = org.things[0]
        self.assertEqual(len(table.things), 2)
        self.assertEqual(table.things[0].cols[0], 'td11')
        self.assertEqual(table.things[0].cols[1], 'td12')
        self.assertEqual(table.things[1].cols[0], 'td21')
        self.assertEqual(table.things[1].cols[1], 'td22')

    def test_table01(self):
        org = OrgDoc(load_data('table01.org'))

        self.assertEqual(len(org.things), 2)
        self.assertEqual(len(org.things[0].things), 2)
        self.assertEqual(len(org.things[1].things), 2)

    def test_table02(self):
        org = OrgDoc(load_data('table02.org'))

        self.assertEqual(len(org.things), 3)
        self.assertEqual(len(org.things[0].things), 2)
        self.assertEqual(len(org.things[1].things), 3)
        self.assertEqual(len(org.things[2].things), 2)

    def test_table03(self):
        org = OrgDoc(load_data('table03.org'))

        self.assertEqual(len(org.things), 1)
        self.assertEqual(len(org.things[0].things), 2)
        self.assertEqual(org.things[0].things[0].is_header, True)
        self.assertEqual(org.things[0].things[0].cols[0], 'th1')
        self.assertEqual(org.things[0].things[0].cols[1], 'th2')
        self.assertEqual(org.things[0].things[1].is_header, False)
        self.assertEqual(org.things[0].things[1].cols[0], 'td1')
        self.assertEqual(org.things[0].things[1].cols[1], 'td2')


class TestHtml(unittest.TestCase):

    def test_definition01(self):
        html = convert(OrgDoc(load_data('definition01.org')), 'html')
        expected = load('definition01.html')
        self.assertEqual(html, expected)

    def test_header00(self):
        html = convert(OrgDoc(load_data('header00.org')), 'html')
        expected = ['<h1>header1</h1>']
        self.assertEqual(html, expected)

    def test_header01(self):
        html = convert(OrgDoc(load_data('header01.org')), 'html')
        expected = load('header01.html')
        self.assertEqual(html, expected)

    def test_list01(self):
        html = convert(OrgDoc(load_data('list01.org')), 'html')
        expected = load('list01.html')
        self.assertEqual(html, expected)

    def test_list03(self):
        html = convert(OrgDoc(load_data('list03.org')), 'html')
        expected = load('list03.html')
        self.assertEqual(html, expected)

    def test_paragraph00(self):
        html = convert(OrgDoc(load_data('paragraph00.org')), 'html')
        expected = load('paragraph00.html')
        self.assertEqual(html, expected)

    def test_paragraph01(self):
        html = convert(OrgDoc(load_data('paragraph01.org')), 'html')
        expected = load('paragraph01.html')
        self.assertEqual(html, expected)

    def test_table02(self):
        html = convert(OrgDoc(load_data('table02.org')), 'html')
        expected = load('table02.html')
        self.assertEqual(html, expected)

    def test_table03(self):
        html = convert(OrgDoc(load_data('table03.org')), 'html')
        expected = load('table03.html')
        self.assertEqual(html, expected)

    def test_text00(self):
        html = convert(OrgDoc(load_data('text00.org')), 'html')
        expected = load('text00.html')
        self.assertEqual(html, expected)


class TestShortcuts(unittest.TestCase):

    def test_html_shortcut(self):
        html = convert_html(load_data('table03.org'))
        expected = '\n'.join(load('table03.html'))
        self.assertEqual(html, expected)


class TestRst(unittest.TestCase):

    def test_code00(self):
        rst = convert(OrgDoc(load_data('code00.org')), 'rst')
        expected = load('code00.rst')
        self.assertEqual(rst, expected)

    def test_definition00(self):
        rst = convert(OrgDoc(load_data('definition00.org')), 'rst')
        expected = load('definition00.rst')
        self.assertEqual(rst, expected)

    def test_header00(self):
        rst = convert(OrgDoc(load_data('header00.org')), 'rst')
        expected = ['header1', '=======']
        self.assertEqual(rst, expected)

    def test_header01(self):
        rst = convert(OrgDoc(load_data('header01.org')), 'rst')
        expected = load('header01.rst')
        self.assertEqual(rst, expected)

    def test_list00(self):
        rst = convert(OrgDoc(load_data('list00.org')), 'rst')
        expected = load('list00.rst')
        self.assertEqual(rst, expected)

    def test_list01(self):
        rst = convert(OrgDoc(load_data('list01.org')), 'rst')
        expected = load('list01.rst')
        self.assertEqual(rst, expected)

    def test_list02(self):
        rst = convert(OrgDoc(load_data('list02.org')), 'rst')
        expected = load('list02.rst')
        self.assertEqual(rst, expected)

    def test_list03(self):
        rst = convert(OrgDoc(load_data('list03.org')), 'rst')
        expected = load('list03.rst')
        self.assertEqual(rst, expected)

    def test_paragraph00(self):
        rst = convert(OrgDoc(load_data('paragraph00.org')), 'rst')
        expected = load('paragraph00.rst')
        self.assertEqual(rst, expected)

    def test_paragraph01(self):
        rst = convert(OrgDoc(load_data('paragraph01.org')), 'rst')
        expected = load('paragraph01.rst')
        self.assertEqual(rst, expected)

    def test_text00(self):
        rst = convert(OrgDoc(load_data('text00.org')), 'rst')
        expected = load('text00.rst')
        self.assertEqual(rst, expected)


if __name__ == '__main__':
    unittest.main()

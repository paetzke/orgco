# -*- coding: utf-8 -*-
"""
orgco

Copyright (c) 2013-2014, Friedrich Paetzke (paetzke@fastmail.fm)
All rights reserved.

"""
from orgco.convert import find_markup


def test_regard_return_as_space():
    markup, i = find_markup('[[Some link]]\r', 0)
    assert i == 13
    assert markup == '[[Some link]]'


def test_minimum_markup_length():
    markup, i = find_markup('c++', 0)
    assert markup == 'c'
    assert i == 1

    markup, i = find_markup('c++', i)
    assert markup == '+'
    assert i == 2


def test_colon_after_markup():
    markup, i = find_markup('/bold/: bool, default False', 0)
    assert markup == '/bold/'
    assert i == 6

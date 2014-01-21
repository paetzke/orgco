# -*- coding: utf-8 -*-
"""
orgco

Copyright (c) 2013-2014, Friedrich Paetzke (f.paetzke@gmail.com)
All rights reserved.

"""
import os


def load_data(filename):
    test_data = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    filename = os.path.join(test_data, 'tests/data', filename)
    with open(filename, 'r') as f:
        return f.read()


def load(filename):
    return load_data(filename).split('\n')

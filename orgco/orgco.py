#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
orgco

Copyright (c) 2013, Friedrich Paetzke (f.paetzke@gmail.com)
All rights reserved.

"""
from argparse import ArgumentParser, FileType

from .convert import convert
from .orgalyzer import OrgDoc


def main():
    parser = ArgumentParser()
    parser.add_argument('-i', '--input', type=FileType('r'), required=True)
    parser.add_argument('-o', '--output', type=FileType('w'), required=True)
    parser.add_argument('-f', '--format', type=str, required=True)
    parser.add_argument('--header', action='store_const', const=True, default=False)
    parser.add_argument('--highlight', action='store_const', const=True, default=False)
    parser.add_argument('--includes', type=str, nargs='+')
    args = parser.parse_args()

    options = {}
    if args.highlight:
        options['highlight'] = args.highlight
    if args.header:
        options['header'] = args.header
    if args.includes:
        options['includes'] = args.includes

    input_content = args.input.read()
    orgdoc = OrgDoc(content=input_content)
    output = convert(orgdoc, args.format, **options)
    for line in output:
        args.output.write('%s\n' % line)


if __name__ == '__main__':
    main()

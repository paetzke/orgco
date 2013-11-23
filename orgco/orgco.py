#! /usr/bin/env python3
"""
orgco

Copyright (c) 2013, Friedrich Paetzke (f.paetzke@gmail.com)
All rights reserved.

"""

from argparse import ArgumentParser, FileType

from orgco.convert import convert
from orgco.orgalyzer import OrgDoc


def main(args):
    input_content = args.input.read()
    orgdoc = OrgDoc(content=input_content)
    kwargs = {'only_body': False}
    output = convert(orgdoc, args.format, **kwargs)
    for line in output:
        args.output.write('%s\n' % line)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-i', '--input', type=FileType('r'), required=True)
    parser.add_argument('-o', '--output', type=FileType('w'), required=True)
    parser.add_argument('-f', '--format', type=str, required=True)
    args = parser.parse_args()
    main(args)

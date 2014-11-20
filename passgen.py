#!/usr/bin/env python
# -*- coding: utf8 -*-
from __future__ import print_function
import argparse
import random
import string
import sys


def get_parser():
    parser = argparse.ArgumentParser(
        description="This is a sample of argparse.",
        epilog="This is an additional description appears in help footer.",
    )
    parser.add_argument('-l',
                        '--length',
                        action='store',
                        type=int,
                        default=12,
                        help='length of password.')
    parser.add_argument('-A',
                        '--with-out-ascii',
                        action='store_true',
                        default=False,
                        help='without ascii letters.')
    parser.add_argument('-P',
                        '--with-out-punctuation',
                        action='store_true', default=False,
                        help='without punctuations.')
    parser.add_argument('-U',
                        '--with-out-uppercase',
                        action='store_true',
                        default=False,
                        help='without upper case letters.')
    return parser.parse_args()


def generate(length, with_out_ascii=False, with_out_uppercase=False, with_out_punctuation=False):
    seed = string.digits
    if not with_out_ascii:
        seed = seed + string.ascii_lowercase
    if not with_out_uppercase and not with_out_ascii:
        seed = seed + string.ascii_uppercase
    if not with_out_punctuation and not with_out_ascii:
        seed = seed + string.punctuation
    return ''.join(random.choice(seed) for _ in range(length))


def main():
    args = get_parser()
    password = generate(args.length,
                        args.with_out_ascii,
                        args.with_out_uppercase,
                        args.with_out_punctuation)
    sys.stdout.write(password)
    print()

if __name__ == '__main__':
    main()

# vim: et sw=4 ts=4

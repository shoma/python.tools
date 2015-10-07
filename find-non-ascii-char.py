#!/usr/bin/python3
import string
import sys
import io

asciichars = string.whitespace + string.ascii_letters + string.digits + string.punctuation

reset = '\x1b[0m'
txt_black_bold = '\x1b[30m'
on_yellow = '\x1b[43m'


def print_line(line):
    in_non_ascii = False
    o = ''
    for c in line:
        if c not in asciichars:
            if not in_non_ascii:
                o = o + on_yellow + txt_black_bold
            in_non_ascii = True
        else:
            if in_non_ascii:
                o = o + reset
            in_non_ascii = False
        o = o + c
    if in_non_ascii and not o.endswith(reset):
        o = o + reset
    print(o, end="")


def none_ascii_in_file(filepath):
    with open(filepath) as f:
        data = io.StringIO(f.read()).getvalue()
        try:
            data.encode('ascii')
        except UnicodeEncodeError:
            return True
    return False


if __name__ == '__main__':
    files = sys.argv[1:]
    for infile in files:
        if none_ascii_in_file(infile):
            with open(infile) as f:
                lines = f.readlines()
                for line in lines:
                    print_line(line)

# vim: et sw=4 ts=4

#!/usr/bin/env python
# subby.py
# Aids in transforming multi-character symbols of a non-standard substitution
# cipher into single, printable characters. Also displays frequency of the
# non-standard symbols.
#
# `subby.py -h` for usage
import argparse

SYMBOL_TABLE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def transform_symbols(ciphertext, separator):
    counts = {}
    symbols = {}
    symbol = 0

    for group in ciphertext.split(separator):
        if group in counts:
            counts[group] += 1
        else:
            counts[group] = 1
            symbols[group] = SYMBOL_TABLE[symbol]
            symbol += 1

    return (counts, symbols)


def main():
    parser = argparse.ArgumentParser(
        description="""Aids in transforming multi-character symbols of a
        non-standard substitution cipher into single, printable characters.
        Also displays frequency of the non-standard symbols.""")
    parser.add_argument("ctfile", help="ciphertext file")
    parser.add_argument("-s", "--separator",
                        help="group separator (defaults to whitespace)")

    args = parser.parse_args()

    ctfile = open(args.ctfile, 'r')
    contents = ctfile.read()

    counts = {}
    symbols = {}

    if args.separator is not None:
        separator = args.separator
    else:
        separator = None

    counts, symbols = transform_symbols(contents, separator)

    print "Size of table: ", len(counts)

    # Sort by frequency and print
    sorted_counts = sorted(counts.items(), key=lambda t: t[1])
    sorted_counts.reverse()
    for item in sorted_counts:
        print "\"%s\"\t%s\t%d" % (item[0], symbols[item[0]], item[1])

if __name__ == "__main__":
    main()

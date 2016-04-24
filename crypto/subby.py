#!/usr/bin/env python
# subby.py
# Aids in transforming multi-character symbols of a non-standard substitution
# cipher into single, printable characters. Also displays frequency of the
# non-standard symbols.
#
# `subby.py -h` for usage
import argparse
import etao

SYMBOL_TABLE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def transform_symbols(ciphertext, separator):
    counts = {}
    symbols = {}
    symbol = 0

    if separator is False:
        contents = ciphertext
    else:
        contents = ciphertext.split(separator)

    for group in contents:
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

    sep_group = parser.add_mutually_exclusive_group()
    sep_group.add_argument("-s", "--separator", type=str,
                           help="group separator (defaults to whitespace)")
    sep_group.add_argument("-n", "--no-separator", action='store_true',
                           help="don't use separators, split on every byte")

    args = parser.parse_args()

    ctfile = open(args.ctfile, 'r')
    contents = ctfile.read()

    counts = {}
    symbols = {}

    if args.no_separator:
        separator = False
    else:
        separator = args.separator

    counts, symbols = transform_symbols(contents, separator)

    print "Size of table: ", len(counts)

    # Sort by frequency and print
    sorted_counts = sorted(counts.items(), key=lambda t: t[1])
    sorted_counts.reverse()
    for item in sorted_counts:
        print "\"%s\"\t%s\t%d" % (
            etao.escape_nonprintables(item[0]),
            symbols[item[0]], item[1])

if __name__ == "__main__":
    main()

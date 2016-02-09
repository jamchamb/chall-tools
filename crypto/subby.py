#!/usr/bin/env python
# subby.py
# Aids in transforming multi-character symbols of a non-standard substitution cipher
# into single, printable characters. Also displays frequency of the non-standard
# symbols.
#
# `subby.py -h` for usage
import argparse
from etao import num_to_letter

def transform_symbols(ciphertext, separator):
    counts = {}
    symbols = {}
    symbol = 1

    for group in ciphertext.split(separator):
        if counts.has_key(group):
            counts[group] += 1
        else:
            counts[group] = 1
            symbols[group] = num_to_letter(symbol)
            symbol += 1

    return (counts,symbols)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ctfile", help="ciphertext file")
    parser.add_argument("-s", "--separator", help="group separator (default SPACE)")

    args = parser.parse_args()

    ctfile = open(args.ctfile, 'r')
    contents = ctfile.read()

    counts = {}
    symbols = {}
    symbol = 1

    if args.separator != None:
        separator = args.separator
    else:
        separator = ' '

    counts,symbols = transform_symbols(contents, separator)

    print "Size of table: " + str(len(counts))

    # Sort by frequency and print
    sorted_counts = sorted(counts.items(), key=lambda t: t[1])
    sorted_counts.reverse()
    for item in sorted_counts:
        print item[0] + "\t" + symbols[item[0]] + "\t" + str(item[1])

if __name__ == "__main__":
    main()

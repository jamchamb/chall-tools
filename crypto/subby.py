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


def transform_symbols(ciphertext):
    """Transform each multi-character symbol into a single character.
       Returns count and symbol dictionary for each group."""
    counts = {}
    symbols = {}
    symbol = 0

    for group in ciphertext:
        if group in counts:
            counts[group] += 1
        else:
            counts[group] = 1
            symbols[group] = SYMBOL_TABLE[symbol]
            symbol += 1

    return (counts, symbols)


def transform_text(ciphertext, symbols):
    """Translate the original ciphertext into a single character based
       ciphertext using the symbol table."""

    result = ''

    for group in ciphertext:
        if group in symbols:
            result += symbols[group]
        else:
            result += '(%s)' % (group)

    return result


def guess_plaintext(ciphertext, counts, symbols):
    """Do a single naive substitution based on frequency."""
    freq_vector = sorted(etao.freq.ENGLISH_FREQ.items(),
                         key=lambda t: t[1])
    freq_vector.reverse()

    sorted_counts = sorted(counts.items(), key=lambda t: t[1])
    sorted_counts.reverse()

    ordered_counts = [x[0] for x in sorted_counts]

    result = ''

    for group in ciphertext:
        group_index = ordered_counts.index(group)
        if group_index < len(freq_vector):
            result += freq_vector[group_index][0]
        else:
            result += '(%s)' % (symbols[group])

    return result


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

    if not args.no_separator:
        contents = contents.split(args.separator)

    counts, symbols = transform_symbols(contents)

    print "Size of table: ", len(counts)

    # Sort by frequency and print
    sorted_counts = sorted(counts.items(), key=lambda t: t[1])
    sorted_counts.reverse()
    for item in sorted_counts:
        print "\"%s\"\t%s\t%d" % (
            etao.escape_nonprintables(item[0]),
            symbols[item[0]], item[1])

    transformed = transform_text(contents, symbols)

    print '\nTransformed ciphertext:'
    print transformed

    #print '\nNaive plaintext guess:'
    #print guess_plaintext(contents, counts, symbols)

if __name__ == "__main__":
    main()

#!/usr/bin/env python
import argparse
import etao
import fileinput
import sys

def main():
    parser = argparse.ArgumentParser(description='Output lines that meet a certain frequency score')
    parser.add_argument('infile', type=argparse.FileType('r'),
                        nargs='?', default=sys.stdin, help='filename or nothing for stdin')
    parser.add_argument('--cutoff', type=float, default=0.3,
                        help='cutoff frequency score')
    parser.add_argument('--digrams', action='store_true',
                        default=False, help='use digram frequency')
    args = parser.parse_args()

    if args.digrams:
        freq_table = etao.freq.ENGLISH_DIGRAMS
    else:
        freq_table = etao.freq.ENGLISH_FREQ

    scorer = etao.NgramFrequencyScorer(freq_table)

    for line in args.infile.readlines():
        line = line.rstrip('\n\r')
        if scorer.score(line) > args.cutoff:
            print etao.escape_nonprintables(line)


if __name__ == "__main__":
    main()



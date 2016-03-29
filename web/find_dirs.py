#!/usr/bin/env python
import argparse
import requests


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('root', type=str,
                        help="Root HTTP path to scan")
    parser.add_argument('wordlist', type=str,
                        help="Newline separated list of directories to try")
    args = parser.parse_args()

    root_dir = args.root.rstrip('/')

    with open(args.wordlist, 'r') as wordlist:
        for line in wordlist:
            cur_dir = line.rstrip('\r\n')
            r = requests.get(root_dir + '/' + cur_dir)
            if r.status_code != 404:
                print '%d: %s' % (r.status_code, cur_dir)

if __name__ == "__main__":
    main()

#!/usr/bin/env python
import argparse
import hashlib
import binascii
import sys


def main():
    parser = argparse.ArgumentParser(description='MD5 Cracker')
    parser.add_argument('hash', help='MD5 hash to crack', type=str)
    parser.add_argument('wordlist', help='wordlist', type=str)
    args = parser.parse_args()

    if len(args.hash) != 32 or not args.hash.isalnum():
        print 'Invalid hash'

    target = binascii.unhexlify(args.hash)
    found = False

    with open(args.wordlist, 'r') as wordlist:
        for word in wordlist:
            word = word.rstrip('\n')
            hashed = hashlib.md5(word).digest()
            if hashed == target:
                found = True
                print 'FOUND %s: "%s"' % (args.hash, word)
                break

    if not found:
        print 'Password not found in wordlist'
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == '__main__':
    main()

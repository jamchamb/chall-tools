#!/usr/bin/python
# Helps with substitution ciphers that use something other than
# single alphabetic characters.
import sys

if len(sys.argv) < 2:
    print "Usage: subby.py <ciphertext_file>"
    sys.exit(1)

ctfile = open(sys.argv[1], 'r')
contents = ctfile.read()

counts = {}
symbols = {}
symbol = 0

for group in contents.split(' '):
    if counts.has_key(group):
        counts[group] += 1
    else:
        counts[group] = 1
        symbols[group] = unichr(symbol + 0x41)
        symbol += 1
    print symbols[group],
print ""
        
print "Size of table: " + str(len(counts))

# Sort by frequency and print
sorted_counts = sorted(counts.items(), key=lambda t: t[1])
sorted_counts.reverse()
for item in sorted_counts:
    print item[0] + "\t" + symbols[item[0]] + "\t" + str(item[1])



    

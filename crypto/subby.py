# Helps with substitution ciphers that use something other than
# single alphabetic characters.
import argparse
from crypta import num_to_letter

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
        
    for group in contents.split(separator):
        if counts.has_key(group):
            counts[group] += 1
        else:
            counts[group] = 1
            symbols[group] = num_to_letter(symbol)
            symbol += 1
            print symbols[group],
    print ""
        
    print "Size of table: " + str(len(counts))

    # Sort by frequency and print
    sorted_counts = sorted(counts.items(), key=lambda t: t[1])
    sorted_counts.reverse()
    for item in sorted_counts:
        print item[0] + "\t" + symbols[item[0]] + "\t" + str(item[1])
    
if __name__ == "__main__":
    main()

# Vigenere analysis with Ohaver routine
# Generates a list of all possible trigrams in the ciphertext and then
# determines the keys that would have been needed to reach that ciphertext
# from common plaintext trigrams. May reveal fragments of the key.
import argparse   
from crypta import letter_to_num, num_to_letter

def all_trigrams(text):
    trigrams = []
    for i in range(len(text) - 2):
        trigrams.append(text[i:i+3])
    return trigrams

def reverse_vigenere(plain, cipher):
    """ Determine the key that would have been applied to
    the plaintext in order to produce the given
    ciphertext. """

    if len(plain) != len(cipher):
        raise Exception("Plaintext and ciphertext length must match")

    key = ""
    
    for i in range(len(cipher)):
        c = letter_to_num(cipher[i])
        p = letter_to_num(plain[i])
        k = c - p
        if k < 0:
            k += 26
        key += num_to_letter(k+1)

    return key
        
def analyze(cipher_text, trigrams=None):
    cipher_text = cipher_text.replace('\r','').replace('\n','').replace(' ','').upper()
    
    ct_trigrams = all_trigrams(cipher_text)
    pt_trigrams = [
        'THE','AND','THA','ENT','ING','ION',
        'TIO','FOR','NDE','HAS','NCE','EDT',
        'TIS','OFT','STH','MEN'
    ]

    if trigrams != None:
        pt_trigrams = trigrams
    
    keys = {}

    # Build key fragments that would get ct from pt
    for pt_trigram in pt_trigrams:
        pt_vig = []
        for ct_trigram in ct_trigrams:
            pt_vig.append(reverse_vigenere(pt_trigram,ct_trigram))
        keys[pt_trigram] = pt_vig

    # Display the results
    cols = 80
    per_row = cols / 4
    for pt_trigram in pt_trigrams:
        print pt_trigram+":"

        pos = 0
        while pos < len(ct_trigrams):
            print '\t',
            for ct_trigram in ct_trigrams[pos:pos+per_row]:
                print ct_trigram,
            print '\n\t',
            for key in keys[pt_trigram][pos:pos+per_row]:
                print key,
            print '\n'
            pos += per_row
            
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ctfile", help="ciphertext file")
    parser.add_argument("-t", "--trigrams", help="comma-separated plaintext trigrams to use")
    
    args = parser.parse_args()

    with open(args.ctfile, 'r') as ctfile:
        cipher_text = ctfile.read()

    if args.trigrams == None:
        analyze(cipher_text)
    else:
        trigrams = args.trigrams.split(',')
        for trigram in trigrams:
            if len(trigram) != 3:
                print "Invalid trigram", trigram
                return
        analyze(cipher_text, trigrams)
        
if __name__ == "__main__":
    main()

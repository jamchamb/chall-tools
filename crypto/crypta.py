# General cryptography/cryptanalysis functions

def letter_to_num(letter):
    return ord(letter) - ord('A') + 1

def num_to_letter(num):
    return chr(num-1 + ord('A'))


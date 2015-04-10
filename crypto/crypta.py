# General cryptography/cryptanalysis functions
import base64
import binascii
import string

def letter_to_num(letter):
    return ord(letter) - ord('A') + 1

def num_to_letter(num):
    return chr(num-1 + ord('A'))

def hex_to_bytes(s):
    return binascii.unhexlify(s)

def bytes_to_b64(b):
    return base64.b64encode(b)

def hex_to_b64(s):
    return bytes_to_b64(hex_to_bytes(s))

def xor_bytes(b1, b2):
    result = ''
    for i in range(len(b1)):
        result += chr(ord(b1[i]) ^ ord(b2[i]))
    return binascii.hexlify(result)

def escape_nonprintables(s):
    result = ''
    printable = string.ascii_letters + string.digits + string.punctuation + ' '
    for c in s:
        if c not in printable:
            result += '\\x' + binascii.hexlify(c)
        else:
            result += c
    return result

english_freq = {
    'e': 12.02,
    't': 9.10,
    'a': 8.12,
    'o': 7.68,
    'i': 7.31,
    'n': 6.95,
    's': 6.28,
    'r': 6.02,
    'h': 5.92,
    'd': 4.32,
    'l': 3.98,
    'u': 2.88
    }

def score_text(s):
    score = 0
    for c in s:
        if c.lower() in english_freq:
            score += english_freq[c.lower()]
    return score

        

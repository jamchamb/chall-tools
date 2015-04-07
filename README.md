# chall-tools
Scripts and tools I write to help solve challenges (cryptography, steganography,
reverse engineering, etc.).

## Cryptography

### `subby.py`
Aids in transforming multi-character symbols of a non-standard substitution cipher
into single, printable characters. Also displays a frequency count of the symbols,
alongside their single character translations.

### `ohaver.py`
A Python implementation of the Ohaver routine described in Gaines' _Cryptanalysis_,
chapter 12. Attacks the Vigenere cipher by assuming that any given trigram in the
ciphertext corresponds to a common (or specified) plaintext trigram, and then lists
the key fragment that would produce such a result. Likely key fragments can then be
used in further analysis.

### `byteshift.py`
Caesar cipher applied to bytes instead of letters.

## Exploits

### `input_gen.py`
Generates test inputs for buffer overflow attacks.

## Miscellaneous

### `modmath.py`
Some useful calculations performed with modular arithmetic (factorial, division,
binomial coefficient, etc.).

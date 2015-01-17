# Caesar cipher on bytes rather than just alphabet
# usage: byteshift.py [-h] [-m MODULO] infile outfile shift
import argparse

def shift_bytes(data, shift, mod):
    shifted = bytearray()
    for byte in data:
        shifted.append((byte + shift) % mod)
    return shifted
        
def main():
    # Get arguments for input/ouput files, shift amounts, mod value
    parser = argparse.ArgumentParser("byteshift.py")
    parser.add_argument("-m", "--modulo", type=int, default=256, help="modulo, i.e. where the value wraps around. max is 256")
    parser.add_argument("infile", help="input file")
    parser.add_argument("outfile", help="output file")
    parser.add_argument("shift_amount", type=int, default=1, help="shift amount")

    args = parser.parse_args()
    
    # Get values
    shift = args.shift_amount
    mod = args.modulo

    print("Shifting " + args.infile + " by " + str(shift) + " (mod " + str(mod) + "), outputting into " + args.outfile)

    # Load the bytes
    data = bytearray()
    with open(args.infile, "rb") as f:
        byte = f.read(1)
        while byte:
            data.append(byte)
            byte = f.read(1)
            
    # Shift and output
    if len(data) == 0:
        print "Empty file"
        sys.exit(1)
    else:
        with open(args.outfile, "wb") as of:
            of.write(shift_bytes(data,shift,mod))
        
if __name__ == "__main__":
    main()

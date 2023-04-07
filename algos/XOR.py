def xor(data, bits, value):
    if len(data) * 8 % bits:
        raise ValueError
    binary = [bin(ord(c))[2:] for c in data]
    binary = ''.join(['0' * (8 - len(i)) + i for i in binary])
    xored_binary = ''
    for block_n in range(8 * len(data) // bits):
        block = binary[bits * block_n: bits * (block_n + 1)]
        xored = value ^ int(block, 2)
        temp = bin(xored)[2:]
        xored_binary += '0' * (8 - len(temp)) + temp
    print(xored_binary)
    return ''.join([chr(int(xored_binary[i * 8: (i + 1) * 8], 2)) for i in range(len(data))])


def encode(filename, bits, value):
    """
    returns string of encrypted text

    Required arguments:
    filename: name of file with data to encode.
    filename can be any binary file with whole number of bytes.
    bits: number of bits in block to be xored with value.
    value: number to xor symbols with.
    """
    with open(filename, 'r', encoding='utf-8') as input_file:
        data = input_file.read()
        try:
            return xor(data, bits, value)
        except ValueError:
            pass


def decode(filename, bits, value):
    """
    returns string of decrypted text

    Required arguments:
    filename: name of file with data to decode.
    filename can be any binary file with whole number of bytes.
    bits: number of bits in block to be xored with value.
    value: number to xor symbols with.
    """
    with open(filename, 'r', encoding='utf-8') as input_file:
        data = input_file.read()
        try:
            return xor(data, bits, value)
        except ValueError:
            pass


def get_bits():
    print('Print number of bits in each block')
    res = 0
    while not res:
        try:
            res = int(input())
            if not res:
                print('Must be integer > 0')
        except ValueError:
            print('Must be integer > 0')
    return res


def get_value(bits):
    print('Print number to xor blocks with')
    res = 0
    while not res:
        try:
            res = int(input())
            if res < 1 or res >= 2 ** bits:
                print('Must be integer between 0 and 2^bits')
        except ValueError:
            print('Must be integer > 0')
    return res


def process_decode(filename):
    bits = get_bits()
    value = get_value(bits)
    return decode(filename, bits, value)


def process_encode(filename):
    bits = get_bits()
    value = get_value(bits)
    return encode(filename, bits, value)


def bruteforce(filename):
    """
    Not implemented yet
    """
    return None  # TODO


def process_bruteforce(filename):
    """
    Not implemented yet
    """
    return None  # TODO

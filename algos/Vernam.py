def xor(data, key):
    res = ""
    if len(key) < len(data):
        print('Too short key')
        return None
    for i in range(len(data)):
        res += chr(ord(data[i]) ^ ord(key[i]))
    return res


def encode(filename, key):
    """
    returns string of encrypted text

    Required arguments:
    filename: name of file with data to encode.
    key:      sequence of symbols for xoring.
    """
    with open(filename, 'r', encoding='utf-8') as input_file:
        data = input_file.read()
        return xor(data, key)


def find_reverse_key(key):
    res = ""
    for c in key:
        res += chr(ord('a') + (26 - (ord(c) - ord('a'))) % 26)
    return res


def decode(filename, key):
    """
    returns string of decrypted text

    Required arguments:
    filename: name of file with data to decode.
    key:      sequence of symbols for xoring.
    """
    with open(filename, 'r', encoding='utf-8') as input_file:
        data = input_file.read()
        return xor(data, key)


def get_key():  # TODO: choose key input method
    key = ""
    while not key:
        key = input()
        if not key:
            print("key must have some letters in it")
    return key


def process_decode(filename):
    return decode(filename, get_key())


def process_encode(filename):
    return encode(filename, get_key())


def bruteforce(filename):
    raise TypeError("Cant bruteforce this algorithm")


def process_bruteforce(filename):
    raise TypeError

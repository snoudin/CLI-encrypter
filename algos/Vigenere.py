def rotate(data, key):
    res = ""
    for (c, ind) in enumerate(data):
        shift = ord(key[ind % len(key)]) - ord('a')
        if 'a' <= c <= 'z':
            res += chr(ord('a') + (shift + ord(c) - ord('a')) % 26)
        elif 'A' <= c <= 'Z':
            res += chr(ord('A') + (shift + ord(c) - ord('A')) % 26)
        else:
            res += c
    return res


def encode(filename, code):
    """
    returns string of encrypted text

    Required arguments:
    filename: name of file with data to encode.
    code:     key - sequence of letters, non-letters are being ignored.
    """
    with open(filename, 'r', encoding='utf-8') as input_file:
        data = input_file.read()
        return rotate(data, code)


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
    code:     key - sequence of letters, non-letters are being ignored.
    """
    with open(filename, 'r', encoding='utf-8') as input_file:
        data = input_file.read()
        return rotate(data, find_reverse_key(key))


def get_key():
    key = ""
    while not key:
        key = ''.join([c.lower() for c in input() if 'a' <= c.lower() <= 'z'])
        if not key:
            print("key must have some letters in it")
    return key


def process_decode(filename):
    return decode(filename, get_key())


def process_encode(filename):
    return encode(filename, get_key())


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

def rotate(data, shift, rules):
    to_shift = [False] * 3
    for rule in rules.split(','):
        if rule == 'letters':
            to_shift[0] = True
        elif rule == 'digits':
            to_shift[1] = True
        elif rule == 'all':
            to_shift = [True] * 3
    res = ""
    for character in data:
        if to_shift[2]:
            res += chr((ord(character) + shift) % 256)
        elif to_shift[0] and character.isalpha():
            if character.isupper():
                res += chr(ord('A') + (ord(character) - ord('A') + shift) % 26)
            else:
                res += chr(ord('a') + (ord(character) - ord('a') + shift) % 26)
        elif to_shift[1] and character.isdigit():
            res += chr(ord('0') + (ord(character) - ord('0') + shift) % 10)
    return res


def encode(filename, shift, rules="letters"):
    """
    returns string of encrypted text

    Required arguments:
    filename: name of file with data to encode.
    shift:    shift for ROT algorithm.

    Optional arguments:
    rules:    subset of next, divided with comma: letters, digits, all, defining symbols to rotate.
    """
    with open(filename, 'r', encoding='utf-8') as input_file:
        data = input_file.read()
        return rotate(data, shift, rules)


def decode(filename, shift, rules="letters"):
    """
    returns string of decrypted text

    Required arguments:
    filename: name of file with data to decode.
    shift:    shift for ROT algorithm.

    Optional arguments:
    rules:    subset of next, divided with comma: letters, digits, all, defining symbols to rotate.
    """
    with open(filename, 'r', encoding='utf-8') as input_file:
        data = input_file.read()
        return rotate(data, -1 * shift, rules)


def get_shift():
    print('Now I need rotation number (how much to shift letters to the right).'
          'It also can be negative, but can\'t be a zero')
    while True:
        res = input()
        try:
            return int(res)
        except ValueError:
            print('Shift must be a number')


def get_rule_number():
    res = 0
    while not res:
        try:
            res = int(input())
            if res < 1 or res > 3:
                res = 0
                print('Must be number 1-3')
        except ValueError:
            print('Must be number 1-3')
    return res


def get_rules():
    print('I can apply ROT with given shift in next ways:\n'
          '1. Rotate only letters\n'
          '2. Rotate letters and digits\n'
          '3. Rotate every character\n'
          'You only need to choose number')
    res = ['', 'letters', 'letters,digits', 'all']
    return res[get_rule_number()]


def process_decode(filename):
    shift = get_shift()
    rules = get_rules()
    return decode(filename, shift, rules)


def process_encode(filename):
    shift = get_shift()
    rules = get_rules()
    return encode(filename, shift, rules)


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

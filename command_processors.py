from settings import *
from algos import ROT, Vigenere, XOR, Vernam
from os.path import isfile


def get_file():
    print("Choose file")
    filename = ''
    while not isfile(filename):
        filename = input()
        if not isfile(filename):
            print("Given path is not file, try again")
    return filename


def get_algo():
    print("Possible names are:\n", *algorithm_list, sep='')
    algo = input()
    while algo.lower() not in [name.lower() for name in algorithm_list]:
        print(f"Incorrect algorithm name. Possible names are:\n", ' '.join(algorithm_list), sep='')
        algo = input()
    return algo


def print_result(result):
    print('Choose file to write result')
    while True:
        try:
            f = open(input(), 'w')
            f.write(result)
            f.close()
            print('done, returning to main menu')
            return True
        except Exception:
            print('Cannot open a file for writing')


def decode_processor():
    """
    parsing decoding arguments
    returns bool - False if need to exit, else True
    """
    filename = get_file()
    print("Choose decrypting algorithm")
    method = get_algo()
    result = eval(method + f'.process_decode("{filename}")')
    if result:
        print_result(result)
    else:
        print("decoding failed")
    return True


def encode_processor():
    """
    parsing encoding arguments
    returns bool - False if need to exit, else True
    """
    filename = get_file()
    print("Choose encrypting algorithm")
    method = get_algo()
    result = eval(method + f'.process_encode("{filename}")')
    if result:
        print_result(result)
    else:
        print("encoding failed")
    return True


def bruteforce_processor():
    """
    parsing encoding arguments
    returns bool - False if need to exit, else True
    """
    filename = get_file()
    print("Choose encrypting algorithm")
    method = get_algo()
    try:
        result = eval(method + f'.process_bruteforce("{filename}")')
        print_result(result)
    except TimeoutError:
        print('Timeout exceeded, no result')
    except TypeError:
        print('Unbreakable algorithm')
    return True  # TODO

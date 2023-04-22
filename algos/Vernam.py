from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


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


def get_key_from_file():
    print('input name of file with key')
    filename = ''
    while not filename:
        filename = input()
        try:
            data = open(filename, 'r').read()
            assert(len(data) > 0)
        except Exception:
            print('Bad file, try again')
            filename = ''


def get_key_from_console():
    print('input key')
    key = ""
    while not key:
        key = input()
        if not key:
            print("key must have some letters in it")
    return key


def get_key():
    print("Choose key input method:"
          "1 for input from console"
          "2 for input from file")
    method = 0
    while not method:
        try:
            method = int(input())
            assert(method > 0)
            assert(method < 3)
        except ValueError or AssertionError:
            print('Bad key input option, try again')
    if method == 1:
        return get_key_from_console()
    else:
        return get_key_from_file()


def process_decode(filename):
    return decode(filename, get_key())


def process_encode(filename):
    return encode(filename, get_key())


def bruteforce(filename):
    raise TypeError("Cant bruteforce this algorithm")


def process_bruteforce(filename):
    raise TypeError
    

class EncodeWidget(QWidget):
    def __init__(self):
        super().__init__()

        #input fields
        
        

class DecodeWidget(QWidget):
    def __init__(self):
        super().__init__()

        #input fields
        
        

class BruteforceWidget(QWidget):
    def __init__(self):
        super().__init__()
        txt = QLabel(self)
        txt.setText('Not implemented!')
        txt.setGeometry(200, 290, 200, 20)


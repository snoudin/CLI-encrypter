from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


def rotate(data, key):
    res = ""
    for (ind, c) in enumerate(data):
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
        return rotate(data, code.lower())


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
    

class EncodeWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        #input fields
        txt1 = QLabel(self)
        txt1.setText('key')
        key = QLineEdit(self)
        txt1.setGeometry(20, 20, 100, 25)
        key.setGeometry(20, 50, 200, 30)

        #input file
        def input():
            self.input = QFileDialog.getOpenFileName(self, 'OpenFile')[0]
            self.filename1.setText(self.input)

        txt3 = QLabel(self)
        txt3.setText('input file name')
        txt3.setGeometry(20, 160, 200, 20)
        self.filename1 = QLineEdit(self)
        self.filename1.setGeometry(20, 190, 300, 30)
        self.filename1.setReadOnly(True)
        file_btn = QPushButton(self)
        file_btn.setGeometry(20, 230, 300, 50)
        file_btn.clicked.connect(input)
        file_btn.setText('choose input file')

        #output file
        def output():
            self.output = QFileDialog.getOpenFileName(self, 'OpenFile')[0]
            self.filename2.setText(self.output)

        txt4 = QLabel(self)
        txt4.setText('output file name')
        txt4.setGeometry(20, 300, 200, 20)
        self.filename2 = QLineEdit(self)
        self.filename2.setGeometry(20, 340, 300, 30)
        self.filename2.setReadOnly(True)
        file_btn = QPushButton(self)
        file_btn.setGeometry(20, 380, 300, 50)
        file_btn.clicked.connect(output)
        file_btn.setText('choose output file')
        
        #work
        def run():
            if not key.text() or not self.input or not self.output:
                return
            with open(self.output, 'w') as file:
                print(encode(self.input, key.text()), file=file)

        btn = QPushButton(self)
        btn.setGeometry(20, 450, 100, 50)
        btn.setText('Encode')
        btn.clicked.connect(run)
    

class DecodeWidget(QWidget):
    def __init__(self):
        super().__init__()

        #input fields
        txt1 = QLabel(self)
        txt1.setText('key')
        key = QLineEdit(self)
        txt1.setGeometry(20, 20, 100, 25)
        key.setGeometry(20, 50, 200, 30)
        
        #input file
        def input():
            self.input = QFileDialog.getOpenFileName(self, 'OpenFile')[0]
            self.filename1.setText(self.input)

        txt3 = QLabel(self)
        txt3.setText('input file name')
        txt3.setGeometry(20, 160, 200, 20)
        self.filename1 = QLineEdit(self)
        self.filename1.setGeometry(20, 190, 300, 30)
        self.filename1.setReadOnly(True)
        file_btn = QPushButton(self)
        file_btn.setGeometry(20, 230, 300, 50)
        file_btn.clicked.connect(input)
        file_btn.setText('choose input file')

        #output file
        def output():
            self.output = QFileDialog.getOpenFileName(self, 'OpenFile')[0]
            self.filename2.setText(self.output)

        txt4 = QLabel(self)
        txt4.setText('output file name')
        txt4.setGeometry(20, 300, 200, 20)
        self.filename2 = QLineEdit(self)
        self.filename2.setGeometry(20, 340, 300, 30)
        self.filename2.setReadOnly(True)
        file_btn = QPushButton(self)
        file_btn.setGeometry(20, 380, 300, 50)
        file_btn.clicked.connect(output)
        file_btn.setText('choose output file')
        
        #work
        def run():
            if not key.text() or not self.input or not self.output:
                return
            with open(self.output, 'w') as file:
                print(decode(self.input, key.text()), file=file)

        btn = QPushButton(self)
        btn.setGeometry(20, 450, 100, 50)
        btn.setText('Decode')
        btn.clicked.connect(run)


class BruteforceWidget(QWidget):
    def __init__(self):
        super().__init__()
        txt = QLabel(self)
        txt.setText('Not implemented!')
        txt.setGeometry(200, 290, 200, 20)


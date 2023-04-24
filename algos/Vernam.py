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
        txt1 = QLabel(self)
        txt1.setText('write key here')
        key = QLineEdit(self)
        txt1.setGeometry(20, 80, 200, 25)
        key.setGeometry(20, 110, 200, 30)
        
        opt1 = QRadioButton('paste key here', self)
        opt2 = QRadioButton('load key from file', self)
        group = QButtonGroup(self)
        group.addButton(opt1)
        group.addButton(opt2)
        opt1.setGeometry(20, 20, 200, 25)
        opt2.setGeometry(300, 20, 200, 25)
        
        txt2 = QLabel(self)
        txt2.setText('choose file with key here')
        txt2.setGeometry(300, 80, 200, 25)
        self.keyfile = QLineEdit(self)
        self.keyfile.setGeometry(300, 110, 260, 30)
        self.keyfile.setReadOnly(True)

        def key():
            self.key = QFileDialog.getOpenFileName(self, 'OpenFile')[0]
            self.keyfile.setText(self.key)

        key_btn = QPushButton(self)
        key_btn.setGeometry(300, 150, 260, 40)
        key_btn.clicked.connect(key)
        key_btn.setText('choose file with key')

        #input file
        def input():
            self.input = QFileDialog.getOpenFileName(self, 'OpenFile')[0]
            self.filename1.setText(self.input)

        txt3 = QLabel(self)
        txt3.setText('input file name')
        txt3.setGeometry(20, 200, 200, 20)
        self.filename1 = QLineEdit(self)
        self.filename1.setGeometry(20, 230, 300, 30)
        self.filename1.setReadOnly(True)
        file_btn = QPushButton(self)
        file_btn.setGeometry(20, 270, 300, 50)
        file_btn.clicked.connect(input)
        file_btn.setText('choose input file')

        #output file
        def output():
            self.output = QFileDialog.getOpenFileName(self, 'OpenFile')[0]
            self.filename2.setText(self.output)

        txt4 = QLabel(self)
        txt4.setText('output file name')
        txt4.setGeometry(20, 340, 200, 20)
        self.filename2 = QLineEdit(self)
        self.filename2.setGeometry(20, 380, 300, 30)
        self.filename2.setReadOnly(True)
        file_btn = QPushButton(self)
        file_btn.setGeometry(20, 420, 300, 50)
        file_btn.clicked.connect(output)
        file_btn.setText('choose output file')
        
        #work
        def run(): # TODO
            if not self.input or not self.output:
                return
            value = ""
            if opt1.isChecked():
                value = key.text()
            else:
                value = open(self.key, 'r').read()
            if not value:
                return
            with open(self.output, 'w') as file:
                print(encode(self.input, value), file=file)

        btn = QPushButton(self)
        btn.setGeometry(20, 490, 100, 50)
        btn.setText('Encode')
        btn.clicked.connect(run)
        

class DecodeWidget(QWidget):
    def __init__(self):
        super().__init__()

        #input fields
        txt1 = QLabel(self)
        txt1.setText('write key here')
        key = QLineEdit(self)
        txt1.setGeometry(20, 80, 200, 25)
        key.setGeometry(20, 110, 200, 30)
        
        opt1 = QRadioButton('paste key here', self)
        opt2 = QRadioButton('load key from file', self)
        group = QButtonGroup(self)
        group.addButton(opt1)
        group.addButton(opt2)
        opt1.setGeometry(20, 20, 200, 25)
        opt2.setGeometry(300, 20, 200, 25)
        
        txt2 = QLabel(self)
        txt2.setText('choose file with key here')
        txt2.setGeometry(300, 80, 200, 25)
        self.keyfile = QLineEdit(self)
        self.keyfile.setGeometry(300, 110, 260, 30)
        self.keyfile.setReadOnly(True)

        def key():
            self.key = QFileDialog.getOpenFileName(self, 'OpenFile')[0]
            self.keyfile.setText(self.key)

        key_btn = QPushButton(self)
        key_btn.setGeometry(300, 150, 260, 40)
        key_btn.clicked.connect(key)
        key_btn.setText('choose file with key')

        #input file
        def input():
            self.input = QFileDialog.getOpenFileName(self, 'OpenFile')[0]
            self.filename1.setText(self.input)

        txt3 = QLabel(self)
        txt3.setText('input file name')
        txt3.setGeometry(20, 200, 200, 20)
        self.filename1 = QLineEdit(self)
        self.filename1.setGeometry(20, 230, 300, 30)
        self.filename1.setReadOnly(True)
        file_btn = QPushButton(self)
        file_btn.setGeometry(20, 270, 300, 50)
        file_btn.clicked.connect(input)
        file_btn.setText('choose input file')

        #output file
        def output():
            self.output = QFileDialog.getOpenFileName(self, 'OpenFile')[0]
            self.filename2.setText(self.output)

        txt4 = QLabel(self)
        txt4.setText('output file name')
        txt4.setGeometry(20, 340, 200, 20)
        self.filename2 = QLineEdit(self)
        self.filename2.setGeometry(20, 380, 300, 30)
        self.filename2.setReadOnly(True)
        file_btn = QPushButton(self)
        file_btn.setGeometry(20, 420, 300, 50)
        file_btn.clicked.connect(output)
        file_btn.setText('choose output file')
        
        #work
        def run(): # TODO
            if not self.input or not self.output:
                return
            value = ""
            if opt1.isChecked():
                value = key.text()
            else:
                value = open(self.key, 'r').read()
            if not value:
                return
            with open(self.output, 'w') as file:
                print(decode(self.input, value), file=file)

        btn = QPushButton(self)
        btn.setGeometry(20, 490, 100, 50)
        btn.setText('Decode')
        btn.clicked.connect(run)
     

class BruteforceWidget(QWidget):
    def __init__(self):
        super().__init__()
        txt = QLabel(self)
        txt.setText('Basically impossible')
        txt.setGeometry(200, 290, 200, 20)


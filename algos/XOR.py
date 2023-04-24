from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

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
            assert(res > 0)
            assert(res < 2 ** bits)
        except ValueError or AssertionError:
            print('Must be integer between 0 and 2^bits')
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


class EncodeWidget(QWidget):
    def __init__(self):
        super().__init__()

        #input fields
        txt1 = QLabel(self)
        txt1.setText('bits')
        txt2 = QLabel(self)
        txt2.setText('value')

        bits = QLineEdit(self)
        value = QLineEdit(self)
        txt1.setGeometry(20, 20, 100, 25)
        txt2.setGeometry(20, 80, 100, 25)
        bits.setGeometry(20, 50, 100, 20)
        value.setGeometry(20, 110, 100, 20)
        bits.setValidator(QIntValidator())
        value.setValidator(QIntValidator())
        
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
            if not bits.text() or not value.text() or not self.input or not self.output:
                return
            with open(self.output, 'w') as file:
                print(encode(self.input, int(bits.text()), int(value.text())), file=file)

        btn = QPushButton(self)
        btn.setGeometry(20, 450, 100, 50)
        btn.setText('Encode')
        btn.clicked.connect(run)


class DecodeWidget(QWidget):
    def __init__(self):
        super().__init__()

        #input fields
        txt1 = QLabel(self)
        txt1.setText('bits')
        txt2 = QLabel(self)
        txt2.setText('value')

        bits = QLineEdit(self)
        value = QLineEdit(self)
        txt1.setGeometry(20, 20, 100, 25)
        txt2.setGeometry(20, 80, 100, 25)
        bits.setGeometry(20, 50, 100, 20)
        value.setGeometry(20, 110, 100, 20)
        bits.setValidator(QIntValidator())
        value.setValidator(QIntValidator())
        
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
            if not bits.text() or not value.text() or not self.input or not self.output:
                return
            with open(self.output, 'w') as file:
                print(decode(self.input, int(bits.text()), int(value.text())), file=file)

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

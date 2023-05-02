from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from choosers import statistical


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
        else:
            res += character
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


def bruteforce(filename, rules='letters'):
    options = [None for _ in range(26)]
    for shift in range(26):
        options[shift] = decode(filename, shift, rules)
    return statistical(options)


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


def process_bruteforce(filename):
    rules = get_rules()
    return bruteforce(filename, rules)
    

class EncodeWidget(QWidget):
    def __init__(self):
        super().__init__()

        #input fields
        txt1 = QLabel(self)
        txt1.setText('rotation')
        rotation = QLineEdit(self)
        txt1.setGeometry(20, 20, 100, 25)
        rotation.setGeometry(20, 50, 100, 20)
        rotation.setValidator(QIntValidator())

        txt2 = QLabel(self)
        txt2.setText('characters to rotate')
        txt2.setGeometry(300, 20, 300, 25)
        
        options = [QRadioButton('letters', self), QRadioButton('digits', self), \
                  QRadioButton('letters and digits', self), QRadioButton('all', self)]
        self.group = QButtonGroup(self)
        for (ind, opt) in enumerate(options):
            self.group.addButton(opt)
            opt.setGeometry(300, 60 + 30 * ind, 200, 25)
        self.rules = ['letters', 'digits', 'letters,digits', 'all']
        
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
            if not rotation.text() or not self.input or not self.output or self.group.checkedId() == -1:
                return
            with open(self.output, 'w') as file:
                print(encode(self.input, int(rotation.text()), self.rules[-2 - self.group.checkedId()]), file=file)

        btn = QPushButton(self)
        btn.setGeometry(20, 450, 100, 50)
        btn.setText('Encode')
        btn.clicked.connect(run)


class DecodeWidget(QWidget):
    def __init__(self):
        super().__init__()

        #input fields
        txt1 = QLabel(self)
        txt1.setText('rotation')
        rotation = QLineEdit(self)
        txt1.setGeometry(20, 20, 100, 25)
        rotation.setGeometry(20, 50, 100, 20)
        rotation.setValidator(QIntValidator())

        txt2 = QLabel(self)
        txt2.setText('characters to rotate')
        txt2.setGeometry(300, 20, 300, 25)
        
        options = [QRadioButton('letters', self), QRadioButton('digits', self), \
                  QRadioButton('letters and digits', self), QRadioButton('all', self)]
        self.group = QButtonGroup(self)
        for (ind, opt) in enumerate(options):
            self.group.addButton(opt)
            opt.setGeometry(300, 60 + 30 * ind, 200, 25)
        self.rules = ['letters', 'digits', 'letters,digits', 'all']
        
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
            if not rotation.text() or not self.input or not self.output or self.group.checkedId() == -1:
                return
            with open(self.output, 'w') as file:
                print(decode(self.input, int(rotation.text()), self.rules[-2 - self.group.checkedId()]), file=file)

        btn = QPushButton(self)
        btn.setGeometry(20, 450, 100, 50)
        btn.setText('Decode')
        btn.clicked.connect(run)

   
        

class BruteforceWidget(QWidget):
    def __init__(self):
        super().__init__()
        txt2 = QLabel(self)
        txt2.setText('characters to rotate')
        txt2.setGeometry(20, 20, 300, 25)
        
        options = [QRadioButton('letters', self), QRadioButton('digits', self), \
                  QRadioButton('letters and digits', self), QRadioButton('all', self)]
        self.group = QButtonGroup(self)
        for (ind, opt) in enumerate(options):
            self.group.addButton(opt)
            opt.setGeometry(20, 60 + 30 * ind, 200, 25)
        self.rules = ['letters', 'digits', 'letters,digits', 'all']
        
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
        def run():
            if not self.input or not self.output or self.group.checkedId() == -1:
                return
            with open(self.output, 'w') as file:
                print(bruteforce(self.input, self.rules[-2 - self.group.checkedId()]), file=file)

        btn = QPushButton(self)
        btn.setGeometry(20, 490, 100, 50)
        btn.setText('Crack!')
        btn.clicked.connect(run)



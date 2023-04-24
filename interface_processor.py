from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from settings import *
exec(f"from algos import {', '.join(gui_algorithm_list)}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Encrypter')
        self.setFixedSize(QSize(800, 600))

        self.mode = ''
        self.algo = ''

        # mode block
        txt1 = QLabel(self)
        txt1.setText('Working mode')
        txt1.setGeometry(20, 15, 200, 25)

        rb_encrypt = QRadioButton('Encrypt', self)
        rb_encrypt.move(20, 50)
        rb_decrypt = QRadioButton('Decrypt', self)
        rb_decrypt.move(20, 80)
        rb_bruteforce = QRadioButton('Bruteforce', self)
        rb_bruteforce.move(20, 110)

        mode_group = QButtonGroup(self)
        mode_group.addButton(rb_encrypt)
        mode_group.addButton(rb_decrypt)
        mode_group.addButton(rb_bruteforce)
        mode_group.buttonClicked.connect(self.set_mode)

        # algorithm block

        txt2 = QLabel(self)
        txt2.setText('Encrypting algorithm')
        txt2.setGeometry(20, 165, 200, 25)

        algo_group = QButtonGroup(self)
        algo_buttons = [QRadioButton(name, self) for name in gui_algorithm_list]
        for (ind, btn) in enumerate(algo_buttons):
            btn.move(20, 200 + 30 * ind)
            algo_group.addButton(btn)
        algo_group.buttonClicked.connect(self.set_algo)
        
        run_button = QPushButton(self)
        run_button.setText('run')
        run_button.setGeometry(50, 220 + 30 * len(algo_buttons), 100, 30)
        run_button.clicked.connect(self.run)

        # algo processors stack
        

        self.stack = QStackedWidget(self)
        self.stack.addWidget(QWidget())
        self.stack.setGeometry(200, 0, 600, 600)
        for name in gui_algorithm_list:
            self.stack.addWidget(eval(f"{name}.EncodeWidget")())
            self.stack.addWidget(eval(f"{name}.DecodeWidget")())
            self.stack.addWidget(eval(f"{name}.BruteforceWidget")())

        self.index = dict()
        for (ind, name) in enumerate(gui_algorithm_list):
            self.index[(name, 'Encrypt')] = 3 * ind + 1
            self.index[(name, 'Decrypt')] = 3 * ind + 2
            self.index[(name, 'Bruteforce')] = 3 * ind + 3
        
    def set_mode(self, btn):
        self.mode = btn.text()

    def set_algo(self, btn):
        self.algo = btn.text()

    def run(self):
        if not self.algo or not self.mode:
            return
        self.stack.setCurrentIndex(self.index[(self.algo, self.mode)])
        

def interface_processor():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
    return True

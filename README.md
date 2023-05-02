## Console line application that can encrypt and decrypt files with ROT, Vernam, Vigenere and XOR ciphers.

To start use ./run.sh

### ANY encoding algorithms can be added in following way:

##### I. Adding CLI version:

Put into algos/ file with following functions:
1. process_decode(filename)
2. process_encode(filename)
3. process_bruteforce(filename)

Update cli_algorithm_list in settings py with name of your module.

Every data piece except filename your command processor should ask thru input() itself.
Is's highly recommended to implement process_decode thru decode(filename, {other needed data}) function and same with other processors.
This way it's much simpler to implement gui version and use you algo file as api.

##### II Adding GUI version:

Put into algos/ (or just update existing) file with following classes:
1. DecodeWidget(QWidget)
2. EncodeWidget(QWidget)
3. BruteforceWidget(QWidget)

Update gui_algorithm_list in settings py with name of your module.

Your widget should fit in 600px X 600px size. Every data piece you need (including filename to process) should be asked thru interface of QT widget.

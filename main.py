from command_processors import *
from interface_processor import interface_processor

if __name__ == '__main__':
    running = True
    print('Choose mode or print \'help\'')
    while running:
        command = input()
        if command in ['q', 'quit', 'exit']:
            running = False
        elif command in ['h', 'help']:
            print(open('helpnote.txt', 'r').read())
        elif command in ['d', 'decode']:
            if not decode_processor():
                running = False
        elif command in ['e', 'encode']:
            if not encode_processor():
                running = False
        elif command in ['c', 'crack', 'b', 'bruteforce']:
            if not bruteforce_processor():
                running = False
        elif command in ['i', 'interface']:
            if not interface_processor():
                running = False
        else:
            print('Unknown command\n'
                  'If you need list of possible commands, type \"help\"')



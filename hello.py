import sys


def main():
    '''
    - takes a command line arguments
    - problems:
        1. If no argmuent is specified
            IndexError: list index out of range
        2. If more than one argument is passed
            Will consider only the first arg 
    '''
    print(f'Hello there {sys.argv[1]}')


if __name__ == '__main__':
    main()

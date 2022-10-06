import argparse


def main():
    '''
    - uses `argparse` argument parser to exceptions 
    - from previous issues
    '''
    parser = argparse.ArgumentParser()
    # defines one positional argument named person
    parser.add_argument('person')
    args = parser.parse_args()
    print(f'Hello there {args.person}')


if __name__ == '__main__':
    main()

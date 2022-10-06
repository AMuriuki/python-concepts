import argparse


def main(argv=None):
    '''
    - uses `argparse` argument parser to handle exceptions 
    - from previous issues
    '''
    parser = argparse.ArgumentParser()
    # defines one positional argument named person
    parser.add_argument('person')
    args = parser.parse_args(argv)
    print(f'Hello there {args.person}')


if __name__ == '__main__':
    main()

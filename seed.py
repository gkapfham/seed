""" seed downloads a JSON file from SimpleForm and then analyzes it """

import argparse
import sys


def parse_seed_arguments(args):
    """ Parses the arguments provided on the command-line """
    parser = argparse.ArgumentParser()

    parser.add_argument("--token",
                        help="SimpleForm API token",
                        required=False)

    parser.add_argument("--verbose",
                        help="Verbose mode",
                        action="store_false")

    utterson_args = parser.parse_args(args)
    return utterson_args


if __name__ == '__main__':
    """Run the program with the command-line arguments """
    utterson_args = parse_seed_arguments(sys.argv[1:])

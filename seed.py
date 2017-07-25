""" seed downloads a JSON file from SimpleForm and then analyzes it """

import argparse
import sys


def parse_seed_arguments(args):
    """ Parses the arguments provided on the command-line """
    parser = argparse.ArgumentParser()

    parser.add_argument("--token",
                        help="SimpleForm API token",
                        required=False)

    parser.add_argument("--download-json",
                        help="Download the JSON file",
                        action="store_false")

    parser.add_argument("--create-list",
                        help="Create the mailing list",
                        action="store_false")

    parser.add_argument("--show-respondents",
                        help="Show the SEED Respondents",
                        action="store_false")

    parser.add_argument("--verbose",
                        help="Verbose mode",
                        action="store_false")

    utterson_args = parser.parse_args(args)
    return utterson_args


def verify_seed_arguments(args):
    """ Checks if the seed_arguments are correct """
    verified = True
    if args.download_json is not None and args.token is None:
        verified = False
    return verified


if __name__ == '__main__':
    """Run the program with the command-line arguments """
    seed_arguments = parse_seed_arguments(sys.argv[1:])
    verified = verify_seed_arguments(seed_arguments)

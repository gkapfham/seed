""" seed downloads a JSON file from SimpleForm and then analyzes it """

import argparse
import sys


def parse_seed_arguments(args):
    """ Parses the arguments provided on the command-line """
    seed_parser = argparse.ArgumentParser()

    seed_parser.add_argument("--token",
                        help="SimpleForm API token",
                        required=False)

    seed_parser.add_argument("--download-json",
                        help="Download the JSON file",
                        action="store_false")

    seed_parser.add_argument("--create-list",
                        help="Create the mailing list",
                        action="store_false")

    seed_parser.add_argument("--show-respondents",
                        help="Show the SEED Respondents",
                        action="store_false")

    seed_parser.add_argument("--verbose",
                        help="Verbose mode",
                        action="store_false")

    # verify the arguments, printing help message if they are wrong
    seed_arguments = seed_parser.parse_args(args)
    return seed_arguments, seed_parser


def verify_seed_arguments(args):
    """ Checks if the seed_arguments are correct """
    verified_arguments = True
    if args.download_json is not None and args.token is None:
        verified_arguments = False
    elif args.create_list is not None and args.token is None:
        verified_arguments = False
    return verified_arguments


if __name__ == '__main__':
    seed_arguments, seed_parser = parse_seed_arguments(sys.argv[1:])
    did_verify_arguments = verify_seed_arguments(seed_arguments)
    if did_verify_arguments is False:
        print("Incorrect arguments to seed.py")
        seed_parser.print_help()

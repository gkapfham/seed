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

    # verify the arguments, printing help message if they are wrong
    seed_arguments = parser.parse_args(args)
    verified_arguments = verify_seed_arguments(seed_arguments)
    if verified_arguments is False:
        print("Incorrect arguments")
        parser.print_help()
    return seed_arguments


def verify_seed_arguments(args):
    """ Checks if the seed_arguments are correct """
    verified_arguments = True
    if args.download_json is not None and args.token is None:
        verified_arguments = False
    elif args.create_list is not None and args.token is None:
        verified_arguments = False
    return verified_arguments


if __name__ == '__main__':
    seed_arguments = parse_seed_arguments(sys.argv[1:])

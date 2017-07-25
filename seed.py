""" seed.py downloads a JSON file from SimpleForm and then analyzes it """

import argparse
import sys

import seed_download
import seed_process

def parse_seed_arguments(args):
    """ Parses the arguments provided on the command-line """
    seed_parser = argparse.ArgumentParser()

    seed_parser.add_argument("--token",
                             help="SimpleForm API token",
                             required=False)

    seed_parser.add_argument("--download-json",
                             help="Download the JSON file",
                             action="store_true")

    seed_parser.add_argument("--create-list",
                             help="Create the mailing list",
                             action="store_true")

    seed_parser.add_argument("--show-respondents",
                             help="Show the SEED Respondents",
                             action="store_true")

    seed_parser.add_argument("--verbose",
                             help="Verbose mode",
                             action="store_true")

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
    # parse and verify the arguments
    seed_arguments, seed_parser = parse_seed_arguments(sys.argv[1:])
    did_verify_arguments = verify_seed_arguments(seed_arguments)
    if seed_arguments.verbose:
        print(seed_arguments)
    # print("After verified arguments")

    # arguments were not verified, so print help message
    if did_verify_arguments is False:
        # print("Incorrect arguments to seed.py")
        seed_parser.print_help()
    # arguments were verified, so perform designated action
    else:
        # download the JSON file from SimpleForm and remove the email addresses
        if seed_arguments.download_json is True:
            seed_json = seed_download.seed_download(seed_arguments.token)
            # print("Before internal dictionary")
            seed_internal_dictionary = seed_process.seed_process_create_internal_dictionary(seed_json)
            seed_no_subscriptions = seed_process.seed_process_remove_email_subscriptions(seed_internal_dictionary)
            seed_no_email_no_subscriptions = seed_process.seed_process_remove_emails(seed_no_subscriptions)
            print(seed_no_email_no_subscriptions)

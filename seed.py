""" seed.py downloads a JSON file from SimpleForm and then analyzes it """

import argparse
import os
import sys

import seed_create
import seed_display
import seed_download
import seed_process
import seed_gensim

INDENT = "  "
SLASH = "/"
DEFAULT_TOPIC_NUMBER = 3
DEFAULT_PASS_NUMBER = 10

SEED_HOME = "SEED_HOME"
SEED_SIMPLEFORM_TOKEN = "SEED_SIMPLEFORM_TOKEN"


def parse_seed_arguments(args):
    """ Parses the arguments provided on the command-line """
    seed_parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    seed_parser.add_argument(
        "--token", help="SimpleForm API token", required=False)

    seed_parser.add_argument(
        "--analyze-advice",
        help="Analyze the 'advice' question",
        action="store_true")

    seed_parser.add_argument(
        "--analyze-challenge",
        help="Analyze the 'challenge' question",
        action="store_true")

    seed_parser.add_argument(
        "--analyze-facts",
        help="Analyze the 'fact' question",
        action="store_true")

    seed_parser.add_argument(
        "--num-topics",
        help="Topics in the LDA model",
        type=int,
        default=DEFAULT_TOPIC_NUMBER,
        required=False)

    seed_parser.add_argument(
        "--num-passes",
        help="Passes when creating the LDA model",
        type=int,
        default=DEFAULT_PASS_NUMBER,
        required=False)

    seed_parser.add_argument(
        "--create-list", help="Create the mailing list", action="store_true")

    seed_parser.add_argument(
        "--download-json", help="Download the JSON file", action="store_true")

    seed_parser.add_argument(
        "--show-respondents",
        help="Show the SEED respondents",
        action="store_true")

    seed_parser.add_argument(
        "--show-sample", help="Show a SEED sample", action="store_true")

    seed_parser.add_argument(
        "--verbose", help="Verbose mode", action="store_true")

    seed_parser.add_argument(
        "--visualize",
        help="Create an interactive visualization",
        action="store_true")

    # verify the arguments, printing help message if they are wrong
    seed_arguments = seed_parser.parse_args(args)
    return seed_arguments, seed_parser


def get_seed_simpleform_token():
    """ Returns the SEED_SIMPLEFORM_TOKEN """
    simple_form_token = os.environ.get(SEED_SIMPLEFORM_TOKEN)
    return simple_form_token


def get_seed_home():
    """ Returns the SEED_HOME """
    current_seed_home = os.environ.get(SEED_HOME)
    had_to_set = False
    # the current SEED_HOME is acceptable, so use it
    if verify_seed_home(current_seed_home) is not False:
        seed_home = current_seed_home
    # the current SEED_HOME is not okay, so guess at one
    else:
        seed_home = os.getcwd() + SLASH
        had_to_set = True
    return seed_home, had_to_set


def verify_performing_lda(args):
    """ Checks if the command-line arguments ask for LDA """
    performing_lda = False
    if args.analyze_advice is True or args.analyze_challenge is True or args.analyze_facts is True:
        performing_lda = True
    return performing_lda


def verify_seed_arguments(args):
    """ Checks if the seed_arguments are correct """
    verified_arguments = True
    if args.download_json is not False and args.token is None:
        verified_arguments = False
    elif args.create_list is not False and args.token is None:
        verified_arguments = False
    elif args.num_topics != DEFAULT_TOPIC_NUMBER and verify_performing_lda(args) is False:
        verified_arguments = False
    elif args.visualize is not False and verify_performing_lda(args) is False:
        verified_arguments = False
    return verified_arguments


def verify_seed_home(current_seed_home):
    """ Verifies that the SEED_HOME environment variable is set correctly """
    verified_seed_home = False
    if current_seed_home is not None and current_seed_home.endswith(
            SLASH) is True:
        verified_seed_home = True
    return verified_seed_home


def display_welcome_message():
    """ Display a welcome message """
    print("SEED: Educational Discussions with Software Engineers")
    print("http://www.cs.allegheny.edu/sites/gkapfham/seed/")
    print()


def perform_gensim_analysis(seed_arguments, response_list):
    """ Use seed_gensim functions to create and analyze a topic model """
    if seed_arguments.num_topics is not None:
        num_topics_requested = seed_arguments.num_topics
    else:
        num_topics_requested = DEFAULT_TOPIC_NUMBER
    gensim_topic_model, topic_model_corpus, topic_model_dictionary, texts_to_analyze = seed_gensim.create_topic_model(
        seed_arguments, response_list)
    seed_gensim.show_topic_model_textually(
        gensim_topic_model,
        topic_model_corpus,
        texts_to_analyze,
        num_topics=num_topics_requested)
    if seed_arguments.visualize is True:
        seed_gensim.show_topic_model_visually(
            gensim_topic_model, topic_model_corpus, topic_model_dictionary)


if __name__ == '__main__':
    display_welcome_message()
    current_seed_home, had_to_set = get_seed_home()
    if had_to_set is True:
        print(INDENT + SEED_HOME,
              "is not set or not set with a trailing slash.")
        print(INDENT + "Using", current_seed_home, "instead.")
        print()
    # parse and verify the arguments
    seed_arguments, seed_parser = parse_seed_arguments(sys.argv[1:])
    did_verify_arguments = verify_seed_arguments(seed_arguments)
    if seed_arguments.verbose:
        print(seed_arguments)

    # arguments were not verified, so print help message
    if did_verify_arguments is False:
        print("Could not verify the command-line arguments!")
        seed_parser.print_help()
    # arguments were verified, so perform designated action
    else:
        # TASK: download the JSON file from SimpleForm
        # remove the email addresses
        # remove the subscriptions from other forms
        # save the final list of dictionaries to a JSON file
        if seed_arguments.download_json is True:
            seed_json = seed_download.seed_download(seed_arguments.token)
            seed_internal_dictionary_list = seed_process.seed_process_create_internal_dictionary(
                seed_json)
            print(INDENT, "Downloaded a total of",
                  len(seed_internal_dictionary_list), "entries")
            seed_process.seed_process_remove_email_subscriptions(
                seed_internal_dictionary_list)
            seed_process.seed_process_remove_emails(
                seed_internal_dictionary_list)
            print(INDENT, "Saved a total of",
                  len(seed_internal_dictionary_list), "entries")
            seed_download.seed_save_json(seed_internal_dictionary_list)
            if seed_arguments.verbose:
                print(seed_internal_dictionary_list)
        # TASK: Create the mailing list for the SEED respondents
        elif seed_arguments.create_list is True:
            seed_json = seed_download.seed_download(seed_arguments.token)
            seed_internal_dictionary_list = seed_process.seed_process_create_internal_dictionary(
                seed_json)
            list_of_email = seed_create.create_mailing_list(
                seed_internal_dictionary_list)
            seed_download.seed_save_mailing_list(list_of_email)
        # TASK: Show all of the respondents to the SEED survey
        elif seed_arguments.show_respondents is True:
            seed_dictionary_list = seed_download.seed_load()
            seed_display.seed_display_respondents(seed_dictionary_list)
        # TASK: Show a sample response to the SEED survey
        elif seed_arguments.show_sample is True:
            seed_dictionary_list = seed_download.seed_load()
            seed_display.seed_display_sample(seed_dictionary_list)
        # TASK: Analyze the responses to the 'fact' question
        elif seed_arguments.analyze_facts is True:
            seed_dictionary_list = seed_download.seed_load()
            fact_response_list = seed_create.create_fact_answer_list(
                seed_dictionary_list)
            perform_gensim_analysis(seed_arguments, fact_response_list)
        # TASK: Analyze the responses to the 'advice' question
        elif seed_arguments.analyze_advice is True:
            seed_dictionary_list = seed_download.seed_load()
            advice_response_list = seed_create.create_advice_answer_list(
                seed_dictionary_list)
            perform_gensim_analysis(seed_arguments, advice_response_list)
        # TASK: Analyze the responses to the 'advice' question
        elif seed_arguments.analyze_challenge is True:
            seed_dictionary_list = seed_download.seed_load()
            challenge_response_list = seed_create.create_challenge_answer_list(
                seed_dictionary_list)
            perform_gensim_analysis(seed_arguments, challenge_response_list)

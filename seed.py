""" seed.py downloads a JSON file from SimpleForm and then analyzes it """

import argparse
import sys

import seed_create
import seed_display
import seed_download
import seed_process
import seed_gensim

INDENT = "  "
DEFAULT_TOPIC_NUMBER = 5

def parse_seed_arguments(args):
    """ Parses the arguments provided on the command-line """
    seed_parser = argparse.ArgumentParser()

    seed_parser.add_argument("--token",
                             help="SimpleForm API token",
                             required=False)

    seed_parser.add_argument("--analyze-advice",
                             help="Analyze responses to the 'advice' question",
                             action="store_true")

    seed_parser.add_argument("--analyze-challenge",
                             help="Analyze responses to the 'challenge' question",
                             action="store_true")

    seed_parser.add_argument("--analyze-facts",
                             help="Analyze responses to the 'fact' question",
                             action="store_true")

    seed_parser.add_argument("--num-topics",
                             help="Number of topics in the LDA model",
                             type=int,
                             required=False)

    seed_parser.add_argument("--create-list",
                             help="Create the mailing list",
                             action="store_true")

    seed_parser.add_argument("--download-json",
                             help="Download the JSON file",
                             action="store_true")

    seed_parser.add_argument("--show-respondents",
                             help="Show the SEED respondents",
                             action="store_true")

    seed_parser.add_argument("--show-sample",
                             help="Show a SEED sample",
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
    if args.download_json is not False and args.token is None:
        verified_arguments = False
    elif args.create_list is not False and args.token is None:
        verified_arguments = False
    return verified_arguments


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

    gensim_topic_model, topic_model_corpus, texts_to_analyze = seed_gensim.create_topic_model(response_list, num_topics_requested)
    seed_gensim.show_topic_model_textually(gensim_topic_model,
                                           topic_model_corpus,
                                           texts_to_analyze,
                                           num_topics=num_topics_requested)


if __name__ == '__main__':
    display_welcome_message()
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
            seed_internal_dictionary_list = seed_process.seed_process_create_internal_dictionary(seed_json)
            print(INDENT, "Downloaded a total of", len(seed_internal_dictionary_list), "entries")
            seed_process.seed_process_remove_email_subscriptions(seed_internal_dictionary_list)
            seed_process.seed_process_remove_emails(seed_internal_dictionary_list)
            print(INDENT, "Saved a total of", len(seed_internal_dictionary_list), "entries")
            seed_download.seed_save_json(seed_internal_dictionary_list)
            if seed_arguments.verbose:
                print(seed_internal_dictionary_list)
        # TASK: Create the mailing list for the SEED respondents
        elif seed_arguments.create_list is True:
            seed_json = seed_download.seed_download(seed_arguments.token)
            seed_internal_dictionary_list = seed_process.seed_process_create_internal_dictionary(seed_json)
            list_of_email = seed_create.create_mailing_list(seed_internal_dictionary_list)
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
            fact_response_list = seed_create.create_fact_answer_list(seed_dictionary_list)
            perform_gensim_analysis(seed_arguments, fact_response_list)
        # TASK: Analyze the responses to the 'advice' question
        elif seed_arguments.analyze_advice is True:
            seed_dictionary_list = seed_download.seed_load()
            advice_response_list = seed_create.create_advice_answer_list(seed_dictionary_list)
            perform_gensim_analysis(seed_arguments, advice_response_list)
        # TASK: Analyze the responses to the 'advice' question
        elif seed_arguments.analyze_challenge is True:
            seed_dictionary_list = seed_download.seed_load()
            challenge_response_list = seed_create.create_challenge_answer_list(seed_dictionary_list)
            perform_gensim_analysis(seed_arguments, challenge_response_list)

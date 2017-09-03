""" seed_display.py displays details about the SEED data """

import json
import random

import seed
import seed_lookup
import seed_process

MARKDOWN_HEADER_MARKER = "---"
MARKDOWN_QUOTE = "\""


def seed_display_respondents(seed_dictionary_list):
    """ Displays all of the people who responded """
    sorted_seed_dictionary_list = seed_process.seed_process_sort_dictionary_list(
        seed_dictionary_list, seed_lookup.PERSON_NAME)
    print("Displaying the", len(sorted_seed_dictionary_list), "respondents")
    print()
    for current_seed_dictionary in sorted_seed_dictionary_list:
        current_name = current_seed_dictionary[seed_lookup.PERSON_NAME]
        current_company = current_seed_dictionary[seed_lookup.COMPANY_NAME]
        current_title = current_seed_dictionary[seed_lookup.TITLE_NAME]
        print(seed.INDENT,
              current_name.strip(), "is a",
              current_title.strip(), "at", current_company.strip())


def seed_display_respondent_markdown(seed_dictionary):
    """ Displays the details about a respondent """

    print(MARKDOWN_HEADER_MARKER)
    seed_display_markdown_header_entry(seed_lookup.PERSON_NAME,
                                       seed_dictionary)
    seed_display_markdown_header_entry(seed_lookup.COMPANY_NAME,
                                       seed_dictionary)
    print(MARKDOWN_HEADER_MARKER)


def seed_display_markdown_header_entry(seed_entry, seed_dictionary):
    """ Display a specific header entry """
    print(
        seed_entry,
        ": ",
        MARKDOWN_QUOTE,
        seed_dictionary[seed_entry].strip(),
        MARKDOWN_QUOTE,
        sep='')


def seed_display_sample(seed_dictionary_list):
    """ Displays all of the topics in a textual format """
    first_entry_index = 0
    last_entry_index = len(seed_dictionary_list)
    randomly_chosen_index = random.randint(first_entry_index, last_entry_index)
    first_seed_dictionary = seed_dictionary_list[randomly_chosen_index]
    print(json.dumps(first_seed_dictionary, indent=3))

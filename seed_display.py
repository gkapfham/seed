""" seed_display.py displays details about the SEED data """

import json
import random

import seed
import seed_lookup
import seed_process


def seed_display_respondents(seed_dictionary_list):
    """ Displays all of the people who responded """
    sorted_seed_dictionary_list = seed_process.seed_process_sort_dictionary_list(
        seed_dictionary_list, seed_lookup.PERSON_NAME)
    for current_seed_dictionary in sorted_seed_dictionary_list:
        current_name = current_seed_dictionary[seed_lookup.PERSON_NAME]
        print(seed.INDENT, current_name)


def seed_display_sample(seed_dictionary_list):
    """ Displays all of the topics in a textual format """
    first_entry_index = 0
    last_entry_index = len(seed_dictionary_list)
    randomly_chosen_index = random.randint(first_entry_index, last_entry_index)
    first_seed_dictionary = seed_dictionary_list[randomly_chosen_index]
    print(json.dumps(first_seed_dictionary, indent=3))

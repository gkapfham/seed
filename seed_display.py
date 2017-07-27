""" seed_display.py displays details about the SEED data """


import json

import seed_lookup
import seed

def seed_display_respondents(seed_dictionary_list):
    """ Displays all of the people who responded """
    for current_seed_dictionary in seed_dictionary_list:
        current_name = current_seed_dictionary[seed_lookup.PERSON_NAME]
        print(seed.INDENT, current_name)


def seed_display_sample(seed_dictionary_list):
    """ Displays all of the topics """
    first_seed_dictionary = seed_dictionary_list[0]
    print(json.dumps(first_seed_dictionary, indent=3))

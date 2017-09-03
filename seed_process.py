""" seed_process.py processes a JSON file from SimpleForm """

from itertools import filterfalse
from operator import itemgetter

DATA_PAYLOAD = "data"
UPDATES = "Updates from"
SUBJECT = "_subject"
EMAIL = "reply_to"


def contains_update_subject(internal_dictionary):
    """ Return True if the subject contains 'Updates from ...'
        This means that it is part of a different form """
    if UPDATES in internal_dictionary[SUBJECT]:
        return True
    else:
        return False


def seed_process_remove_emails(seed_internal_dictionary_list):
    """ Process the JSON file by removing the provided email address """
    for internal_dictionary in seed_internal_dictionary_list:
        del internal_dictionary[EMAIL]


def seed_process_remove_email_subscriptions(seed_internal_dictionary_list):
    """ Process the JSON file by removing the mailing list subscription entries """
    seed_internal_dictionary_list[:] = filterfalse(
        contains_update_subject, seed_internal_dictionary_list)


def seed_process_create_internal_dictionary(seed_json):
    """ Process the JSON file and then create the internal dictionary """
    maximum_form_submission = len(seed_json)
    internal_dictionary_list = []
    for current_form_submission_index in range(0, maximum_form_submission):
        current_form_submission = seed_json[current_form_submission_index]
        for key_specific_person, value_specific_person in current_form_submission.items(
        ):
            if key_specific_person == DATA_PAYLOAD:
                submission_details_dict = value_specific_person
                internal_dictionary_list.append(submission_details_dict)
    return internal_dictionary_list


def seed_process_sort_dictionary_list(dictionary_list, chosen_key):
    """ Sorts the list of dictionaries according to a key """
    sorted_dictionary_list = sorted(dictionary_list, key=itemgetter(chosen_key))
    return sorted_dictionary_list

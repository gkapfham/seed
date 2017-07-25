""" seed_process.py processes a JSON file from SimpleForm """


from collections import OrderedDict


DATA_PAYLOAD = "data"


def seed_process_remove_emails(seed_internal_dictionary):
    """ Process the JSON file by removing the provided email address """
    processed_seed_list = seed_internal_dictionary
    return processed_seed_list


def seed_process_remove_email_subscriptions(seed_internal_dictionary):
    """ Process the JSON file by removing the provided email address """
    processed_seed_list = seed_internal_dictionary
    return processed_seed_list


def seed_process_create_internal_dictionary(seed_json):
    """ Process the JSON file creating the internal dictionary"""
    maximum_form_submission = len(seed_json)
    processed_seed_list = []
    for current_form_submission_index in range(1, maximum_form_submission):
        current_form_submission = seed_json[current_form_submission_index]
        for key_specific_person, value_specific_person in current_form_submission.items():
            if key_specific_person == DATA_PAYLOAD:
                submission_details_dict = value_specific_person
                # print("person", submission_details_dict)
                processed_seed_list.append(submission_details_dict)
    return processed_seed_list

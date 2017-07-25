""" seed_process.py processes a JSON file from SimpleForm """


DATA_PAYLOAD = "data"
UPDATES = "Updates from"
SUBJECT = "_subject"
EMAIL = "reply_to"


def seed_process_remove_emails(seed_internal_dictionary_list):
    """ Process the JSON file by removing the provided email address """
    print(len(seed_internal_dictionary_list))
    for internal_dictionary in seed_internal_dictionary_list:
        del internal_dictionary[EMAIL]
    print(len(seed_internal_dictionary_list))


def seed_process_remove_email_subscriptions(seed_internal_dictionary_list):
    """ Process the JSON file by removing the subscription entries """
    processed_seed_list = seed_internal_dictionary_list
    for internal_dictionary in seed_internal_dictionary_list:
        print('-----')
        print(internal_dictionary)
        print('-----')
        print()
        if UPDATES in internal_dictionary[SUBJECT]:
            print(UPDATES)
            print(internal_dictionary)
            seed_internal_dictionary_index = seed_internal_dictionary_list.index(internal_dictionary)
            del processed_seed_list[seed_internal_dictionary_index]


def seed_process_create_internal_dictionary(seed_json):
    """ Process the JSON file and then create the internal dictionary """
    maximum_form_submission = len(seed_json)
    internal_dictionary_list = []
    for current_form_submission_index in range(0, maximum_form_submission):
        current_form_submission = seed_json[current_form_submission_index]
        for key_specific_person, value_specific_person in current_form_submission.items():
            if key_specific_person == DATA_PAYLOAD:
                submission_details_dict = value_specific_person
                internal_dictionary_list.append(submission_details_dict)
    return internal_dictionary_list

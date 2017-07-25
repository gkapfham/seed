""" seed_process.py processes a JSON file from SimpleForm """


from collections import OrderedDict


def seed_process_remove_emails(seed_json):
    """ Process the JSON file by removing the provided email address """
    maximum_form_submission = len(seed_json)
    processed_seed_list = []
    for current_form_submission_index in range(1, maximum_form_submission):
        current_form_submission = seed_json[current_form_submission_index]
        for key_specific_person, value_specific_person in current_form_submission.items():
            if key_specific_person == 'data':
                submission_details_dict = value_specific_person
                ordered_submission_details = OrderedDict(sorted(submission_details_dict.items(), key=lambda t: t[0]))
                processed_seed_json_dict = {}
                for key_submission_details, value_specific_details in ordered_submission_details.items():
                    processed_seed_json_dict[key_submission_details] = value_specific_details
                    processed_seed_list.append(processed_seed_json_dict)
    return processed_seed_list

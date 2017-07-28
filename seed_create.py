""" Create different entities used during the analysis of SEED responses """


import seed_lookup


DIVIDER = ","
QUOTATION_MARK = "\""


def create_mailing_list(seed_dictionary_list):
    """ Create a mailing list from the provided dictionary """
    email_address_list = []
    for current_seed_dictionary in seed_dictionary_list:
        current_name = current_seed_dictionary[seed_lookup.PERSON_NAME]
        current_email = current_seed_dictionary[seed_lookup.EMAIL]
        current_list_entry = current_email + DIVIDER + QUOTATION_MARK + current_name + QUOTATION_MARK
        email_address_list.append(current_list_entry)
    return email_address_list


def create_fact_answer_list(seed_dictionary_list):
    """ Create the list of all of the answers to the FACT question """
    answers_list = []
    for current_seed_dictionary in seed_dictionary_list:
        current_fact = current_seed_dictionary[seed_lookup.QUESITON_FACT]
        answers_list.append(current_fact)
    return answers_list


def create_advice_answer_list(seed_dictionary_list):
    """ Create the list of all of the answers to the ADVICE question """
    answers_list = []
    for current_seed_dictionary in seed_dictionary_list:
        current_fact = current_seed_dictionary[seed_lookup.QUESTION_ADVICE]
        answers_list.append(current_fact)
    return answers_list


def create_challenge_answer_list(seed_dictionary_list):
    """ Create the list of all of the answers to the CHALLENGE question """
    answers_list = []
    for current_seed_dictionary in seed_dictionary_list:
        current_fact = current_seed_dictionary[seed_lookup.QUESTION_CHALLENGE]
        answers_list.append(current_fact)
    return answers_list

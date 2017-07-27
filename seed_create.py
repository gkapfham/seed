""" Create different entities used during the analysis of SEED responses """


import seed_lookup


DIVIDER = ","
QUOTATION_MARK = "\""
MAILING_LIST_FILENAME = "recipients.csv"


def create_mailing_list(seed_dictionary_list):
    """ Create a mailing list from the provided dictionary """
    email_address_list = []
    for current_seed_dictionary in seed_dictionary_list:
        current_name = current_seed_dictionary[seed_lookup.PERSON_NAME]
        current_email = current_seed_dictionary[seed_lookup.EMAIL]
        current_list_entry = current_email + DIVIDER + QUOTATION_MARK + current_name + QUOTATION_MARK
        email_address_list.append(current_list_entry)

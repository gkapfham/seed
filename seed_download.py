""" seed_download.py downloads a JSON file from SimpleForm and saves files """

import json
import requests

import seed

JSON_FILENAME = "seed.json"
MAILING_LIST_FILENAME = "recipients.csv"


def seed_download(seed_simpleform_token):
    """ Download the JSON file from SimpleForm using the provided token """
    simpleform_response = requests.get(
        'http://getsimpleform.com/messages.json?api_token=' +
        seed_simpleform_token)
    response_json = None

    # the query worked and the JSON file can be returned
    if simpleform_response.ok:
        # extract the JSON object
        response_json = simpleform_response.json()
    return response_json


def seed_save_json(list_of_dictionaries):
    """ Save the list of dictionaries to the specified file """
    with open(JSON_FILENAME, 'w') as file_output:
        json.dump(list_of_dictionaries, file_output)


def seed_save_mailing_list(list_of_emails):
    """ Save the list of dictionaries to the specified file """
    with open(MAILING_LIST_FILENAME, 'w') as file_output:
        for email in list_of_emails:
            file_output.write("{}\n".format(email))


def seed_load():
    """ Reads the list of dictionaries from the specified file """
    with open(seed.get_seed_home() + JSON_FILENAME, 'r') as file_output:
        seed_json = json.load(file_output)
    return seed_json

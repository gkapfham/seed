""" seed_download.py downloads a JSON file from SimpleForm """


import json
import requests


JSON_FILENAME = "seed.json"


def seed_download(seed_simpleform_token):
    """ Download the JSON file from SimpleForm using the provided token """
    simpleform_response = requests.get('http://getsimpleform.com/messages.json?api_token=' + seed_simpleform_token)
    response_json = None

    # the query worked and the JSON file can be returned
    if simpleform_response.ok:
        # extract the JSON object
        response_json = simpleform_response.json()
    return response_json


def seed_save(list_of_dictionaries):
    """ Save the list of dictionaries to the specified file """
    with open(JSON_FILENAME, 'w') as file_output:
        json.dump(list_of_dictionaries, file_output)


def seed_load():
    """ Save the list of dictionaries to the specified file """
    with open(JSON_FILENAME, 'r') as file_output:
        seed_json = json.load(file_output)
    return seed_json

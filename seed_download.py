""" seed_download.py downloads a JSON file from SimpleForm """


import requests


def seed_download(seed_simpleform_token):
    """ download the JSON file from SimpleForm using the provided token """
    simpleform_response = requests.get('http://getsimpleform.com/messages.json?api_token=' + seed_simpleform_token)
    response_json = None

    # the query worked and the JSON file can be returned
    if simpleform_response.ok:
        # extract the JSON object
        response_json = simpleform_response.json()
    # print("Right before seed_download return")
    return response_json

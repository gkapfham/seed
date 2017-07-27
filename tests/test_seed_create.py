"""Test suite for the seed_create.py module"""


import os
import pytest

import seed
import seed_create
import seed_download
import seed_process


@pytest.fixture
def verifiable_seed_args():
    """Return arguments that are verifiable with the token specified through the OS"""
    # test case can only pass if the environment variable is set
    simple_form_token = os.environ.get('SIMPLEFORM_TOKEN')
    return ['--token', simple_form_token, '--create-list']


def test_mailing_list_entries_for_each_name(verifiable_seed_args):
    """Make sure that the removal of the email address makes a same-sized list"""
    seed_arguments, seed_parser = seed.parse_seed_arguments(verifiable_seed_args)
    downloaded_json = seed_download.seed_download(seed_arguments.token)
    assert downloaded_json is not None
    seed_internal_dictionary_list = seed_process.seed_process_create_internal_dictionary(downloaded_json)
    assert seed_internal_dictionary_list is not None
    length_internal_dictionary_list = len(seed_internal_dictionary_list)
    assert length_internal_dictionary_list > 0
    mailing_list = seed_create.create_mailing_list(seed_internal_dictionary_list)
    assert length_internal_dictionary_list == len(mailing_list)

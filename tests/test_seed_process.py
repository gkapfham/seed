"""Test suite for the seed_process.py module"""

import os
import pytest

import seed
import seed_download
import seed_process


SEED_SIMPLEFORM_TOKEN = "SEED_SIMPLEFORM_TOKEN"

download = pytest.mark.skipif(
    not pytest.config.getoption("--rundownload"),
    reason="needs the --rundownload option to run")


@pytest.fixture
def verifiable_seed_args():
    """Return arguments that are verifiable with the token specified through the OS"""
    # test case can only pass if the environment variable is set
    simple_form_token = os.environ.get(SEED_SIMPLEFORM_TOKEN)
    return ['--token', simple_form_token, '--download-json']


@download
def test_dictionary_is_not_none(verifiable_seed_args):
    """Run seed with a specified token and it is verified"""
    seed_arguments, seed_parser = seed.parse_seed_arguments(verifiable_seed_args)
    downloaded_json = seed_download.seed_download(seed_arguments.token)
    assert downloaded_json is not None
    seed_internal_dictionary = seed_process.seed_process_create_internal_dictionary(downloaded_json)
    assert seed_internal_dictionary is not None


@download
def test_dictionary_list_after_email_list_removal_is_smaller(verifiable_seed_args):
    """Make sure that the removal of the email subscriptions makes a smaller list"""
    seed_arguments, seed_parser = seed.parse_seed_arguments(verifiable_seed_args)
    downloaded_json = seed_download.seed_download(seed_arguments.token)
    assert downloaded_json is not None
    seed_internal_dictionary_list = seed_process.seed_process_create_internal_dictionary(downloaded_json)
    assert seed_internal_dictionary_list is not None
    length_internal_dictionary_list = len(seed_internal_dictionary_list)
    assert length_internal_dictionary_list > 0
    seed_process.seed_process_remove_email_subscriptions(seed_internal_dictionary_list)
    assert len(seed_internal_dictionary_list) < length_internal_dictionary_list


@download
def test_dictionary_list_after_email_address_removal_is_same(verifiable_seed_args):
    """Make sure that the removal of the email address makes a same-sized list"""
    seed_arguments, seed_parser = seed.parse_seed_arguments(verifiable_seed_args)
    downloaded_json = seed_download.seed_download(seed_arguments.token)
    assert downloaded_json is not None
    seed_internal_dictionary_list = seed_process.seed_process_create_internal_dictionary(downloaded_json)
    assert seed_internal_dictionary_list is not None
    length_internal_dictionary_list = len(seed_internal_dictionary_list)
    assert length_internal_dictionary_list > 0
    seed_process.seed_process_remove_emails(seed_internal_dictionary_list)
    assert len(seed_internal_dictionary_list) == length_internal_dictionary_list

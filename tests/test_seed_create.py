"""Test suite for the seed_create.py module"""

import os
import pytest

import seed
import seed_create
import seed_download
import seed_process


download = pytest.mark.skipif(
    not pytest.config.getoption("--rundownload"),
    reason="needs the --rundownload option to run")


@pytest.fixture
def verifiable_seed_args():
    """Return arguments that are verifiable with the token specified through the OS"""
    # test case can only pass if the environment variable is set
    simple_form_token = seed.get_seed_simpleform_token()
    return ['--token', simple_form_token, '--create-list']


@download
def test_mailing_list_entries_for_each_name(verifiable_seed_args):
    """Make sure that the removal of the email address makes a same-sized list"""
    seed_arguments, seed_parser = seed.parse_seed_arguments(
        verifiable_seed_args)
    downloaded_json = seed_download.seed_download(seed_arguments.token)
    assert downloaded_json is not None
    seed_internal_dictionary_list = seed_process.seed_process_create_internal_dictionary(
        downloaded_json)
    assert seed_internal_dictionary_list is not None
    length_internal_dictionary_list = len(seed_internal_dictionary_list)
    assert length_internal_dictionary_list > 0
    mailing_list = seed_create.create_mailing_list(
        seed_internal_dictionary_list)
    assert length_internal_dictionary_list == len(mailing_list)


@download
def test_fact_responses_for_each_name(verifiable_seed_args):
    """Make sure that the removal of the email address makes a same-sized list"""
    seed_arguments, seed_parser = seed.parse_seed_arguments(
        verifiable_seed_args)
    downloaded_json = seed_download.seed_download(seed_arguments.token)
    assert downloaded_json is not None
    seed_internal_dictionary_list = seed_process.seed_process_create_internal_dictionary(
        downloaded_json)
    assert seed_internal_dictionary_list is not None
    length_internal_dictionary_list = len(seed_internal_dictionary_list)
    assert length_internal_dictionary_list > 0
    seed_process.seed_process_remove_email_subscriptions(
        seed_internal_dictionary_list)
    assert len(seed_internal_dictionary_list) < length_internal_dictionary_list
    fact_answers_list = seed_create.create_fact_answer_list(
        seed_internal_dictionary_list)
    assert len(seed_internal_dictionary_list) == len(fact_answers_list)


@download
def test_advice_responses_for_each_name(verifiable_seed_args):
    """Make sure that the removal of the email address makes a same-sized list"""
    seed_arguments, seed_parser = seed.parse_seed_arguments(
        verifiable_seed_args)
    downloaded_json = seed_download.seed_download(seed_arguments.token)
    assert downloaded_json is not None
    seed_internal_dictionary_list = seed_process.seed_process_create_internal_dictionary(
        downloaded_json)
    assert seed_internal_dictionary_list is not None
    length_internal_dictionary_list = len(seed_internal_dictionary_list)
    assert length_internal_dictionary_list > 0
    seed_process.seed_process_remove_email_subscriptions(
        seed_internal_dictionary_list)
    assert len(seed_internal_dictionary_list) < length_internal_dictionary_list
    advice_answers_list = seed_create.create_advice_answer_list(
        seed_internal_dictionary_list)
    assert len(seed_internal_dictionary_list) == len(advice_answers_list)


@download
def test_challenge_responses_for_each_name(verifiable_seed_args):
    """Make sure that the removal of the email address makes a same-sized list"""
    seed_arguments, seed_parser = seed.parse_seed_arguments(
        verifiable_seed_args)
    downloaded_json = seed_download.seed_download(seed_arguments.token)
    assert downloaded_json is not None
    seed_internal_dictionary_list = seed_process.seed_process_create_internal_dictionary(
        downloaded_json)
    assert seed_internal_dictionary_list is not None
    length_internal_dictionary_list = len(seed_internal_dictionary_list)
    assert length_internal_dictionary_list > 0
    seed_process.seed_process_remove_email_subscriptions(
        seed_internal_dictionary_list)
    assert len(seed_internal_dictionary_list) < length_internal_dictionary_list
    challenge_answers_list = seed_create.create_challenge_answer_list(
        seed_internal_dictionary_list)
    assert len(seed_internal_dictionary_list) == len(challenge_answers_list)

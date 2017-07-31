"""Test suite for the seed_gensim.py module"""

import pytest

import seed
import seed_create
import seed_download
import seed_gensim

VERIFIED = True
NOT_VERIFIED = False


@pytest.fixture
def verifiable_seed_args_facts():
    """Return arguments that are verifiable because only analyze_facts"""
    return ['--analyze-facts', "--num-passes", "1", "--num-topics", "2"]


def test_seed_gensim_creates_dictionary():
    """ Determine if seed_gensim can create a not-None dictionary """
    seed_dictionary_list = seed_download.seed_load()
    fact_response_list = seed_create.create_fact_answer_list(
        seed_dictionary_list)
    topic_model_dictionary, texts_to_analyze = seed_gensim.create_topic_model_dictionary(
        fact_response_list)
    assert topic_model_dictionary is not None
    assert texts_to_analyze is not None
    assert len(topic_model_dictionary.keys()) != 0


def test_seed_gensim_creates_model(verifiable_seed_args_facts):
    """ Determine if seed_gensim can create a not-None model with LDA """
    seed_arguments, seed_parser = seed.parse_seed_arguments(
        verifiable_seed_args_facts)
    seed_args_verified = seed.verify_seed_arguments(seed_arguments)
    assert seed_args_verified == VERIFIED
    seed_dictionary_list = seed_download.seed_load()
    fact_response_list = seed_create.create_fact_answer_list(
        seed_dictionary_list)
    seed.perform_gensim_analysis(seed_arguments, fact_response_list)

"""Test suite for the seed_gensim.py module"""

import pytest

import seed
import seed_create
import seed_download
import seed_gensim


def test_seed_gensim_creates_dictionary():
    """ Determine if seed_gensim can create a not-None dictionary """
    seed_dictionary_list = seed_download.seed_load()
    fact_response_list = seed_create.create_fact_answer_list(seed_dictionary_list)
    topic_model_dictionary, texts_to_analyze = seed_gensim.create_topic_model_dictionary(fact_response_list)
    assert topic_model_dictionary is not None
    assert len(topic_model_dictionary.keys()) != 0

"""Test suite for the seed.py module"""

import pytest
import seed

VERIFIED = True
NOT_VERIFIED = False


@pytest.fixture
def no_seed_args():
    """Return no command-line arguments"""
    return []


@pytest.fixture
def verifiable_seed_args():
    """Return arguments that are verifiable"""
    return ['--token', 'SimpleFormToken']


@pytest.fixture
def not_verifiable_seed_args_download_json():
    """Return arguments that are not verifiable because download_json with no token"""
    return ['--download-json']


@pytest.fixture
def not_verifiable_seed_args_create_list():
    """Return arguments that are not verifiable because create_list with no token"""
    return ['--create-list']


@pytest.fixture
def verifiable_seed_args_show_respondents():
    """Return arguments that are verifiable because only show_respondents"""
    return ['--show-respondents']


@pytest.fixture
def verifiable_seed_args_show_sample():
    """Return arguments that are verifiable because only show_respondents"""
    return ['--show-sample']


@pytest.fixture
def verifiable_seed_args_facts():
    """Return arguments that are verifiable because only analyze_facts"""
    return ['--analyze-facts']


@pytest.fixture
def nonverifiable_seed_args_no_lda_with_visualize():
    """Return arguments that are not verifiable because no LDA"""
    return ['--visualize']


@pytest.fixture
def nonverifiable_seed_args_no_lda_with_num_topics():
    """Return arguments that are not verifiable because no LDA"""
    return ['--num-topics', '5']


@pytest.fixture
def nonverifiable_seed_args_incorrect_alpha():
    """Return arguments that are not verifiable because incorrect alpha"""
    return ['--alpha', 'auto111']


@pytest.fixture
def verifiable_seed_args_correct_alpha():
    """Return arguments that are verifiable because correct alpha"""
    return ['--alpha', 'auto']


def test_seed_empty_test():
    """Run an empty test to ensure test harness working"""
    return "empty"


def test_seed_verified(verifiable_seed_args):
    """Run seed with a specified token and it is verified"""
    seed_arguments, seed_parser = seed.parse_seed_arguments(
        verifiable_seed_args)
    seed_args_verified = seed.verify_seed_arguments(seed_arguments)
    assert seed_args_verified == VERIFIED


def test_seed_verified_show_respondents(verifiable_seed_args_show_respondents):
    """Run seed with a specified token and it is verified"""
    seed_arguments, seed_parser = seed.parse_seed_arguments(
        verifiable_seed_args_show_respondents)
    seed_args_verified = seed.verify_seed_arguments(seed_arguments)
    assert seed_args_verified == VERIFIED


def test_seed_verified_show_sample(verifiable_seed_args_show_sample):
    """Run seed with a specified token and it is verified"""
    seed_arguments, seed_parser = seed.parse_seed_arguments(
        verifiable_seed_args_show_sample)
    seed_args_verified = seed.verify_seed_arguments(seed_arguments)
    assert seed_args_verified == VERIFIED


def test_seed_verified_analyze_facts(verifiable_seed_args_facts):
    """Run seed with a specified token and it is verified"""
    seed_arguments, seed_parser = seed.parse_seed_arguments(
        verifiable_seed_args_facts)
    seed_args_verified = seed.verify_seed_arguments(seed_arguments)
    assert seed_args_verified == VERIFIED


def test_seed_not_verified_download(not_verifiable_seed_args_download_json):
    """Run seed with a specified token and it is verified"""
    seed_arguments, seed_parser = seed.parse_seed_arguments(
        not_verifiable_seed_args_download_json)
    were_seed_args_verified = seed.verify_seed_arguments(seed_arguments)
    assert were_seed_args_verified == NOT_VERIFIED


def test_seed_not_verified_list(not_verifiable_seed_args_create_list):
    """Run seed with a specified token and it is verified"""
    seed_arguments, seed_parser = seed.parse_seed_arguments(
        not_verifiable_seed_args_create_list)
    were_seed_args_verified = seed.verify_seed_arguments(seed_arguments)
    assert were_seed_args_verified == NOT_VERIFIED


def test_seed_home_is_set():
    """ Ensure that the SEED_HOME environment variable is set"""
    seed_home = seed.get_seed_home()
    assert seed_home is not None


def test_seed_home_verification_working_verified():
    """Run seed and checks that SEED_HOME verification is working """
    seed_home_verified = seed.verify_seed_home("/home/gkapfham/")
    assert seed_home_verified == VERIFIED


def test_seed_home_verification_working_notverified():
    """Run seed and checks that SEED_HOME verification is working """
    seed_home_verified = seed.verify_seed_home("/home/gkapfham")
    assert seed_home_verified == NOT_VERIFIED


def test_seed_simpleform_is_set():
    """ Ensure that the SEED_SIMPLEFORM_TOKEN environment variable is set"""
    seed_simpleform = seed.get_seed_simpleform_token()
    assert seed_simpleform is not None


def test_seed_not_verified_no_lda_visualize(nonverifiable_seed_args_no_lda_with_visualize):
    """Run seed with a specified token and it is not verified"""
    seed_arguments, seed_parser = seed.parse_seed_arguments(
        nonverifiable_seed_args_no_lda_with_visualize)
    seed_args_verified = seed.verify_seed_arguments(seed_arguments)
    assert seed_args_verified == NOT_VERIFIED


def test_seed_not_verified_no_lda_numtopics(nonverifiable_seed_args_no_lda_with_num_topics):
    """Run seed with a specified token and it is not verified"""
    seed_arguments, seed_parser = seed.parse_seed_arguments(
        nonverifiable_seed_args_no_lda_with_num_topics)
    seed_args_verified = seed.verify_seed_arguments(seed_arguments)
    assert seed_args_verified == NOT_VERIFIED


def test_seed_not_verified_incorrect_alpha(nonverifiable_seed_args_incorrect_alpha):
    """Run seed with a specified token and it is not verified"""
    try:
        seed_arguments, seed_parser = seed.parse_seed_arguments(
            nonverifiable_seed_args_incorrect_alpha)
        seed.verify_seed_arguments(seed_arguments)
    except SystemExit:
        pass
    assert True

def test_seed_verified_correct_alpha(verifiable_seed_args_correct_alpha):
    """Run seed with a specified token and it is not verified"""
    seed_arguments, seed_parser = seed.parse_seed_arguments(
        verifiable_seed_args_correct_alpha)
    seed_args_verified = seed.verify_seed_arguments(seed_arguments)
    assert seed_args_verified == NOT_VERIFIED


def test_default_argument_values_correct(no_seed_args):
    """The default command-line arguments are correct"""
    seed_arguments, seed_parser = seed.parse_seed_arguments(
        no_seed_args)
    seed_args_verified = seed.verify_seed_arguments(seed_arguments)
    assert seed_args_verified == VERIFIED
    assert seed_arguments.num_topics == 3
    assert seed_arguments.num_passes == 10
    assert seed_arguments.alpha == seed.DEFAULT_ALPHA
    assert seed_arguments.eta == seed.DEFAULT_ETA

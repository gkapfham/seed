"""Test suite for the seed module"""


import pytest
import seed


VERIFIED = True
NOT_VERIFIED = True


@pytest.fixture
def verifiable_seed_args():
    """Return arguments that are verifiable"""
    return ['--token', 'SimpleFormToken']


@pytest.fixture
def not_verifiable_seed_args_download():
    """Return arguments that are not verifiable because download_json with no token"""
    return ['--download-json']


@pytest.fixture
def not_verifiable_seed_args_mailing_list():
    """Return a default utterson arguments, resulting in list of size 10"""
    return ['--create-list']


def test_seed_empty_test():
    """Run an empty test to ensure test harness working"""
    return "empty"


def test_seed_verified(verifiable_seed_args):
    """Run seed with a specified token and it is verified"""
    seed_args = seed.parse_seed_arguments(verifiable_seed_args)
    seed_args_verified = seed.verify_seed_arguments(seed_args)
    assert seed_args_verified == VERIFIED


def test_seed_not_verified_download(not_verifiable_seed_args_download):
    """Run seed with a specified token and it is verified"""
    seed_args = seed.parse_seed_arguments(not_verifiable_seed_args_download)
    seed_args_verified = seed.verify_seed_arguments(seed_args)
    assert seed_args_verified == NOT_VERIFIED

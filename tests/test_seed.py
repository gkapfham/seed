"""Test suite for the seed module"""


import pytest
import seed


VERIFIED = True
NOT_VERIFIED = False


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
    """Return a default utterson arguments, resulting in list of size 10"""
    return ['--create-list']


def test_seed_empty_test():
    """Run an empty test to ensure test harness working"""
    return "empty"


def test_seed_verified(verifiable_seed_args):
    """Run seed with a specified token and it is verified"""
    seed_arguments, seed_parser = seed.parse_seed_arguments(verifiable_seed_args)
    seed_args_verified = seed.verify_seed_arguments(seed_arguments)
    assert seed_args_verified == VERIFIED


def test_seed_not_verified_download(not_verifiable_seed_args_download_json):
    """Run seed with a specified token and it is verified"""
    seed_arguments, seed_parser = seed.parse_seed_arguments(not_verifiable_seed_args_download_json)
    were_seed_args_verified = seed.verify_seed_arguments(seed_arguments)
    assert were_seed_args_verified == NOT_VERIFIED


def test_seed_not_verified_list(not_verifiable_seed_args_create_list):
    """Run seed with a specified token and it is verified"""
    seed_arguments, seed_parser = seed.parse_seed_arguments(not_verifiable_seed_args_create_list)
    were_seed_args_verified = seed.verify_seed_arguments(seed_arguments)
    assert were_seed_args_verified == NOT_VERIFIED

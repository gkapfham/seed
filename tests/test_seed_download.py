"""Test suite for the seed_download.py module"""

import os
import pytest

import seed
import seed_download


VERIFIED = True

DOWNLOADED = True
NOT_DOWNLOADED = False

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
def test_seed_verified_downloaded_something(verifiable_seed_args):
    """Run seed with a specified token and it is verified"""
    seed_arguments, seed_parser = seed.parse_seed_arguments(verifiable_seed_args)
    seed_args_verified = seed.verify_seed_arguments(seed_arguments)
    assert seed_args_verified == VERIFIED
    downloaded_json = seed_download.seed_download(seed_arguments.token)
    assert downloaded_json is not None

"""Test suite for the seed module"""


import pytest
import seed


@pytest.fixture
def verifiable_seed_args():
    """Return a default utterson arguments, resulting in list of size 10"""
    return ['--token', 'SimpleFormToken']


def test_utterson_empty_test():
    """Run an empty test to ensure test harness working"""
    return "empty"


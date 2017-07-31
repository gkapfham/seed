import os
# import pytest
import sys

# set the system path to contain the previous directory
mypath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, mypath + '/../')


# define command-line argument for including slow tests
def pytest_addoption(parser):
    parser.addoption(
        "--runslow", action="store_true", help="Run the slow test cases")

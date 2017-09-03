# SEED: Educational Discussions with Software Engineers

SEED is a Python 3 program that analyzes and visualizes a data set for the [SEED
Project](http://www.cs.allegheny.edu/sites/gkapfham/seed/) created by [Gregory
M. Kapfhammer](http://www.cs.allegheny.edu/sites/gkapfham/). With required
tokens, it can be used to download the responses of the interviewees who
participated in the SEED project. Additionally, you can use SEED to see the
interviewees' responses and to perform natural language processing to extract
the key topic models. This program is currently under heavy development; more
extensive documentation is forthcoming.

## Installation

As a Python 3 program, SEED relies on
[pip](https://pip.pypa.io/en/stable/installing/) for installation. To ensure
that all of the dependencies are installed correctly, please type the following
commands before running SEED.

- `pip install --upgrade pip`
- `pip install -r requirements.txt`

Note that you may have Python 3 setup in different ways on your computer. For
instance, you may prefer to install SEED's dependencies in a site-wide
location and then you would have to type, for instance, `sudo pip install -r
requirements.txt`. Alternatively, you may choose to install the dependencies by
typing `pip install --user -r requirements.txt`.

## Testing SEED

SEED uses [Pytest](https://docs.pytest.org/en/latest/) for testing. To run
SEED's test suite, please type `pytest tests` in the root of the project's
repository. If any of the test cases fail in your development environment,
please please raise an issue in SEED's issue tracker.

Please note that some of SEED's test cases require you to have a private access
token stored in the `SEED_SIMPLEFORM_TOKEN` environment variable. By necessity,
this token is kept private and only known to the developer of this program. As
such, these test cases will be skipped when you run the aforementioned command.

Moreover, SEED contains some test cases that normally take a longer time to run
because of the fact that they invoke functions that use natural language
processing libraries. If you would still like to run those tests, then you can
type `pytest tests --runslow`.

## Problems or Praise

If you have any problems with installing or using SEED, then please create an
issue associated with this Git repository using the "Issues" link at the top of
this site. I will do everything that I can to resolve your issue and ensure that
the entire tool works well in your own development environment.

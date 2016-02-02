# Speculative Python API for REST API to scholarometer

***IMPORTANT:*** This is just a POC - you should be able to make sure that the
requirements are available and just go.

This is a simple wrapper around a small fraction the Scholarometer API
documented at http://scholarometer.indiana.edu/data.html.
The one exception is `Authors.get_articles_by_id` - that is a call to the ReST endpoint
used by the scholarometer web application itself.

## Development and Details

After cloning, set up the dev environment with `setup.sh` and then use the
created virtualenv to run tests with `run_tests.py`.

We use defusedxml for secure XML parsing and requests for HTTP. As mentioned
above, the script `setup.sh` will install these for you into a virtualenv. See
requirements.txt if you want to manually install them into a virtualenv of
your choosing. Yes, we should have a pypi-compatible setup.py one day.

The file `test.py` contatins all unit tests. Run them via `run_tests.py`. Note
that this means that you should have already run `setup.sh`

The unit tests call the live scholarometer API. Yes, this needs to change to
calling mocks. See the Config class for a good candidate for testing mocking.

## Quick file run-down (in alphabetical order)

* README.md - this file
* requirements.txt - requirements list for this project
* run_tests.sh - run the unit tests in test.py using the virtualenv created by setup.py
* scholarometer.py - the actual module
* setup.sh - create a virtualenv for development
* test.py - unit tests (execute with run_tests.sh)

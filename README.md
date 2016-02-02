# Speculative Python API for REST API to scholarometer

***IMPORTANT:*** This is just a POC - you should be able to make sure that the
requirements are available and just go.

This is a simple wrapper around a small fraction the Scholarometer API
(documented at http://scholarometer.indiana.edu/data.html). It uses defusedxml
for secure XML parsing, requests for HTTP, and supplies unit tests (that
call the live API - yes, that needs to change).

## Development

After cloning, set up the dev environment with `setup.sh` and then use the
created virtualenv to run tests with `run_tests.py`.

## Quick file run-down (in alphabetical order)

* README.md - this file
* requirements.txt - requirements list for this project
* run_tests.sh - run the unit tests in test.py using the virtualenv created by setup.py
* scholarometer.py - the actual module
* setup.sh - create a virtualenv for development
* test.py - unit tests (execute with run_tests.sh)

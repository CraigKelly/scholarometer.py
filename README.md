# Python API for Scholarometer ReSTful API

***IMPORTANT:*** This is just a POC - you should be able to make sure that the
requirements are available and just go.

This is a simple wrapper around a small fraction the Scholarometer API
documented at http://scholarometer.indiana.edu/data.html. The one exception is
`Authors.get_articles_by_id` - that is a call to the ReST endpoint used by the
scholarometer web application itself.

## Development and Details

This project uses the MIT License. See LICENSE.txt for details.

After cloning, set up the dev environment with `script/bootstrap` and then use
the created virtualenv to run tests with `script/test`. The virtualenv created
by the bootstrap script includes all dependencies, including libraries used for
testing.

We use `defusedxml` for secure XML parsing and `requests` for HTTP. See
requirements.txt for details if you want to use scholarometer.py outside this
directory. *YES*, we know - we should have a pip-compatible setup.py, and we
should register a release on pypi.

The file `test.py` contains all unit tests. Run them via `script/test`. Note
that this means that you should have already run `script/bootstrap`

The unit tests may call the live scholarometer API! We try to limit
this by using the betamax library to store previous request/response cycles.

## Quick contents run-down (in alphabetical order)

* .cassettes directory - storage for betamax "cassettes" used for unit testing. `script/test` will create if necessary
* CHANGELOG - if we ever have a formal release, we'll put release notes here :)
* CONTRIBUTING.md - Guidelines and help for developers/contributors
* LICENSE.txt - the license for this project (MIT)
* README.md - this file
* requirements.txt - requirements list for this project
* scholarometer.py - the actual module
* script directory - contains helper scripts for the project: `bootstrap` and `test`
* test.py - unit tests (execute with run_tests.sh)

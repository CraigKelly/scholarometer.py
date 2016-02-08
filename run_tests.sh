#!/bin/bash

# Insure we're in our own directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $SCRIPT_DIR

# Insure the cassettes directory is there
mkdir -p .cassettes

# Note that we just set logging to DEBUG and go below. If you really
# need to capture networking stuff, you can use strace:
# $ strace -f -e trace=network -s 10000 ./run_tests.sh

# Actually startup our virtualenv and run tests with nose
source $SCRIPT_DIR/venv/bin/activate
nosetests --logging-level=DEBUG test.py $*

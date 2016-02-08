#!/bin/bash

# Insure we're in our own directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $SCRIPT_DIR

# Insure the cassettes directory is there
mkdir -p .cassettes

# Actually startup our virtualenv and run tests with nose
source $SCRIPT_DIR/venv/bin/activate
nosetests --logging-level=DEBUG test.py $*

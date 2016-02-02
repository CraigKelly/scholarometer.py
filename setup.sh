#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $SCRIPT_DIR

if [ -d venv ];
then
    source $SCRIPT_DIR/venv/bin/activate
    echo -e "\033[33mUpdating venv reqs in $SCRIPT_DIR/requirements.txt\033[0m"
    pip install --upgrade -r "$SCRIPT_DIR/requirements.txt"
else
    echo -e "\033[33mSetting up virtualenv in venv\033[0m"
    virtualenv -p python3 venv
    source $SCRIPT_DIR/venv/bin/activate
    echo -e "\033[33mInstalling reqs in $SCRIPT_DIR/requirements.txt\033[0m"
    pip install --upgrade pip wheel setuptools
    pip install --upgrade -r "$SCRIPT_DIR/requirements.txt"
fi

echo -e "\033[32mSetup Complete\033[0m"

#!/bin/sh

export FLASK_APP=./stackoverflow/jobs.py

source $(pipenv --venv)/bin/activate

flask run
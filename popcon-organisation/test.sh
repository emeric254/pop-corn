#!/bin/sh

python -m coverage run --omit "venv/*" -m pytest --junitxml /tmp/results.xml -o cache_dir=/tmp/.pytest_cache -o junit_family=xunit2 .
python -m coverage report --omit "venv/*" -m -i
python -m coverage xml --omit "venv/*" -o /tmp/coverage.xml -i

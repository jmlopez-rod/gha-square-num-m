#!/bin/bash
set -euo pipefail

export DEBUG_HTTP_INCLUDE_BODY=1

SINGLE=true
SINGLE=false

pyPath="src"
baseSrc="src/pkg"
if [ "$SINGLE" = 'false' ]; then
  coverage run --source "$baseSrc" -m pytest -p no:logging
  coverage report -m --fail-under 98
else
  # To run specific tests:
  filter="test_testing"
  source="$baseSrc"
  coverage run --source "$source" -m pytest -p no:logging "$pyPath" -vv -k "$filter"
  coverage report -m
fi

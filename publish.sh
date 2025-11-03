#!/bin/bash

pip install build

python -m build

pip install twine

# twine upload -r testpypi dist/*
#
# twine upload dist/*

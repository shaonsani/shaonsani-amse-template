#!/bin/bash

# Install pytest
pip install pytest

# Run test files from test directory
pwd
pytest -v project/tests/test_data_pipeline.py
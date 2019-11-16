#!/bin/bash
python3 ./src/handlers.py
py.test ./test/test_minimal-200.tavern.yaml -v
py.test ./test/test_minimal-400.tavern.yaml -v
py.test ./test/test_minimal-404.tavern.yaml -v
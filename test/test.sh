#!/bin/bash

py.test ./test_minimal-200.tavern.yaml -v
py.test ./test_minimal-400.tavern.yaml -v
py.test ./test_minimal-404.tavern.yaml -v
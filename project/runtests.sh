#!/usr/bin/env bash

py.test --cov=. --cov-report=html --cov-config=.coveragerc core

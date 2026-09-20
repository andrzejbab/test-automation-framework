#!/usr/bin/env bash

allure generate tests/allure-results -o allure-report --clean
python3 -m http.server 8001 --directory allure-report
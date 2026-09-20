#!/usr/bin/env bash

export DISPLAY=:99
export CHROME_BINARY=/usr/bin/google-chrome

pytest tests/ui -m ui --ui-headless false
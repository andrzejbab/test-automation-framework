#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install -y chromium chromium-driver
wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get install -y ./google-chrome-stable_current_amd64.deb
google-chrome --version
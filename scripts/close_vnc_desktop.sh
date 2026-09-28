#!/usr/bin/env bash

# 1. Kill all processes associated with the desktop session
pkill -f novnc_proxy
pkill -f x11vnc
pkill -f fluxbox
pkill -f "Xvfb :99"

# 2. Clean up any leftover X11 lock files for display :99
rm -f /tmp/.X99-lock /tmp/.X11-unix/X99
#!/usr/bin/env bash

# Start virtual frame buffer in background
Xvfb :99 -screen 0 1920x1080x24 &
#Xvfb :99 -screen 0 1600x800x24 &

# Set display environment variable for this process and child processes
export DISPLAY=:99

# Start Fluxbox window manager
fluxbox >/tmp/fluxbox.log 2>&1 &

# Start VNC server
x11vnc -display :99 -forever -shared -rfbport 5900 -nopw >/tmp/x11vnc.log 2>&1 &

# Start noVNC web proxy
/usr/share/novnc/utils/novnc_proxy --vnc localhost:5900 --listen 6080 >/tmp/novnc.log 2>&1 &
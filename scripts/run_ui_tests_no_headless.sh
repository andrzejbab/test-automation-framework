#!/usr/bin/env bash
set -euo pipefail

export DISPLAY=:99

if [[ ! -S /tmp/.X11-unix/X99 ]]; then
    ./scripts/start_vnc_desktop.sh
    for _ in {1..50}; do
        [[ -S /tmp/.X11-unix/X99 ]] && break
        sleep 0.1
    done
fi

if [[ ! -S /tmp/.X11-unix/X99 ]]; then
    printf 'Could not start Xvfb on display :99. Check that Xvfb is installed and inspect its startup errors.\n' >&2
    exit 1
fi

pytest tests/ui -m ui --ui-headless false
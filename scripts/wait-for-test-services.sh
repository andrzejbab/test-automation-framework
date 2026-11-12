#!/usr/bin/env bash
set -euo pipefail

wait_for() {
    local service="$1"
    local url="$2"

    printf 'Waiting for %s at %s' "$service" "$url"
    for _ in {1..60}; do
        if curl --silent --fail --max-time 3 "$url" >/dev/null; then
            printf ' ready\n'
            return
        fi
        printf '.'
        sleep 2
    done

    printf '\nTimed out waiting for %s\n' "$service" >&2
    exit 1
}

wait_for backend http://backend:8000/api/schema/
wait_for frontend http://frontend/
wait_for mailpit http://mailpit:8025/api/v1/info

exec "$@"

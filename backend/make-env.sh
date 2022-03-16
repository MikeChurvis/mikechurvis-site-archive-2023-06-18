#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o allexport

cat \
"$1/shared.env" \
"$1/backend.env" \
> "$2/.env"
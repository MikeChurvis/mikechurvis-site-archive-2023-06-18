#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o allexport

_ORIGINAL_DIR=$(pwd)
trap 'cd "${_ORIGINAL_DIR}"' exit

cd "$1"

cat shared.env shared.production.env backend.env backend.production.env > "${_ORIGINAL_DIR}/.env"

cd "${_ORIGINAL_DIR}"
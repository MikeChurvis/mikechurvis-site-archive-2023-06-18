#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o allexport

cat \
"$1/shared.env" \
"$1/frontend.env" \
> .env

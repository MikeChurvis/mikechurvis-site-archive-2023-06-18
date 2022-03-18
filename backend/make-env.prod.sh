#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o allexport

cat \
"$1/shared.env" \
"$1/shared.production.env" \
"$1/backend.env" \
"$1/backend.production.env" \
> .env.prod

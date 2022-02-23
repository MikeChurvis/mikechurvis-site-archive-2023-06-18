#!/usr/bin/env bash

CALL_DIRECTORY=$(pwd)
SCRIPT_DIRECTORY=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
ENV_DIRECTORY="${SCRIPT_DIRECTORY}/../../env"

cd "${ENV_DIRECTORY}" || return

echo "Importing environment variables:"
set -o allexport

echo "- .env.shared"
source .env.shared

echo "- .env.frontend"
source .env.frontend

if [ "$1" == "-p" ]; then
  echo "- .env.frontend.production"
  source .env.frontend.production
fi

set +o allexport

cd "${CALL_DIRECTORY}" || return
#!/usr/bin/env bash

set -euo pipefail

CALL_DIR=$(pwd)
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
BASE_DIR="${SCRIPT_DIR}/.."
FRONTEND_DIR="${BASE_DIR}/frontend/portfolio"


echo "[BUILD][FRONTEND] Building Astro project."
cd "${FRONTEND_DIR}" || return
npm run build
touch dist/.nojekyll


cd "${BASE_DIR}" || return
git add -A
git status
git commit -m "Deployment Build ($(date))"
#git push
git subtree split --prefix frontend/portfolio/dist -b gh-pages
git push -f origin gh-pages:gh-pages
git branch -D gh-pages

cd "${CALL_DIR}" || return
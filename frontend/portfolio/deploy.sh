#!/usr/bin/env bash

CALL_DIRECTORY=$(pwd)
SCRIPT_DIRECTORY=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
PROJECT_ROOT_DIRECTORY="${SCRIPT_DIRECTORY}/../.."

cd "${SCRIPT_DIRECTORY}"
npm run build

cd "${PROJECT_ROOT_DIRECTORY}"
git add -A
git status
git commit -m "Deployment Build ($(date))"
git push
git subtree split --prefix frontend/portfolio/dist -b gh-pages
git push -f origin gh-pages:gh-pages
git branch -D gh-pages

cd "${CALL_DIRECTORY}"
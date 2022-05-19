#!/usr/bin/env bash

function log {
  echo "[npm-run-build.sh] $1"
}

log "Making production .env file."
source make-env.prod.sh ../../env-source 

log "Building Astro project."
astro build 
touch dist/.nojekyll

log "Writing CNAME file."
set -u
source .env
echo "${SITE_HOST_FRONTEND}" > dist/CNAME 

#!/usr/bin/env bash

###################################
# Process command line arguments. #
###################################

while [ -z "$1" ]; do
  case "$1" in
  --ssh-key-path)
    shift
    DROPLET_SSH_KEY_PATH="${1-}"
    ;;
  --droplet-ip)
    shift
    DROPLET_IP="${1-}"
    ;;
  esac
  shift
done

###################################
# Prepare project for deployment. #
###################################

if [ -n "${DROPLET_SSH_KEY_PATH:-}" ]; then
  echo "The path to the droplet's private SSH key must be provided as an environment variable (DROPLET_SSH_KEY_PATH)."
  exit 1
elif [ -n "${DROPLET_IP:-}" ]; then
  echo "The droplet's IP address must be provided as an environment variable (DROPLET_IP)."
  exit 1
elif [ -n "$(git rev-parse --show-prefix)" ]; then
  echo "This command must be called from the project root."
  exit 1
elif [ -n "$(git status --porcelain)" ]; then
  echo "There are uncommitted changes in the working tree. Commit or stash changes before running this script."
  exit 1
fi

# Bash set args used:
# -e:           Exit the first time a command returns an non-zero
#               exit status.
# -u:           Exit when a substitution is made with a variable
#               that has not been set.
# -x:           Print each command as it is executed.
# -o pipefail:  Do not mask pipeline errors; return the exit code of
#               the first failing command.
set -euxo pipefail

PORTFOLIO=$(pwd)
trap 'cd "${PORTFOLIO}"' exit

# Build temporary environment variable files.
cd "${PORTFOLIO}/deployment"

BACKEND_ENV_PATH="${PORTFOLIO}/backend/.env"
FRONTEND_ENV_PATH="${PORTFOLIO}/frontend/portfolio/.env"

trap 'rm -f "${FRONTEND_ENV_PATH}"' exit
source make-env.sh "${PORTFOLIO}/env" \
  --frontend \
  --production \
  --output "${FRONTEND_ENV_PATH}"

trap 'rm -f "${BACKEND_ENV_PATH}"' exit
source make-env.sh "${PORTFOLIO}/env" \
  --backend \
  --production \
  --output "${BACKEND_ENV_PATH}"

##################################
# Build and deploy the frontend. #
##################################

cd "${PORTFOLIO}/frontend/portfolio"

npm run build
touch dist/.nojekyll

trap 'git branch -D gh-pages' exit
git subtree split --prefix frontend/portfolio/dist -b gh-pages
git push -f origin gh-pages:gh-pages

#################################
# Build and deploy the backend. #
#################################

scp

#!/usr/bin/env bash

# Perform data migrations and static file collection.
source venv/bin/activate
python manage.py migrate
python manage.py collectstatic --no-input --clear

# Turn on bash's job control (allows process suspension).
set -m

# Run the main command and put the resulting process in the background.
exec "$@" &

# Start the task consumer.
python manage.py run_huey

# Return the main command's process to the foreground.
fg %1

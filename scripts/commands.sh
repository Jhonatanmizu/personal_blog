#!/bin/sh

# Stop script when a command fails
set -e

wait_psql.sh
# collectstatic.sh
migrate.sh
runserver.sh

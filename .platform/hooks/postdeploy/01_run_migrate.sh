#!/bin/bash

if [ "$EB_IS_COMMAND_LEADER" = "true" ]; then
  echo "Running DB migrate as command leader"
  CONTAINER_ID=$(docker ps -q)
  docker exec "$CONTAINER_ID" python manage.py migrate --noinput
else
  echo "Skipping migration on this instance"
fi
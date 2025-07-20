#!/bin/bash

# Dynamically get container ID (Elastic Beanstalk default is usually the only container running)
CONTAINER_ID=$(docker ps -q)

echo "Running migrate inside container $CONTAINER_ID"

docker exec "$CONTAINER_ID" python manage.py migrate --noinput

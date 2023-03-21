#!/bin/bash

echo "START SCRIPT"
echo "DOCKER COMPOSE UP"
docker-compose up -d --build
echo "START API TESTING"
docker-compose exec web pytest tests/
echo "DOCKER COMPOSE DOWN"
docker-compose down
# shellcheck disable=SC2046
fuser -k 5557/tcp && fuser -k 8000/tcp
echo "FINISH"

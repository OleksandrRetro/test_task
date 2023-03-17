#!/bin/bash

echo "START SCRIPT"
echo "DOCKER COMPOSE UP"
docker-compose up -d --build
echo "START TESTING"
docker-compose exec web pytest .
echo "DOCKER COMPOSE DOWN"
docker-compose down
echo "FINISH"
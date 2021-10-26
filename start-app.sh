#!/bin/sh
docker-compose build
docker-compose run --rm node sh -c "npm install -g create-react-app && create-react-app react-front"
docker-compose up -d

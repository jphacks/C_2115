#!/bin/sh
docker-compose build
docker-compose run --rm node sh -c "npm install -g create-react-app && create-react-app react-front && npm install @material-ui/core && npm install @mui/material@emotion/react@emotion/styled && npm install axios && npm install --save react-dropzone && npm install react-bootstrap bootstrap@5.1.3"
docker-compose up -d

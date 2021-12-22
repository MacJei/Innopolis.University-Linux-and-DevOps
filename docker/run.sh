#!/bin/bash
app="flaskapp"
docker build -t ${app} .
docker run -d \
  --name=${app} \
  -v $PWD:/app ${app}

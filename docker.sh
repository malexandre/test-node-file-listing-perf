#!/bin/sh
docker build -t test-node-list .
docker run -ti --rm -v content:/code/content test-node-list
docker rmi test-node-list

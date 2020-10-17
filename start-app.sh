#!/bin/bash

docker-compose build blog_exporter
docker-compose run blog_exporter

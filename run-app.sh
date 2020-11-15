#!/bin/bash

curl -LO http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_mac64.zip
export DRIVER_EXECUTABLE="./chromedriver"

pip3 install -r requirements.txt
python3 -m src.main

rm -f "./chromedriver*"
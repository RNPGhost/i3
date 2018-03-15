#!/bin/bash

SCREENSAVER_FOLDER_PATH=~/pictures/screensavers/seaofthieves/
i3lock -i $(find $SCREENSAVER_FOLDER_PATH -name "*.png" | shuf -n1) -c 000000 -t -e

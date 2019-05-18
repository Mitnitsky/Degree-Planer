#!/usr/bin/env bash

python -OO -m PyInstaller main.py \
        --name degreePlanner \
        --add-data 'images/:images' \
        --add-data 'db/:db' \
        --add-data 'settings.json:settings.json' \
        -c \
        -w
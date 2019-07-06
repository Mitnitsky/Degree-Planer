#!/usr/bin/env bash

pyinstaller main.py \
        --clean \
	-D \
	--name degreePlanner \
        --add-data 'images/:images' \
        --add-data 'templates/:templates' \
        --add-data 'saves/:saves' \
        --add-data 'db/:db' \
        --add-data 'settings.json:.' \
        -w

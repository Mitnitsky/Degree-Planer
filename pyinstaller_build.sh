#!/usr/bin/env bash

pyinstaller main.py \
        --clean \
	-D \
	--name degreePlanner \
        --add-data 'images/:images' \
        --add-data 'db/:db' \
        -w

#!/usr/bin/env bash

python -OO -m PyInstaller main.py \
        --clean \
	-D \
	--name degreePlanner \
        --add-data 'images/:images' \
        --add-data 'db/:db' \
        -w

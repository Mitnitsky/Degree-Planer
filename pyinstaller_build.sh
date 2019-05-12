 
python -OO -m PyInstaller main.py \
        --name degreePlanner \
        --add-data 'images/:images' \
        --add-data 'db/:db' \
        -w 


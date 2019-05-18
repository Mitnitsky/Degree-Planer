python -OO -m PyInstaller main.py ^
	--clean ^
        --name "Degree Planner" ^
        --add-data images/;images ^
        --add-data settings.json;settings.json ^
        --add-data db/;db ^
	    -i images/main_icon.ico ^
	    -c ^
        -w

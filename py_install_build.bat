python -OO -m PyInstaller main.py ^
	--clean ^
        -D ^
        --name "Degree Planner" ^
        --add-data images/;images ^
        --add-data db/;db ^
	    -i images/main_icon.ico ^
	    -c ^
        -w

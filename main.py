import json
from sys import exit

from PyQt5 import QtWidgets, QtGui

from logic import MyWindow


def createSettingsFile():
    with open("settings.json", "w") as write_file:
        data = {'save_file': '', 'language': 'heb', 'dimensions': [{'width': 1320, 'height': 565}]}
        json.dump(data, write_file, indent=4)


def checkSettingsFile():
    try:
        read_write_file = open("settings.json", "r+")
        if read_write_file:
            data = json.load(read_write_file)
            if 'save_file' not in data.keys():
                data['save-file'] = ''
            if 'language' not in data.keys():
                data['language'] = 'heb'
            if 'dimensions' not in data.keys():
                data['dimensions'] = [{'width': 1320, 'height': 565}]
            read_write_file.seek(0)
            json.dump(data, read_write_file, indent=4)
            read_write_file.truncate()
        else:
            createSettingsFile()
    except (FileNotFoundError, KeyError, json.decoder.JSONDecodeError):
        createSettingsFile()


if __name__ == "__main__":
    checkSettingsFile()
    app = QtWidgets.QApplication([])
    app.setQuitOnLastWindowClosed(True)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("images/main_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    app.setWindowIcon(icon)
    # Linux case
    if 'Breeze' in QtWidgets.QStyleFactory.keys():
        app.setStyle('Breeze')
    else:
        # Windows case
        app.setStyle('Fusion')
    application = MyWindow()
    exit(app.exec())

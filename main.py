from PyQt5 import QtWidgets
from logic import MyWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MyWindow()
    exit(app.exec())
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
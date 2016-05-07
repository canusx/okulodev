import sys
from PyQt5.QtWidgets import QApplication

from views.MainWindow import MainWindow

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = MainWindow()
    main.showMaximized()
    sys.exit(app.exec_())
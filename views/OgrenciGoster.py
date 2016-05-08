from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.uic import loadUi


class OgrenciGoster(QDialog):

    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent)
        loadUi("ui/OgrenciGoster.ui",self)
        self.parent = parent
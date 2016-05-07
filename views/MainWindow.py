from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from libs.database import Database
from views.OgrenciEkleWindow import OgrenciEkleWindow
from views.OgrenciListesi import OgrenciListesi


class MainWindow(QMainWindow):

    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent)
        loadUi("ui/MainWindow.ui",self)
        print(self.menuBar().__dir__())
        self.ogrenci_ekle.triggered.connect(self.ogrenciEkleWindowShow)
        self.ogrenciList.triggered.connect(self.ogrenciListesi)
        self.db = Database("db/main.db")



    def ogrenciListesi(self):
        self.ogrenciler = OgrenciListesi(self)
        try:
            self.mdi.addSubWindow(self.ogrenciler)
        except:
            pass
        try:
            self.ogrenciler.show()
        except:
            pass

    def ogrenciEkleWindowShow(self):
        self.ogrenciEkleWindow = OgrenciEkleWindow(self)
        try:
            self.mdi.addSubWindow(self.ogrenciEkleWindow)
        except:
            pass
        try:
            self.ogrenciEkleWindow.show()
        except:
            pass





from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QGraphicsView, QGraphicsScene, QPushButton, QMessageBox
from PyQt5.uic import loadUi

from views.OgrenciGoster import OgrenciGoster


class OgrenciListesi(QMainWindow):

    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent)
        loadUi("ui/OgrenciListesi.ui",self)
        self.parent = parent
        self.getAll()
        self.pushButton.clicked.connect(self.filtre)
    def filtre(self):
        filtre = {}
        if self.ad.text().replace(" ","") != "":
            filtre.update({"ad":self.ad.text().replace(" ","")})

        if self.soyad.text().replace(" ","") != "":
            filtre.update({"soyad":self.soyad.text().replace(" ","")})

        if self.no.text().replace(" ","") != "":
            filtre.update({"okul_no":self.no.text().replace(" ","")})

        self.getAll(filtre)

    def showogrenci(self):
        try:
            ogrenci = OgrenciGoster(self.parent)
            self.parent.mdi.addSubWindow(ogrenci)
            ogrenci.show()
            data = self.sender().data

            ogrenci.ad.setText(data[1])
            ogrenci.soyad.setText(data[2])
            ogrenci.anneadi.setText(data[4])
            ogrenci.babaadi.setText(data[5])

            gp = QGraphicsScene(self)
            ogrenci.graphicsView.setScene(gp)
            ogrenci.graphicsView.setFixedHeight(100)
            ogrenci.graphicsView.setFixedWidth(100)
            if data[8] is not None:
                gp.addPixmap(QPixmap("db/%s" % data[8]))
                ogrenci.graphicsView.show()

            nots = self.parent.db.getNot(data[0])
            ogrenci.tableWidget.setRowCount(len(nots))
            ogrenci.tableWidget.setColumnCount(1)
            ogrenci.tableWidget.setHorizontalHeaderLabels(["Notlar"])
            z = 0
            for i in nots:

                ogrenci.tableWidget.setItem(z,0,QTableWidgetItem(i[2]))
                z +=1

        except Exception as e:
            print(e)
    def getAll(self,filter={}):
        self.tableWidget.clear()
        try:
            data = self.parent.db.get(filter)
            self.tableWidget.setRowCount(len(data))
            self.tableWidget.setColumnCount(5)
            self.tableWidget.setHorizontalHeaderLabels(["Resim","Ad","Soyad","No"])


            iz = 0

            for i in data:
                ad = QTableWidgetItem(i[1])
                soyad = QTableWidgetItem(i[2])
                no = QTableWidgetItem(i[3])
                gp = QGraphicsScene(self)

                resim = QGraphicsView(gp)
                resim.setFixedHeight(100)
                resim.setFixedWidth(100)
                if i[8] is not None:
                    gp.addPixmap(QPixmap("db/%s" % i[8]))
                    resim.show()

                self.tableWidget.setCellWidget(iz,0,resim)

                btn = QPushButton(self)
                btn.setText("Göster")
                btn.data = i
                btn.clicked.connect(self.showogrenci)
                self.tableWidget.setItem(iz,1,ad)
                self.tableWidget.setItem(iz,2,soyad)
                self.tableWidget.setItem(iz,3,no)
                self.tableWidget.setCellWidget(iz,4,btn)
                self.tableWidget.setRowHeight(iz,100)


                iz +=1
        except Exception as e:
            print(e)

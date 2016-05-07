from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QGraphicsView, QGraphicsScene
from PyQt5.uic import loadUi


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


    def getAll(self,filter={}):
        self.tableWidget.clear()
        try:
            data = self.parent.db.get(filter)
            self.tableWidget.setRowCount(len(data))
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(["Resim","Ad","Soyad","No"])


            iz = 0

            for i in data:
                print(i)
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
                self.tableWidget.setItem(iz,1,ad)
                self.tableWidget.setItem(iz,2,soyad)
                self.tableWidget.setItem(iz,3,no)
                self.tableWidget.setRowHeight(iz,100)
                iz +=1
        except Exception as e:
            print(e)

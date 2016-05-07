from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem, QFileDialog, QGraphicsScene
from PyQt5.uic import loadUi


class OgrenciEkleWindow(QDialog):

    def __init__(self,parent=None):
        QDialog.__init__(self,parent)
        loadUi("ui/Ogrenci.ui",self)
        try:
            self.parent = parent
            self.not_ekle.clicked.connect(self.NotEkle)
            self.nots.setHorizontalHeaderLabels(["Not"])
            self.kaydet.clicked.connect(self.OgrenciKaydet)
            self.fotograf_ekle.clicked.connect(self.FotografEkle)
            self.filename = None
            self.gscene = QGraphicsScene(self)
            self.graphicsView.setScene(self.gscene)
        except Exception as e:
            print(e)

    def FotografEkle(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Dosya Seç',".",filter="Resim Dosyası (*.jpg *.jpeg *.png *.bmp)")
            self.filename = fname[0]
            px = QPixmap(self.filename)
            self.gscene.addPixmap(px)
            self.graphicsView.show()

        except Exception as e:
            print(e)


    def controlForm(self,elems):
        for elem in elems:
            if len(elem.text().replace(" ","")) == 0:
                return False
        return True

    def OgrenciKaydet(self):
        try:
            if self.controlForm([self.ad,self.soyad,self.anne,self.baba,self.dyeri,self.no]):
                nots = []
                for i in range(self.nots.rowCount()):
                    nots.append(self.nots.item(i,0).text())

                durum = self.parent.db.create_student(self.ad.text(),self.soyad.text(),self.no.text(),self.anne.text(),self.baba.text(),self.dyeri.text(),self.dtarihi.text(),nots,self.filename )
                if durum is False:
                    QMessageBox.critical(self,"Hata","Öğrenci eklenemedi . Yazılım Hatası : %s" % self.parent.db.error)
                self.close()
                #print(self.dtarihi.text())
                #print(dir(self.dtarihi))
            else:
                QMessageBox.critical(self,"Hata","Tüm alanları doldurmalısınız.")
        except Exception as e:
            print(e)
    def NotEkle(self):
        if len(self.nottext.text().replace(" ","")) > 0:

            self.nots.setRowCount(self.nots.rowCount()+1)
            item = QTableWidgetItem(self.nottext.text())
            self.nots.setItem(self.nots.rowCount()-1,0,item)
            self.nottext.setText("")

        else:
            QMessageBox.critical(self,"Hata","Not boş bırakılamaz.")




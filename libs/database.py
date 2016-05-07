import os
import sqlite3
import shutil
import sys


class Database(object):

    def __init__(self,db):

        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()
        self.error = ""
    def get(self,filter=None):
        where = ""
        for field,value in filter.items():
            if where != "":
                where += " AND "

            where += " %s = '%s'" % (field,value)
        if where != "":
            where = " where " + where
        self.cursor.execute("select * from ogrenciler" + where)
        return self.cursor.fetchall()

    def create_student(self,name,surname,number,father_name,mother_name,birth_place,birth_date,nots=[],file=None):
        """
        Creating a stundent
        :param name: str
        :param surname: str
        :param number: str
        :param father_name: str
        :param mother_name: str
        :param birth_place: str
        :param birth_date: date
        :param nots: list
        :return: boolean
        """
        dosya = ""
        if file is not None:
            dosya = os.path.basename(file)
            shutil.copy(file,"db/%s" % dosya)

        try:
            sql = """
                insert into ogrenciler
                (ad,soyad,okul_no,anne_adi,baba_adi,dogum_yeri,dogum_tarihi,fotograf)
                VALUES
                ("%s","%s","%s","%s","%s","%s","%s","%s")
            """ % (name,surname,number,mother_name,father_name,birth_place,birth_date,dosya)

            self.cursor.execute(sql)
            self.conn.commit()
            ogrenci_id = self.cursor.lastrowid
            for i in nots:
                sql_not = """
                insert into ogrenci_not (ogrenci_id,`not`) VALUES ("%d","%s")
                """ % (ogrenci_id,i)
                self.cursor.execute(sql_not)
                self.conn.commit()
            return True
        except Exception as e:
            self.error = str(e)
            return False



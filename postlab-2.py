import mysql.connector
import pytest

db_conn = mysql.connector.connect(host="localhost",user="root",password="Shiva_789",database="dwmlab",port="3306")
cursor = db_conn.cursor()


class Army():
    def __init__(self, fname, lname, status, nod):
        self.fname=fname
        self.lname=lname
        self.status=status
        self.nod=nod
    def insert_record(self):
        try:
            sql = "insert into student(fname,lname,status,nod) values(%s,%s,%s,%s)"
            val=(self.fname, self.lname, self.status, self.nod)
            cursor.execute(sql,val)
            db_conn.commit()
            return cursor.rowcount
        except Exception as e:
            print("Exception",e)
        else:
            print("No Exception")


fname = input("Enter First Name: ")
lname = input("Enter Last Name: ")
status = input("Enter Status: ")
nod = input("Enter No of days: ")
d = Army(fname,lname,status,nod)

def test_insert_record():
    assert d.insert_record() == 1



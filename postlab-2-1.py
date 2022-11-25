import mysql.connector
import pytest

db_conn = mysql.connector.connect(host="localhost",user="root",password="Shiva_789",database="dwmlab",port="3306")
cursor = db_conn.cursor()

@pytest.mark.deleterecord
def test_delete_record():
    try:
        cursor.execute("delete from student where id=3")
        db_conn.commit()
        assert cursor.rowcount == 1
    except Exception as e:
        print("Exception Occured", e)
    else:
        print("No Exception")


@pytest.mark.updaterecord
def test_update_record():
    try:
        cursor.execute("update student set status='fail' where id=2")
        db_conn.commit()
        assert cursor.rowcount == 1
    except Exception as e:
        print("Exception Occured", e)
    else:
        print("No Exception")


@pytest.mark.viewrecord
def test_view_record():
    cursor.execute(" select * from student")
    for row in cursor:
        print(row[0], row[1], row[2], row[3], row[4])
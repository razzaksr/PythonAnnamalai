# database creation

from pymysql import *

try:
    var = connect("localhost", "root", "")
    qry = "create database avscollege"
    cur = var.cursor()
    cur.execute(qry)
    var.close()
except:
    var.rollback()
finally:print("Database created")
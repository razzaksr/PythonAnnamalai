# creating table with primary key and auto increment

from pymysql import *

try:
    var = connect("localhost", "root", "", "avscollege")
    qry = "create table events(eid int(4) not null auto_increment, edate date not null, edept varchar(30) not null, eorg varchar(30) not null, participants text, winner varchar(30), prize int(5) not null, primary key(eid))"
    cur = var.cursor()
    cur.execute(qry)
    var.close()
except Exception as e:
    print(e)
    var.rollback()
finally:print("Table created")
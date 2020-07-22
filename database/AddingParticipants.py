# adding participants into events

from pymysql import *

try:
    temp=""
    parts=input("Enter the parrticpant name: ")
    id=int(input("Enter event id: "))
    con = connect("localhost", "root", "", "avscollege")
    cur = con.cursor()
    read="select participants from events where eid=%d"%(id)
    cur.execute(read)
    exists=cur.fetchall()
    for x in exists[0]:
        temp+=x#+"/"
    temp+=parts+"/"
    con.autocommit(True)
    qry = "update events set participants='%s' where eid=%d"%(temp,id)
    cur.execute(qry)
    con.close()
except Exception as e:
    print(e)
    con.rollback()
finally:print("Record updated")
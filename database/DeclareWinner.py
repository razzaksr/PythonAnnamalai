# Declare winner from participants

from pymysql import *

try:
    id = int(input("Enter event id: "))
    con = connect("localhost", "root", "", "avscollege")
    cur = con.cursor()
    read="select participants from events where eid=%d"%(id)
    cur.execute(read)
    exists=cur.fetchall()
    for x in exists[0]:
        print(x)
    con.autocommit(True)
    win = input("Declare who is the winner is: ")
    qry="update `events` set `winner`='"+win+"' where `eid` ="+str(id)+" and `participants` like '%"+win+"%'"
    print("Winner declared")
    cur.execute(qry)
    con.close()
except Exception as e:
    print(e)
    con.rollback()
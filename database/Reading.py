# Report

from pymysql import *

try:
    con = connect("localhost", "root", "", "avscollege")
    cur = con.cursor()
    # fetching all details/column of all the events
    read="select * from events"
    cur.execute(read)
    record=cur.fetchall()
    for x in record:
        print(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7])

    # fetching particular details/column of all the events
    read = "select edept,edate from events"
    cur.execute(read)
    record = cur.fetchall()
    for x in record:
        print(x[0], x[1])
    # fetching particular details/column of all the events by user told
    given=input("Tell which column you want:")
    read = "select %s from events"%(given)
    cur.execute(read)
    record = cur.fetchall()
    for x in record:
        print(x[0])
    # fetching all details/column of particular event by user given eid
    given = int(input("Tell which event want by id:"))
    read = "select * from events where eid=%d" % (given)
    cur.execute(read)
    record = cur.fetchone()
    print(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7])
    # fetching all details/column of particular event by user given eorg/edept/....
    given = input("Tell which event want by event name:")
    read = "select * from events where ename='%s'" % (given)
    cur.execute(read)
    record = cur.fetchall()
    for x in record:
        print(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7])
    # fetching all details/column of particular event by user given edate interval
    start = input("Tell start date:")
    end = input("Tell end date:")
    read = "select * from events where edate between '%s' and '%s'" % (start,end)
    cur.execute(read)
    record = cur.fetchall()
    for x in record:
        print(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7])
    # fetching all details/column of particular event by user given edate interval
    start = input("Tell start date:")
    end = input("Tell end date:")
    given = input("Tell which event want by department:")
    read = "select * from events where edate between '%s' and '%s' and edept='%s'" % (start, end, given)
    cur.execute(read)
    record = cur.fetchall()
    for x in record:
        print(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7])
    start = input("Tell start date:")
    end = input("Tell end date:")
    given = input("Tell which data you want:")
    read = "select %s from events where edate between '%s' and '%s'" % (given,start,end)
    cur.execute(read)
    record = cur.fetchall()
    for x in record:
        print(x[0])
    con.close()
except Exception as e:
    print(e)
    con.rollback()
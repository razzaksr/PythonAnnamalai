from pymysql import *

try:
    con = connect("localhost", "root", "", "avscollege")
    cur = con.cursor()
    # counting all events
    read="select count(*) from events"
    cur.execute(read)
    print("Total events",cur.fetchone())
    # counting all events conducted by particular department
    dep=input("Tell us dept: ")
    read = "select count(*) from events where edept='"+dep+"'"
    cur.execute(read)
    print("events done by",dep,"is",cur.fetchone())
    # counting all events conducted by particular organiser
    org = input("Tell us organizer: ")
    read = "select count(*) from events where eorg='" + org + "'"
    cur.execute(read)
    print("events done by", org, "is", cur.fetchone())
    con.close()
except Exception as e:
    print(e)
    con.rollback()
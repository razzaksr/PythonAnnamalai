# New event gonna added in table besides the participants and winner

from pymysql import *

try:
    date = input("Tell us event date like yyyy-MM-dd: ")
    name = input("Tell us name of the event: ")
    dept = input("Tell us which department gonna conduct the event: ")
    organiser = input("Tell us who gonna organise the event: ")
    prize = int(input("Tell us the prize amount of the event: "))
    con = connect("localhost", "root", "", "avscollege")
    con.autocommit(True)
    qry = """insert into events(edate,ename,edept,eorg,prize) values('%s','%s','%s','%s',%d)""" % (
    date, name, dept, organiser, prize)
    cur = con.cursor()
    cur.execute(qry)
    con.close()
except ValueError as verror:
    print(verror)
    prize = int(input("Tell us the prize amount of the event: "))
    con.rollback()
except Exception as e:
    print(e)
    con.rollback()
finally:print("Record inserted")
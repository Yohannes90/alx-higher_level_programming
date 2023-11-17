#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    conn = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306
    )
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities,\
                 states WHERE cities.state_id = states.id ORDER BY id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()

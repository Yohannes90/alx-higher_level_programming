#!/usr/bin/python3
""" display value of states table in hbtn_0e_0_usa where name match argument
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    conn = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306
    )
    cur = conn.cursor()
    state = argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY\
                '{}';".format(state))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()

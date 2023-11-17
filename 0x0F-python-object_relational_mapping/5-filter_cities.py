#!/usr/bin/python3
""" takes in the name of a state as an argument and lists all cities of that
    state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    conn = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306
    )
    cur = conn.cursor()
    state = argv[4]
    cur.execute("SELECT cities.name FROM cities, states WHERE cities.state_id\
                 = states.id AND states.name LIKE BINARY %s", (state, ))

    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))

    cur.close()
    conn.close()

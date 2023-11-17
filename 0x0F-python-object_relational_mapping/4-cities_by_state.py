#!/usr/bin/python3

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host='localhost', user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities,\
                 states WHERE cities.state_id = states.id ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host='localhost', user=argv[1], passwd=argv[2], db=argv[3], port=3306
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()

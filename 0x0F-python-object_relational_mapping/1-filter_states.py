#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host='localhost', user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name like 'N%'")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()

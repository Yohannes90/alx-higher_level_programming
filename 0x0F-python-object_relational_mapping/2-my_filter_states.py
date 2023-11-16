#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    state = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE '{}'".format(state))
    row = cur.fetchone()
    print(row)

    cur.close()
    conn.close()

#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_host = "localhost"
    db_usr = argv[1]
    db_pass = argv[2]
    db_name = argv[3]
    conn = MySQLdb.connect(
        host=db_host, user=db_usr, passwd=db_pass, db=db_name, port=3306
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()

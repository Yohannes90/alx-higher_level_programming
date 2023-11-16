#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host='localhost', user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    state = sys.argv[4]
    cur.execute("SELECT cities.name FROM cities, states WHERE\
            cities.state_id = states.id AND states.name LIKE %s", (state, ))

    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))

    cur.close()
    conn.close()

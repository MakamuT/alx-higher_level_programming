#!/usr/bin/python3
""" ists all states with a name starting with N """

import sys
import MySQLdb

if __name == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    c = db.cursor()
    c.execute("""SELECT * FROM states  WHERE name
              LIKE BINARY 'N%' ORDER BY states.id ASC""")
    rows = c.fetchall()
    for row in rows:
        print(row)
        c.close()
        db.close()

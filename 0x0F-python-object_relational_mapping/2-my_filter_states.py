#!/usr/bin/python3
"""takes in an argument and displays all
   values in the states table of hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    c = db.cursor()
    c.exexcute("""SELECT * FROM states WHERE name LIKE BINARY
               '{}' ORDER BY states.id ASC""".format(sys.argv[4]))
    rows = c.fecthall()
    for row in rows:
        print(row)
    c.close()
    db.close()

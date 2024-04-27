#!/usr/bin/python3
""" ists all states with a name starting with N """

import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        con = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                             passwd=mysql_password)
    except MySQLdb.Error as e:
        print("Error connecting to database: {}".format(e))
        sys.exit(1)

    c = con.cursor()
    c.execute("""SELECT * FROM states  WHERE name
              LIKE BINARY 'N%' ORDER BY states.id ASC""")
    rows = c.fetchall()
    for row in rows:
        print(row)
        c.close()
        con.close()

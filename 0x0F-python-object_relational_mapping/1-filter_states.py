#!/usr/bin/python3
""" ists all states with a name starting with N """

import sys
import MySQLdb

if __name__ == "__main__":
    """access database"""
    if len(sys.argv) < 4:
        print("Usage: {} [mysql_username=root] [mysql_password=] <db_name>"
              .format(sys.argv[0]))
        sys.exit(1)

        mysql_username = "root"
        mysql_password = ""
        db_name = sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                             passwd=mysql_password)
        cursor = db.cursor()
        cursor.execute("""SELECT * FROM states  WHERE name
                       LIKE BINARY 'N%' ORDER BY states.id ASC""")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print("Error connecting to database: {}", e)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()


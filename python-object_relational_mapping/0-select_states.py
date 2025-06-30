#!/usr/bin/python3
"""
Return all table values (tables 'states')
Parameters given to the script:
mysql username, mysql password, database name
"""

import MySQLdb
import sys


def state_list(username, password, database_name):
    """Connects to MySQL server"""
    try:
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
        states = cursor.fetchall()
        for state in states:
            print(state)

        cursor.close()
        conn.close()

    except MySQLdb.Error as error:
        print(f"Error connecting to MySQL or executing query: {error}")


if __name__ == "__main__":
    state_list(sys.argv[1], sys.argv[2], sys.argv[3])

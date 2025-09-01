#!/usr/bin/python3
"""Module for selecting all states from the database."""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()

    cursor.execute('SELECT * FROM states ORDER BY id ASC')

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()

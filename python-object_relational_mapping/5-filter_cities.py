#!/usr/bin/python3
"""All cities by state"""

import sys
import MySQLdb


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()
    query = (
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC;"
    )
    cur.execute(query, (state_name,))

    rows = cur.fetchall()
    cities = [row[0] for row in rows]
    print(", ".join(cities))

    cur.close()
    db.close()

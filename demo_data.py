import sqlite3
import pandas as pd

# ESTABLISH connection with demo_data.squlite3
# def create_connection():
#     conn = None
#     try:
#         conn = sqlite3.connect('demo_data.sqlite3')
#     except Error as e:
#         print(e)
#     return conn # ESTABLISH connection with demo_data.squlite3
conn = sqlite3.connect('demo_data.sqlite3')
demo = DATA = [
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
]

def make_db():
    """Make and populate the demo database."""
    curs = conn.cursor()
    curs.execute('CREATE TABLE demo (s char(1), x int, y int);')
    for datum in DATA:
        curs.execute('INSERT INTO demo (s, x, y) VALUES ' + str(datum))
    curs.close()
    conn.commit()

    def run_queries():
        curs = conn.cursor()
        print(curs.execute('SELECT COUNT(*) FROM demo;').fetchall())
        print(curs.execute('SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >=5;').fetchall())
        print(curs.execute('SELECT COUNT(DISTINCT y) FROM demo;').fetchall())

if __name__ == "__main__":
    make_db()
    run_queries()


# def demo():
#     cursor = conn.cursor()
#     cursor.execute('CREATE TABLE demo (s TEXT PRIMARY KEY, x INTEGER NOT NULL, y INTEGER NOT NULL);')
#     cursor.close()
#     conn.commit()
# if __name__ = "__main__":
#     create_connection()
#     demo()
# #
#
# cursor.execute('INSERT INTO demo (s, v, f) '
#                    'VALUES ('g', 3, 9);
#
#     INSERT INTO demo (s, v, f)
#     VALUES ('v', 5, 7);
#
#     INSERT INTO demo (s, v, f)
#     VALUES ('f', 8, 7);')
#

#
# # This function selects all rows from the tasks table and displays the data
# def select_all_tasks(conn):
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM demo")
#
#     rows = cur.fetchall()
#
#     for row in rows:
#         print(row)
#
# # NUMBER of rows in df
# row_count = len(demo.index)
#
# print(row_count)
#
# # SELECT rows in df where both x & y are greater than 5
# xy_at_least_5 = demo[(demo['x')] > 5 &
#                 demo[(demo['y')] > 5 &
#
# print(xy_at_least_5)
#
# # NUMBER of unique values of `y`
#
# xy_at_least_5 = demo.y.unique()
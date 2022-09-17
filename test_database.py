from database import Database
from my_time import MyTime
import sqlite3


def test():
    start = MyTime(10, 30)
    end = MyTime(11, 00)

    db = Database()
    db.create_table()
    db.get_times()
    db.insert_data(start, end)
    db.get_times()

    # conn = sqlite3.connect(":memory:")
    # c = conn.cursor()
    # c.execute("""CREATE TABLE test (
    # first_name text,
    # last_name text
    # )""")
    # conn.commit()
    # c.execute("SELECT * FROM test")
    # print(c.fetchall())


from database import Database
from my_time import MyTime
import sqlite3


def test():
    start = MyTime(10, 30)
    end = MyTime(11, 00)

    db = Database()
    db.create_table()
    # db.get_times()
    db.insert_data(start, end)
    # db.get_times()

import os
from database import Database
from my_time import MyTime


def test():
    start = MyTime(10, 30)
    end = MyTime(11, 00)
    database_file = "times.db"
    db = Database(database_file)
    if not db.check_table_exists():
        db.create_table()
    db.insert_data(start, end)
    db.get_times()
    db.close()

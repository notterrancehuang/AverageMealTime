from databases.database import Database
from my_time import MyTime


def test():
    start_time = MyTime(10, 30)
    end_time = MyTime(11, 00)
    database_file = "times.db"
    db = Database(database_file)
    db.create_table()
    db.insert_data("Terrance", start_time, end_time)
    db.get_times()
    db.close()

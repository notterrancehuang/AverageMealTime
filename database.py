import sqlite3
from my_time import MyTime


class Database:

    def __init__(self, database_file):
        self.conn = sqlite3.connect(database_file)
        self.c = self.conn.cursor()

    def close(self):
        self.conn.close()

    def create_table(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS times (
                        start_hour int,
                        start_minute int,
                        end_hour int,
                        end_minute int,
                        duration_hour int,
                        duration_minute int
                        );""")

    def insert_data(self, start: MyTime, end: MyTime):
        duration = start.time_diff(end)
        self.c.execute(
            "INSERT INTO times VALUES (?, ?, ?, ?, ?, ?)", (start.hour,
                                                            start.minute,
                                                            end.hour,
                                                            end.minute,
                                                            duration.hour,
                                                            duration.minute))
        self.conn.commit()

    def get_times(self):
        # print out whole table
        self.c.execute("SELECT * FROM times")
        print(self.c.fetchall())

    def check_table_exists(self):
        self.c.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='times'")
        test_table_exist = self.c.fetchall()
        return test_table_exist

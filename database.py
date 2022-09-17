import sqlite3
from my_time import MyTime
import os.path


class Database:
    database_file = "times.db"

    def __init__(self):
        self.conn = sqlite3.connect(Database.database_file)
        self.c = self.conn.cursor()

    def close(self):
        self.conn.close()

    def create_table(self):
        with self.conn:
            if not os.path.exists(self.database_file):
                self.c.execute("""CREATE TABLE IF NOT EXISTS times (
                            start_hour int,
                            start_minute int,
                            end_hour int,
                            end_minute int,
                            duration_hour int,
                            duration_minute int
                            );""")

    def insert_data(self, start: MyTime, end: MyTime):
        with self.conn:
            duration = start.time_diff(end)
            self.c.execute(
                "INSERT INTO times VALUES (?, ?, ?, ?, ?, ?)", (start.hour,
                                                                start.minute,
                                                                end.hour,
                                                                end.minute,
                                                                duration.hour,
                                                                duration.minute))

    def get_times(self):
        # print out whole table
        with self.conn:
            self.c.execute("SELECT * FROM times")
            print(self.c.fetchall())

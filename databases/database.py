import sqlite3
from my_time import MyTime


class Database:
    def __init__(self, database_file):
        self.conn = sqlite3.connect(database_file)
        self.c = self.conn.cursor()

    def close(self):
        self.conn.close()

    def reset_table(self):
        self.conn.execute("DROP TABLE times")

    def create_table(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS times (
                        username text,
                        start_hour int,
                        start_minute int,
                        end_hour int,
                        end_minute int,
                        duration_hour int,
                        duration_minute int
                        );""")

    def insert_data(self, username: str, start: MyTime, end: MyTime):
        duration = start.time_diff(end)
        self.c.execute(
            "INSERT INTO times VALUES (?, ?, ?, ?, ?, ?, ?)", (
                username,
                start.hour,
                start.minute,
                end.hour,
                end.minute,
                duration.hour,
                duration.minute)
        )
        self.conn.commit()

    def get_times(self):
        # print out whole table
        self.c.execute("SELECT * FROM times")
        print(self.c.fetchall())

    def get_times_from_username(self, username):
        self.c.execute("SELECT * FROM times WHERE username=?", (username,))
        print(self.c.fetchall())

    # create delete data function here
    def delete_data(self, username: str, start_hour: int, start_minute: int,
                    end_hour: int, end_minute: int,
                    duration_hour: int, duration_minute: int):

        self.c.execute("SELECT * FROM times WHERE username = ? AND start_hour = ? "
                       "AND start_minute = ? AND end_hour = ? AND end_minute = ?"
                       "AND duration_hour = ? AND duration_minute = ?", (username,), (start_hour,),
                       (start_minute,), (end_hour,), (end_minute,), (duration_hour,), (duration_minute,))

        # look at later
        self.c.execute("DELETE FROM times WHERE username = ? AND start_hour = ? AND "
                       "start_minute = ? AND end_hour = ? AND end_minute = ? AND "
                       "duration_hour = ? AND duration_minute = ?", (username,), (start_hour,), (start_minute,),
                       (end_hour,), (end_minute,), (duration_hour,),
                       (duration_minute,))

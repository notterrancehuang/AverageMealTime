import sqlite3


class CredentialsDatabase():
    def __init__(self, database_file):
        self.conn = sqlite3.connect(database_file)
        self.c = self.conn.cursor()

    def close(self):
        self.conn.close()

    def create_table(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS credentials (
        username text,
        password text
        );""")

    def insert_data(self, username: str, password: str):
        self.c.execute(
            "INSERT INTO credentials (?, ?)", (username, password)
        )
        self.conn.commit()

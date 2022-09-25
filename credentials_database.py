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
            "INSERT INTO credentials VALUES(?, ?)", (username, password)
        )
        self.conn.commit()

    def get_data(self):
        self.c.execute("SELECT * FROM credentials")
        print(self.c.fetchall())

    @classmethod
    def check_valid_username(cls, input_username: str) -> bool:
        self.c.execute("SELECT rowid FROM credentials WHERE username = ?", (input_username,))
        return self.c.fetchone() is not None

    @classmethod
    def check_valid_password(cls, input_password: str) -> bool:
        self.c.execute("SELECT rowid FROM credentials WHERE password = ?", (input_password,))
        return self.c.fetchone() is not None

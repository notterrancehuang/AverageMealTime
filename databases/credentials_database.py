import sqlite3
import hashlib


class CredentialsDatabase:
    def __init__(self, database_file):
        self.conn = sqlite3.connect(database_file)
        self.c = self.conn.cursor()

    def close(self):
        self.conn.close()

    def reset_table(self):
        self.conn.execute("DROP TABLE credentials")

    def create_table(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS credentials (
        login_hash text
        );""")

    def insert_data(self, username: str, password: str):
        hashed = hashlib.sha256((username + password).encode(
            'utf-8')).hexdigest()
        self.c.execute(
            "INSERT INTO credentials VALUES (?)", (hashed,)
        )
        self.conn.commit()

    def get_data(self):
        self.c.execute("SELECT * FROM credentials")
        print(self.c.fetchall())

    def check_valid_login(self, input_username: str, input_password: str) -> \
            bool:
        hashed = hashlib.sha256((input_username + input_password).encode(
            'utf-8')).hexdigest()
        self.c.execute("SELECT rowid FROM credentials WHERE login_hash = ?",
                       (hashed,))
        return self.c.fetchone() is not None

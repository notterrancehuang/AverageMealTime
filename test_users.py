from credentials_database import CredentialsDatabase

def test():
    username = "James Bond"
    password = "agentdouble007"
    database_file = "users.db"
    db = CredentialsDatabase(database_file)
    db.create_table()
    db.get_data()
    print(db.check_valid_username(username))
    print(db.check_valid_password(password))
    db.close()
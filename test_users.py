from credentials_database import CredentialsDatabase

def test():
    username = "James Bond"
    password = "agentdouble007"
    database_file = "users.db"
    db = CredentialsDatabase(database_file)
    db.create_table()
    db.insert_data(username,password)
    db.get_data()
    db.close()
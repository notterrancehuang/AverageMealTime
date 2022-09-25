from databases.credentials_database import CredentialsDatabase
from login import Login


def test():
    username = "John Smith"
    password = "password"
    database_file = "users.db"
    db = CredentialsDatabase(database_file)
    db.create_table()
    db.get_data()
    # db.insert_data(username, password)
    input_username = input("Username: ")
    input_password = input("Password: ")
    login = Login(input_username, input_password)
    valid = login.check_validity()
    if valid:
        print("Login successful")
    else:
        print("Login failed")
    db.close()

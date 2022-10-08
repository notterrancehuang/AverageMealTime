from databases.credentials_database import CredentialsDatabase


class Login:
    def __init__(self, input_username, input_password):
        self.input_username = input_username
        self.input_password = input_password

    def check_validity(self):
        # should this be here???? 
        credentials_database = CredentialsDatabase("users.db")
        return credentials_database.check_valid_login(
            self.input_username, self.input_password)

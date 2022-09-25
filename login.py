from credentials_database import CredentialsDatabase

class Login:
    def __init__(self, input_username, input_password):
        self.input_username = input_username
        self.input_password = input_password

    def check_validity(self):
        CredentialsDatabase.check_valid_username(self.input_username) and \
        CredentialsDatabase.check_valid_password(self.input_password)

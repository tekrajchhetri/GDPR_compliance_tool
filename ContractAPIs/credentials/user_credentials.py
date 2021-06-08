import os

class UserCredentials:
    def get_username(self):
        return os.environ.get("USERNAME")

    def get_password(self):
        return os.environ.get("PASSWORD")
        
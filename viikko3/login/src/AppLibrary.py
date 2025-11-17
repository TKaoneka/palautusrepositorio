import requests


class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5001"

    def reset_application(self):
        requests.post(f"{self._base_url}/tests/reset")

    def create_user(self, username, password):
        data = {
            "username": username,
            "password": password,
            "password_confirmation": password
        }

        requests.post(f"{self._base_url}/register", data=data)
    
    def create_user_password_twice(self, username, password_1, password_2):
        data = {
            "username": username,
            "password": password_1,
            "password_confirmation": password_2
        }
        if data["password"] == data["password_confirmation"]:
            requests.post(f"{self._base_url}/register", data=data)
        else:
            pass
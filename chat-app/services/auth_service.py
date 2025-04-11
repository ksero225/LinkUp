import requests
from User import User
from config import api_link_login, api_link_register

class AuthService:
    @staticmethod
    def login(username: str, password: str) -> User:
        data = {"userLogin": username, "userPassword": password}
        response = requests.post(api_link_login, json=data, timeout=5)
        if response.status_code == 200:
            user_data = response.json()
            return User(
                user_data["userId"],
                user_data["userLogin"],
                user_data["userEmail"],
                user_data["userFriendList"],
                password
            )
        raise ValueError("Incorrect login or password")

    @staticmethod
    def register(username: str, email: str, password: str, public_key_str: str) -> None:
        data = {
            "userLogin": username,
            "userEmail": email,
            "userPassword": password,
            "userPublicKey": public_key_str
        }
        response = requests.post(api_link_register, json=data, timeout=5)
        if response.status_code != 200:
            raise ValueError("Registration failed")
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
import requests
from User import User
from config import api_link_login
from ErrorHandler import show_error_message

class LoginWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login window")
        self.setFixedSize(300, 150)

        self.user = None

        layout = QVBoxLayout(self)

        # Pole loginu
        self.label_user = QLabel("Login:")
        self.input_user = QLineEdit()
        layout.addWidget(self.label_user)
        layout.addWidget(self.input_user)

        # Pole hasła
        self.label_password = QLabel("Password:")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)

        # Przycisk logowania
        self.btn_login = QPushButton("Log in")
        self.btn_login.clicked.connect(self.handle_login)
        layout.addWidget(self.btn_login)

    def handle_login(self):
        username = self.input_user.text()
        password = self.input_password.text()

        # Jeśli username i password są poprawne, uruchamiamy zapytanie HTTP w osobnym wątku
        if username and password:
            data = {"userLogin": username, "userPassword": password}
            print(data)

            try:
                response = requests.post(api_link_login, json=data)
                print(response.status_code)

                if response.status_code == 200:
                    response_data = response.json()
                    self.user = User(response_data["userId"], response_data["userLogin"], response_data["userEmail"])

                    print(self.user.get_user_login())
                    print(self.user.get_user_email())
                    print(self.user.get_user_id())
                    self.accept()
                elif response.status_code == 401:
                    show_error_message(f"Incorrect login or password")
                else:
                    show_error_message(f"Server connection error")
            except requests.exceptions.RequestException as e:
                show_error_message(f"Error: {e}")




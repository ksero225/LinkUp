from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
import bcrypt
import json
import requests
import threading
from User import User
from config import api_link_login

class LoginWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Logowanie")
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
            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

            threading.Thread(target=self.login_request, args=(username, hashed_password)).start()

    def login_request(self, username, password):
        data = json.dumps({"userLogin": username, "userPassword": password})
        print(data)

        try:
            response = requests.post(api_link_login, json=data)
            print(response.status_code)

            if response.status_code == 200:
                # Obsługuje logikę, np. zamyka okno logowania, jeśli dane są poprawne
                self.accept()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
import bcrypt
import json
import requests
import threading
from config import api_link_register

class RegisterWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Registration")
        self.setFixedSize(300, 300)

        layout = QVBoxLayout(self)

        # Pole loginu
        self.label_user = QLabel("Login:")
        self.input_user = QLineEdit()
        self.input_user.setMinimumHeight(20)
        layout.addWidget(self.label_user)
        layout.addWidget(self.input_user)

        # Pole emaila
        self.label_email = QLabel("Email:")
        self.input_email = QLineEdit()
        self.input_email.setMinimumHeight(20)
        layout.addWidget(self.label_email)
        layout.addWidget(self.input_email)

        # Pole hasła
        self.label_password = QLabel("Password:")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_password.setMinimumHeight(20)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)

        # Pole potwierdzenia hasła
        self.label_confirm_password = QLabel("Confirm password:")
        self.input_confirm_password = QLineEdit()
        self.input_confirm_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_confirm_password.setMinimumHeight(20)
        layout.addWidget(self.label_confirm_password)
        layout.addWidget(self.input_confirm_password)

        # Przycisk rejestracji
        self.btn_register = QPushButton("Sign up")
        self.btn_register.setMinimumHeight(20)
        self.btn_register.clicked.connect(self.handle_register)
        layout.addWidget(self.btn_register)

    def handle_register(self):
        username = self.input_user.text()
        email = self.input_email.text()
        password = self.input_password.text()
        confirm_password = self.input_confirm_password.text()

        if not username or not email or not password or not confirm_password:
            print("All fields are required!")
            return

        if password != confirm_password:
            print("Passwords are not identical!")
            return

        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        threading.Thread(target=self.register_request, args=(username, email, hashed_password)).start()

    def register_request(self, username, email, hashed_password):
        data = json.dumps({"userLogin": username, "userEmail": email, "userPassword": hashed_password})
        print(data)

        try:
            response = requests.post(api_link_register, json=data)
            print(response.status_code)

            if response.status_code == 200:
                print("Registration completed successfully!")
                self.accept()
            else:
                print("Registration error!")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

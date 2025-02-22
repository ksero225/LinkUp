from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
import requests
from config import api_link_register
from ErrorHandler import show_error_message

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
        is_user_active = False

        if not username or not email or not password or not confirm_password:
            show_error_message("All fields are required!")
            return

        if len(password) < 8:
            show_error_message("The password must be at least 8 characters long!")
            return

        if password != confirm_password:
            show_error_message("Passwords are not identical!")
            return

        data = {"userLogin": username, "userEmail": email, "userPassword": password, "isUserActive": is_user_active}
        print(data)

        try:
            response = requests.post(api_link_register, json=data)
            print(response.status_code)
            print(response)
            if response.status_code == 200:
                self.accept()
            else:
                show_error_message("Registration error!")
        except requests.exceptions.RequestException as e:
            show_error_message(f"Error: {e}")


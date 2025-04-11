from dialogs.base_auth_dialog import BaseAuthDialog
from PySide6.QtWidgets import QPushButton
from services.auth_service import AuthService
from ErrorHandler import show_error_message
from User import User
import base64

class RegisterWindow(BaseAuthDialog):
    def __init__(self, parent=None):
        super().__init__("Register", height=300, parent=parent)
        self.create_input_field("Login:", "username")
        self.create_input_field("Email:", "email")
        self.create_input_field("Password:", "password", is_password=True)
        self.create_input_field("Confirm Password:", "confirm", is_password=True)

        register_btn = QPushButton("Sign up")
        register_btn.clicked.connect(self.handle_register)
        self.layout.addWidget(register_btn)

    def handle_register(self):
        username = self.get_value("username")
        email = self.get_value("email")
        password = self.get_value("password")
        confirm = self.get_value("confirm")

        if not all([username, email, password, confirm]):
            show_error_message("All fields are required.")
            return

        if password != confirm:
            show_error_message("Passwords do not match.")
            return

        if len(password) < 8:
            show_error_message("Password must be at least 8 characters long.")
            return

        user = User(None, username, email, None, password)
        public_key_str = base64.b64encode(user.get_public_key_pem()).decode()

        try:
            AuthService.register(username, email, password, public_key_str)
            self.accept()
        except Exception as e:
            show_error_message(str(e))
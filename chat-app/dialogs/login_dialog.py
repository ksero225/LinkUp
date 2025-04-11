from dialogs.base_auth_dialog import BaseAuthDialog
from PySide6.QtWidgets import QPushButton
from services.auth_service import AuthService
from ErrorHandler import show_error_message

class LoginWindow(BaseAuthDialog):
    def __init__(self, parent=None):
        super().__init__("Login", height=150, parent=parent)
        self.user = None
        self.create_input_field("Login:", "username")
        self.create_input_field("Password:", "password", is_password=True)

        login_btn = QPushButton("Log in")
        login_btn.clicked.connect(self.handle_login)
        self.layout.addWidget(login_btn)

    def handle_login(self):
        username = self.get_value("username")
        password = self.get_value("password")

        if not username or not password:
            show_error_message("All fields are required.")
            return

        try:
            self.user = AuthService.login(username, password)
            self.accept()
        except Exception as e:
            show_error_message(str(e))
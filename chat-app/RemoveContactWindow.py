from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
import requests
from config import contact_link
from ErrorHandler import show_error_message
from User import User

class RemoveContactWindow(QDialog):
    def __init__(self, parent=None, user: User=None):
        super().__init__(parent)
        self.setWindowTitle("Remove Contact")
        self.setFixedSize(300, 150)

        layout = QVBoxLayout(self)

        self.user_login = user.get_user_login()
        self.removed_contact = None

        # Pole login kontaktu
        self.label_contact_login = QLabel("Contact name:")
        self.input_contact_login = QLineEdit()
        self.input_contact_login.setMinimumHeight(20)
        layout.addWidget(self.label_contact_login)
        layout.addWidget(self.input_contact_login)

        # Przycisk usuwania kontaktu
        self.btn_remove_contact = QPushButton("Remove Contact")
        self.btn_remove_contact.setMinimumHeight(20)
        self.btn_remove_contact.clicked.connect(self.handle_remove_contact)
        layout.addWidget(self.btn_remove_contact)

    def handle_remove_contact(self):
        contact_login = self.input_contact_login.text()

        if not contact_login:
            show_error_message("Contact name cannot be empty!")
            return

        api_link_remove_contact = contact_link(self.user_login, contact_login, 'DELETE')

        try:
            response = requests.patch(api_link_remove_contact, timeout=5)
            print(response.status_code)
            print(response.text)
            if response.status_code == 200:
                self.removed_contact = contact_login
                self.accept()
            else:
                show_error_message("Error removing contact!")
        except requests.exceptions.Timeout:
            show_error_message(f"Request timed out. Please try again later.")
        except requests.exceptions.RequestException as e:
            show_error_message(f"Error: {e}")
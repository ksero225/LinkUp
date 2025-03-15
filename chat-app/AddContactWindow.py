from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
import requests
from config import get_new_contact_link
from ErrorHandler import show_error_message

class AddContactWindow(QDialog):
    def __init__(self, parent=None, user_id=None):
        super().__init__(parent)
        self.setWindowTitle("Add Contact")
        self.setFixedSize(300, 150)

        layout = QVBoxLayout(self)

        self.user_id = user_id

        # Pole ID kontaktu
        self.label_contact_id = QLabel("Contact ID:")
        self.input_contact_id = QLineEdit()
        self.input_contact_id.setMinimumHeight(20)
        layout.addWidget(self.label_contact_id)
        layout.addWidget(self.input_contact_id)

        # Przycisk dodawania kontaktu
        self.btn_add_contact = QPushButton("Add Contact")
        self.btn_add_contact.setMinimumHeight(20)
        self.btn_add_contact.clicked.connect(self.handle_add_contact)
        layout.addWidget(self.btn_add_contact)

    def handle_add_contact(self):
        contact_id = self.input_contact_id.text()

        if not contact_id:
            show_error_message("Contact ID cannot be empty!")
            return

        api_link_add_contact = get_new_contact_link(self.user_id, contact_id)

        try:
            response = requests.patch(api_link_add_contact, timeout=5)
            print(response.status_code)
            print(response.text)
            if response.status_code == 200:
                self.accept()
            else:
                show_error_message("Error adding new contact!")
        except requests.exceptions.Timeout:
            show_error_message(f"Request timed out. Please try again later.")
        except requests.exceptions.RequestException as e:
            show_error_message(f"Error: {e}")
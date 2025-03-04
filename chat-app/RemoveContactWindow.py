from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
import requests
from config import get_remove_contact_link
from ErrorHandler import show_error_message

class RemoveContactWindow(QDialog):
    def __init__(self, parent=None, user_id=None):
        super().__init__(parent)
        self.setWindowTitle("Remove Contact")
        self.setFixedSize(300, 150)

        layout = QVBoxLayout(self)

        self.user_id = user_id

        # Pole ID kontaktu
        self.label_contact_id = QLabel("Contact ID:")
        self.input_contact_id = QLineEdit()
        self.input_contact_id.setMinimumHeight(20)
        layout.addWidget(self.label_contact_id)
        layout.addWidget(self.input_contact_id)

        # Przycisk usuwania kontaktu
        self.btn_remove_contact = QPushButton("Remove Contact")
        self.btn_remove_contact.setMinimumHeight(20)
        self.btn_remove_contact.clicked.connect(self.handle_remove_contact)
        layout.addWidget(self.btn_remove_contact)

    def handle_remove_contact(self):
        contact_id = self.input_contact_id.text()

        if not contact_id:
            show_error_message("Contact ID cannot be empty!")
            return

        api_link_remove_contact = get_remove_contact_link(self.user_id, contact_id)

        try:
            response = requests.patch(api_link_remove_contact)
            print(response.status_code)
            print(response.text)
            if response.status_code == 200:
                self.accept()
            else:
                show_error_message("Error removing contact!")
        except requests.exceptions.RequestException as e:
            show_error_message(f"Error: {e}")
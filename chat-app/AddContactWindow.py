from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
import requests
from config import get_new_contact_link
from ErrorHandler import show_error_message
from User import User

class AddContactWindow(QDialog):
    def __init__(self, parent=None, user: User = None):
        super().__init__(parent)
        self.setWindowTitle("Add Contact")
        self.setFixedSize(300, 150)

        self.new_contact = None

        layout = QVBoxLayout(self)

        self.user_id = user.get_user_id()
        self.user_contacts = user.get_user_contacts()

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

            if response.status_code == 200:
                new_contact_data = response.json()
                print(new_contact_data)

                if isinstance(new_contact_data, list) and new_contact_data:
                    new_contact_data = new_contact_data[-1]
                self.new_contact = new_contact_data  # Zapisujemy nowy kontakt
                self.user_contacts.append(new_contact_data)
                self.accept()
            else:
                show_error_message("Error adding new contact!")
        except requests.exceptions.Timeout:
            show_error_message(f"Request timed out. Please try again later.")
        except requests.exceptions.RequestException as e:
            show_error_message(f"Error: {e}")
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
import requests
from config import contact_link
from ErrorHandler import show_error_message
from User import User

class AddContactWindow(QDialog):
    def __init__(self, parent=None, user: User = None):
        super().__init__(parent)
        self.setWindowTitle("Add Contact")
        self.setFixedSize(300, 150)

        self.new_contact = None

        layout = QVBoxLayout(self)

        self.user_login = user.get_user_login()
        self.user_contacts = user.get_user_contacts()

        # Pole login kontaktu
        self.label_contact_login = QLabel("Contact name:")
        self.input_contact_login = QLineEdit()
        self.input_contact_login.setMinimumHeight(20)
        layout.addWidget(self.label_contact_login)
        layout.addWidget(self.input_contact_login)

        # Przycisk dodawania kontaktu
        self.btn_add_contact = QPushButton("Add Contact")
        self.btn_add_contact.setMinimumHeight(20)
        self.btn_add_contact.clicked.connect(self.handle_add_contact)
        layout.addWidget(self.btn_add_contact)

    def handle_add_contact(self):
        contact_login = self.input_contact_login.text()

        if not contact_login:
            show_error_message("Contact name cannot be empty!")
            return

        api_link_add_contact = contact_link(self.user_login, contact_login, 'ADD')
        print(api_link_add_contact)

        try:
            response = requests.patch(api_link_add_contact, timeout=5)
            print(response.status_code)

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
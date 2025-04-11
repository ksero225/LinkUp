from windows.contact.base_contact_window import BaseContactWindow
from services.contact_service import ContactService
from ErrorHandler import show_error_message

class AddContactWindow(BaseContactWindow):
    def __init__(self, parent=None, user=None):
        super().__init__("Add Contact", "Add Contact", parent)
        self.user = user
        self.button.clicked.connect(self.handle_add_contact)

    def handle_add_contact(self):
        contact_login = self.input_contact.text()

        if not contact_login:
            show_error_message("Contact name cannot be empty!")
            return

        success, new_contact_data, error = ContactService.add_contact(self.user, contact_login)

        if success:
            self.result_contact = new_contact_data
            self.user.get_user_contacts().append(new_contact_data)
            self.accept()
        else:
            show_error_message(error)

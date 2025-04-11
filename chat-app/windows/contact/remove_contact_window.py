from windows.contact.base_contact_window import BaseContactWindow
from services.contact_service import ContactService
from ErrorHandler import show_error_message

class RemoveContactWindow(BaseContactWindow):
    def __init__(self, parent=None, user=None):
        super().__init__("Remove Contact", "Remove Contact", parent)
        self.user = user
        self.button.clicked.connect(self.handle_remove_contact)

    def handle_remove_contact(self):
        contact_login = self.input_contact.text()

        if not contact_login:
            show_error_message("Contact name cannot be empty!")
            return

        success, _, error = ContactService.remove_contact(self.user, contact_login)

        if success:
            self.result_contact = contact_login
            self.accept()
        else:
            show_error_message(error)

import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from ui_form import Ui_MainWindow
from LoginWindow import LoginWindow
from RegisterWindow import RegisterWindow
from AddContactWindow import AddContactWindow
from RemoveContactWindow import RemoveContactWindow
from User import User

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.user = None

        self.ui.actionAdd_new_contact.setEnabled(False)
        self.ui.actionDelete_contact.setEnabled(False)

        self.set_status_label()

        self.ui.lineEdit.setText("Log in before start typing")
        self.ui.lineEdit.setReadOnly(True)

        # Połączenie akcji w menu z oknem logowania
        self.ui.actionSign_in.triggered.connect(self.show_login_window)
        self.ui.actionSign_up.triggered.connect(self.show_register_window)
        self.ui.actionAdd_new_contact.triggered.connect(self.show_add_contact_window)
        self.ui.actionDelete_contact.triggered.connect(self.show_remove_contact_window)

    def show_login_window(self):
        """Otwiera okno logowania i dodaje użytkownika do listy"""
        login_window = LoginWindow(self)
        if login_window.exec():  # Jeśli użytkownik się zalogował (dialog zwróci 1)
            self.user = login_window.user
            if self.user:
                self.add_contacts_to_widget()  # Dodaj do listy
                self.ui.actionSign_in.setEnabled(False)
                self.ui.lineEdit.setText("")
                self.ui.lineEdit.setReadOnly(False)
                self.set_status_label()
                self.ui.actionAdd_new_contact.setEnabled(True)
                self.ui.actionDelete_contact.setEnabled(True)

    def show_register_window(self):
        """Otwiera okno rejestracji"""
        register_window = RegisterWindow(self)
        if register_window.exec():  # Jeśli użytkownik się zarejestrował (dialog zwróci 1)
            pass

    def show_add_contact_window(self):
        """Otwiera okno dodawania kontaktu"""
        new_contact_window = AddContactWindow(self, user_id=self.user.get_user_id())
        if new_contact_window.exec():  # Jeśli użytkownik dodał poprawnie kontakt (dialog zwróci 1)
            pass

    def show_remove_contact_window(self):
        """Otwiera okno usuwania kontaktu"""
        remove_contact_window = RemoveContactWindow(self, user_id=self.user.get_user_id())
        if remove_contact_window.exec():  # Jeśli użytkownik dodał poprawnie kontakt (dialog zwróci 1)
            pass

    def set_status_label(self):
        if self.user:
            self.ui.label_2.setText(f'Status: <span style="color: green;">online({self.user.get_user_login()})</span>')
        else:
            self.ui.label_2.setText('Status: <span style="color: red;">offline</span>')

    def add_contacts_to_widget(self):
        for contact in self.user.get_user_contacts():
            self.ui.listWidget.addItem(contact)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

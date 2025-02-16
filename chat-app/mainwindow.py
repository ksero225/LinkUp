import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from ui_form import Ui_MainWindow
from LoginWindow import LoginWindow
from RegisterWindow import RegisterWindow
from User import User

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.user = None

        self.ui.lineEdit.setText("Log in before start typing")
        self.ui.lineEdit.setReadOnly(True)

        # Połączenie akcji w menu z oknem logowania
        self.ui.actionSign_in.triggered.connect(self.show_login_window)
        self.ui.actionSign_up.triggered.connect(self.show_register_window)

    def show_login_window(self):
        """Otwiera okno logowania i dodaje użytkownika do listy"""
        login_window = LoginWindow(self)
        if login_window.exec():  # Jeśli użytkownik się zalogował (dialog zwróci 1)
            self.user = login_window.user
            if self.user:
                self.ui.listWidget.addItem(self.user.get_user_login())  # Dodaj do listy
                self.ui.actionSign_in.setEnabled(False)
                self.ui.lineEdit.setText("")
                self.ui.lineEdit.setReadOnly(False)

    def show_register_window(self):
        """Otwiera okno rejestracji"""
        register_window = RegisterWindow(self)
        if register_window.exec():  # Jeśli użytkownik się zarejestrował (dialog zwróci 1)
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

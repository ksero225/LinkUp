from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
import bcrypt
import json

class LoginWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Logowanie")
        self.setFixedSize(300, 150)

        self.username = None

        layout = QVBoxLayout(self)

        # Pole loginu
        self.label_user = QLabel("Login:")
        self.input_user = QLineEdit()
        layout.addWidget(self.label_user)
        layout.addWidget(self.input_user)

        # Pole hasła
        self.label_password = QLabel("Password:")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)

        # Przycisk logowania
        self.btn_login = QPushButton("Log in")
        self.btn_login.clicked.connect(self.handle_login)
        layout.addWidget(self.btn_login)

    def handle_login(self):
        username = self.input_user.text()
        password = self.input_password.text()

        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        data = json.dumps({"username": username, "password": hashed_password})
        print(data)

        if username and password:  # Prosta walidacja
            self.username = username  # Zapisujemy nazwę użytkownika
            self.accept()  # Zamykamy okno logowania

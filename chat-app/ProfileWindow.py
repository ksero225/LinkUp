from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication
from PySide6.QtCore import Qt
from User import User

class ProfileWindow(QWidget):
    def __init__(self, user: User):
        super().__init__()
        self._userId = user.get_user_id()
        self._userLogin = user.get_user_login()
        self._userEmail = user.get_user_email()

        self.setWindowTitle("Profile")
        self.setMinimumSize(300, 150)

        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout()

        label_id = QLabel(f"ID: {self._userId}")
        label_login = QLabel(f"Login: {self._userLogin}")
        label_email = QLabel(f"Email: {self._userEmail}")

        for label in (label_id, label_login, label_email):
            label.setAlignment(Qt.AlignCenter)
            layout.addWidget(label)

        self.setLayout(layout)

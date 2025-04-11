from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

class BaseContactWindow(QDialog):
    def __init__(self, title: str, button_text: str, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setFixedSize(300, 150)
        self.result_contact = None

        layout = QVBoxLayout(self)

        self.label_contact = QLabel("Contact name:")
        self.input_contact = QLineEdit()
        self.input_contact.setMinimumHeight(20)

        layout.addWidget(self.label_contact)
        layout.addWidget(self.input_contact)

        self.button = QPushButton(button_text)
        self.button.setMinimumHeight(20)
        layout.addWidget(self.button)

from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit

class BaseAuthDialog(QDialog):
    def __init__(self, title: str, width=300, height=200, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setFixedSize(width, height)
        self.layout = QVBoxLayout(self)
        self.fields = {}

    def create_input_field(self, label_text: str, name: str, is_password=False):
        label = QLabel(label_text)
        input_field = QLineEdit()

        if is_password:
            input_field.setEchoMode(QLineEdit.EchoMode.Password)

        self.layout.addWidget(label)
        self.layout.addWidget(input_field)
        self.fields[name] = input_field

        return input_field

    def get_value(self, name: str) -> str:
        return self.fields[name].text().strip()

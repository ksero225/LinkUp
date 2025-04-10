from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        self.setFixedSize(300, 120)

        layout = QVBoxLayout()

        label = QLabel("LinkUp")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 16px; font-weight: bold;")

        link = QLabel('<a href="https://linkup-rf0o.onrender.com">Visit our website</a>')
        link.setOpenExternalLinks(True)
        link.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)
        layout.addWidget(link)
        self.setLayout(layout)

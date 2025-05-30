import sys
import json

import requests
from PySide6 import QtCore

from PySide6.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon
from PySide6.QtGui import QIcon, QTextCursor
from PySide6.QtCore import Qt

from ui_form import Ui_MainWindow
from dialogs.login_dialog import LoginWindow
from dialogs.register_dialog import RegisterWindow
from windows.contact.add_contact_window import AddContactWindow
from windows.contact.remove_contact_window import RemoveContactWindow
from WebSocketClient import WebSocketStompClient
from config import api_link_websocket, resource_path, chat_history_link
from AboutWindow import AboutWindow
from ProfileWindow import ProfileWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(resource_path('assets/icon_eXh_icon.ico')))
        self.tray_icon.setVisible(True)

        self.user = None
        self.selected_contact = None
        self.websocket_client = None

        self.current_page = 0
        self.loading = False
        self.last_loaded_contact = None

        self.setup_ui()
        self.connect_actions()

    def setup_ui(self):
        self.ui.actionAdd_new_contact.setEnabled(False)
        self.ui.actionDelete_contact.setEnabled(False)
        self.ui.actionLog_out.setEnabled(False)
        self.ui.actionMy_profile.setEnabled(False)
        self.ui.actionSign_up.setEnabled(True)

        self.ui.lineEdit.setText("Log in before start typing")
        self.ui.lineEdit.setReadOnly(True)

        self.set_status_label()

    def connect_actions(self):
        self.ui.lineEdit.returnPressed.connect(self.send_message)
        self.ui.actionSign_in.triggered.connect(self.show_login_window)
        self.ui.actionSign_up.triggered.connect(self.show_register_window)
        self.ui.actionAdd_new_contact.triggered.connect(self.show_add_contact_window)
        self.ui.actionDelete_contact.triggered.connect(self.show_remove_contact_window)
        self.ui.listWidget.currentItemChanged.connect(self.on_contact_changed)
        self.ui.actionAbout.triggered.connect(self.show_about_window)
        self.ui.actionLog_out.triggered.connect(self.logout)
        self.ui.textEdit.verticalScrollBar().valueChanged.connect(self.handle_scroll)
        self.ui.actionMy_profile.triggered.connect(self.show_profile_window)

    def show_login_window(self):
        login_window = LoginWindow(self)
        if login_window.exec():
            self.user = login_window.user
            if self.user:
                self.prepare_logged_in_state()

    def prepare_logged_in_state(self):
        self.ui.listWidget.clear()
        self.add_contacts_to_widget()
        self.set_status_label()
        self.ui.lineEdit.setText("")
        self.ui.lineEdit.setReadOnly(False)

        self.ui.actionSign_in.setEnabled(False)
        self.ui.actionSign_up.setEnabled(False)
        self.ui.actionAdd_new_contact.setEnabled(True)
        self.ui.actionDelete_contact.setEnabled(True)
        self.ui.actionLog_out.setEnabled(True)
        self.ui.actionMy_profile.setEnabled(True)

        self.websocket_client = WebSocketStompClient(api_link_websocket, self.user.get_user_login())
        self.websocket_client.received_message.connect(self.receive_message)
        self.websocket_client.start()

    def show_register_window(self):
        RegisterWindow(self).exec()

    def show_profile_window(self):
        self.profile_window = ProfileWindow(self.user)
        self.profile_window.show()

    def show_add_contact_window(self):
        add_window = AddContactWindow(self, user=self.user)
        if add_window.exec():
            new_contact = add_window.result_contact
            if new_contact:
                self.ui.listWidget.addItem(new_contact['contactLogin'])

    def show_remove_contact_window(self):
        remove_window = RemoveContactWindow(self, user=self.user)
        if remove_window.exec():
            removed_contact = remove_window.result_contact
            if removed_contact:
                items = self.ui.listWidget.findItems(removed_contact, Qt.MatchFlag.MatchExactly)
                for item in items:
                    self.ui.listWidget.takeItem(self.ui.listWidget.row(item))

    def set_status_label(self):
        if self.user:
            self.ui.label_2.setText(f'Status: <span style="color: green;">online({self.user.get_user_login()})</span>')
        else:
            self.ui.label_2.setText('Status: <span style="color: red;">offline</span>')

    def add_contacts_to_widget(self):
        for contact in self.user.get_user_contacts():
            self.ui.listWidget.addItem(contact['contactLogin'])

    def send_message(self):
        if not self.user:
            return

        recipient_item = self.ui.listWidget.currentItem()
        if not recipient_item:
            self.ui.textEdit.append('<p style="color: red;">Select a contact before sending a message!</p>')
            return

        recipient = recipient_item.text()
        message_text = self.ui.lineEdit.text().strip()
        self.ui.lineEdit.clear()

        if not message_text:
            return

        recipient_key = self.user.get_contact_public_key(recipient)
        if not recipient_key:
            self.ui.textEdit.append('<p style="color: red;">Recipient public key missing!</p>')
            return

        encrypted = self.user.encrypt_message(message_text, recipient_key)
        print(encrypted)
        self.websocket_client.send_message(recipient, encrypted)

        self.ui.textEdit.append(f'<p style="color: blue;"><b>Me:</b> {message_text}</p>')

    def receive_message(self, message):
        try:
            message = message.rstrip('\x00').strip()
            parts = message.split('\n\n', 1)
            json_part = parts[1].strip() if len(parts) > 1 else message

            message_data = json.loads(json_part)
            sender = message_data.get('sender')
            encrypted_message = message_data.get('encryptedMessage')
            iv = message_data.get('iv')
            key_for_recipient = message_data.get('keyForRecipient')
            key_for_sender = message_data.get('keyForSender')

            encrypted_data = {
                "encryptedMessage": encrypted_message,
                "iv": iv,
                "keyForRecipient": key_for_recipient,
                "keyForSender": key_for_sender
            }

            decrypted = self.user.decrypt_message(encrypted_data)
            display = f'<p style="color: green;"><b>{sender}:</b> {decrypted}</p>'

            if self.selected_contact == sender:
                self.ui.textEdit.append(display)

            if self.tray_icon.isVisible():
                self.tray_icon.showMessage(
                    f"New message from {sender}",
                    decrypted,
                    QSystemTrayIcon.Information,
                    3000
                )

        except json.JSONDecodeError:
            self.ui.textEdit.append('<p style="color: red;">Invalid message received!</p>')
        except Exception as e:
            self.ui.textEdit.append(f'<p style="color: red;">Decryption error: {str(e)}</p>')

    def logout(self):
        try:
            if self.websocket_client:
                self.websocket_client.stop_client()
        except Exception as e:
            print(f"Error on logout: {e}")

        self.user = None
        self.websocket_client = None
        self.selected_contact = None

        self.ui.lineEdit.setText("Log in before start typing")
        self.ui.lineEdit.setReadOnly(True)
        self.ui.listWidget.clear()
        self.ui.textEdit.clear()

        self.ui.actionAdd_new_contact.setEnabled(False)
        self.ui.actionDelete_contact.setEnabled(False)
        self.ui.actionSign_in.setEnabled(True)
        self.ui.actionSign_up.setEnabled(True)
        self.ui.actionLog_out.setEnabled(False)
        self.ui.actionMy_profile.setEnabled(False)

        self.set_status_label()

    def closeEvent(self, event):
        self.logout()
        event.accept()

    def on_contact_changed(self, current, _):
        self.ui.textEdit.clear()
        self.current_page = 0
        self.last_loaded_contact = None

        if not current or not self.user:
            return

        self.selected_contact = current.text()
        self.load_conversation(self.user.get_user_login(), self.selected_contact, 0)

    def load_conversation(self, sender, recipient, page=0):
        # Zabezpieczenie przed ładowaniem nieaktualnego czatu
        current_requested_contact = recipient

        if self.last_loaded_contact != recipient and page > 0:
            return

        self.loading = True
        url = chat_history_link(sender, recipient, page)

        scrollbar = self.ui.textEdit.verticalScrollBar()
        old_value = scrollbar.value()
        old_max = scrollbar.maximum()

        try:
            response = requests.get(url)
            response.raise_for_status()
            messages = response.json().get("content", [])

            if not messages:
                if page == 0:
                    self.ui.textEdit.append('<p style="color: gray;">No messages found.</p>')
                self.loading = False
                return

            if page > 0:
                cursor = self.ui.textEdit.textCursor()
                cursor.movePosition(QTextCursor.Start)

                for msg in reversed(messages):
                    # Zabezpieczenie przed zmianą kontaktu
                    if self.selected_contact != current_requested_contact:
                        return

                    try:
                        decrypted = self.user.decrypt_message(msg)
                        is_me = msg.get("sender") == sender
                        html = f'<p style="color: {"blue" if is_me else "green"};"><b>{"Me" if is_me else msg.get("sender")}:</b> {decrypted}</p>'
                        cursor.insertHtml(html)
                        cursor.insertBlock()
                    except Exception:
                        cursor.insertHtml('<p style="color: red;">[Error decrypting message]</p>')
                        cursor.insertBlock()

                QtCore.QTimer.singleShot(0, lambda: scrollbar.setValue(scrollbar.maximum() - (old_max - old_value)))

            else:
                self.ui.textEdit.clear()
                for msg in reversed(messages):
                    if self.selected_contact != current_requested_contact:
                        return

                    try:
                        decrypted = self.user.decrypt_message(msg)
                        is_me = msg.get("sender") == sender
                        self.ui.textEdit.append(
                            f'<p style="color: {"blue" if is_me else "green"};"><b>{"Me" if is_me else msg.get("sender")}:</b> {decrypted}</p>'
                        )
                    except Exception:
                        self.ui.textEdit.append('<p style="color: red;">[Error decrypting message]</p>')

        except requests.RequestException as e:
            self.ui.textEdit.append(f'<p style="color: red;">Error fetching messages: {str(e)}</p>')

        self.loading = False
        self.last_loaded_contact = recipient

    def show_about_window(self):
        self.about_window = AboutWindow()
        self.about_window.show()

    def handle_scroll(self, value):
        if value == 0 and not self.loading and self.selected_contact:
            self.current_page += 1
            self.load_conversation(self.user.get_user_login(), self.selected_contact, self.current_page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("LinkUp Messenger")
    app.setApplicationDisplayName("LinkUp")
    app.setWindowIcon(QIcon(resource_path('assets/icon_eXh_icon.ico')))

    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
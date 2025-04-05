from crypto_utils import CryptoUtils
import os
from base64 import b64decode

class User:
    def __init__(self, userId, userLogin, userEmail, userFriendList, userPassword):
        self._userId = userId
        self._userLogin = userLogin
        self._userEmail = userEmail
        self._isUserActive = True
        self._userContacts = userFriendList
        self._userPassword = userPassword
        self._private_key = None
        self._public_key = None

        if os.path.exists(f"{self._userLogin}_private_key.pem"):
            self.load_private_key()
        else:
            self.generate_keys()
            self.save_private_key()

    def generate_keys(self):
        self._private_key, self._public_key = CryptoUtils.generate_rsa_keypair()

    def save_private_key(self):
        with open(f"{self._userLogin}_private_key.pem", "wb") as f:
            f.write(CryptoUtils.serialize_private_key(self._private_key, self._userPassword))

    def load_private_key(self):
        with open(f"{self._userLogin}_private_key.pem", "rb") as f:
            self._private_key = CryptoUtils.load_private_key_from_pem(f.read(), self._userPassword)
        self._public_key = self._private_key.public_key()

    def get_public_key_pem(self):
        return CryptoUtils.serialize_public_key(self._public_key)

    def get_contact_public_key(self, recipient):
        for contact in self._userContacts:
            if contact['contactLogin'] == recipient:
                return CryptoUtils.load_public_key_from_pem(b64decode(contact['userPublicKey']))

    def encrypt_message(self, message, recipient_public_key):
        return CryptoUtils.encrypt_message(message, recipient_public_key, self._public_key)

    def decrypt_message(self, encrypted_data):
        return CryptoUtils.decrypt_message(encrypted_data, self._private_key)

    def get_user_id(self):
        return self._userId

    def get_user_login(self):
        return self._userLogin

    def get_user_email(self):
        return self._userEmail

    def get_is_user_active(self):
        return self._isUserActive

    def get_user_contacts(self):
        return self._userContacts

    def set_user_id(self, user_id):
        self._userId = user_id

    def set_user_login(self, user_login):
        self._userLogin = user_login

    def set_user_email(self, user_email):
        self._userEmail = user_email

    def set_is_user_active(self, is_user_active):
        self._isUserActive = is_user_active

    def set_user_contacts(self, user_contacts):
        self._userContacts = user_contacts
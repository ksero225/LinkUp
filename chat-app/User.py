import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import base64

class User:
    def __init__(self, userId: str, userLogin: str, userEmail: str, userFriendList: list, userPassword: str):
        self._userId = userId
        self._userLogin = userLogin
        self._userEmail = userEmail
        self._isUserActive = True
        self._userContacts = userFriendList
        self._userPassword = userPassword
        self._private_key = None
        self._public_key = None

        # Sprawdzenie, czy klucz prywatny już istnieje
        if os.path.exists(f"{self._userLogin}_private_key.pem"):
            self.load_private_key()
        else:
            self.generate_keys()
            self.save_private_key()

    def generate_keys(self):
        """Generuje nową parę kluczy RSA"""
        self._private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self._public_key = self._private_key.public_key()

    def save_private_key(self):
        """Zapisuje klucz prywatny do pliku (zaszyfrowany hasłem)"""
        with open(f"{self._userLogin}_private_key.pem", "wb") as f:
            f.write(self._private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.BestAvailableEncryption(self._userPassword.encode())
            ))

    def load_private_key(self):
        """Wczytuje klucz prywatny z pliku"""
        with open(f"{self._userLogin}_private_key.pem", "rb") as f:
            self._private_key = serialization.load_pem_private_key(
                f.read(),
                password=self._userPassword.encode()
            )
        self._public_key = self._private_key.public_key()

    def get_public_key_pem(self):
        """Zwraca klucz publiczny w formacie PEM (gotowy do wysłania do API)"""
        return self._public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    def decrypt_aes_key(self, encrypted_key):
        """Odszyfrowuje klucz AES za pomocą klucza prywatnego"""
        return self._private_key.decrypt(
            encrypted_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    def get_contact_public_key(self, recipient):
        for contact in self._userContacts:
            if contact['contactLogin'] == recipient:
                public_key_bytes = base64.b64decode(contact['userPublicKey'])
                return serialization.load_pem_public_key(public_key_bytes)

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

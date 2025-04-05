import os
import json
from base64 import b64encode, b64decode
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class CryptoUtils:
    """Klasa odpowiedzialna za szyfrowanie i odszyfrowywanie wiadomości."""
    @staticmethod
    def generate_rsa_keypair():
        """Generuje nową parę kluczy RSA."""
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def serialize_private_key(private_key, password):
        """Zapisuje klucz prywatny do formatu PEM (zaszyfrowany hasłem)."""
        return private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(password.encode())
        )

    @staticmethod
    def load_private_key_from_pem(pem_data, password):
        """Wczytuje klucz prywatny z PEM."""
        return serialization.load_pem_private_key(
            pem_data,
            password=password.encode()
        )

    @staticmethod
    def serialize_public_key(public_key):
        """Zwraca klucz publiczny w formacie PEM."""
        return public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    @staticmethod
    def load_public_key_from_pem(public_key_pem):
        """Ładuje klucz publiczny z PEM."""
        return serialization.load_pem_public_key(public_key_pem)

    @staticmethod
    def encrypt_aes_key(aes_key, public_key):
        """Szyfruje klucz AES kluczem publicznym RSA."""
        return public_key.encrypt(
            aes_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    @staticmethod
    def decrypt_aes_key(encrypted_key, private_key):
        """Odszyfrowuje klucz AES kluczem prywatnym RSA."""
        return private_key.decrypt(
            encrypted_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    @staticmethod
    def encrypt_message(message, recipient_public_key, sender_public_key):
        """Szyfruje wiadomość AES + RSA (Hybrid Encryption)."""
        aes_key = os.urandom(32)  # Losowy klucz AES (256-bit)
        iv = os.urandom(16)  # Wektor inicjalizacyjny

        # Szyfrowanie wiadomości AES
        cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        padded_message = message + ' ' * (16 - len(message) % 16)  # Padding do 16 bajtów
        encrypted_message = encryptor.update(padded_message.encode()) + encryptor.finalize()

        # Szyfrujemy klucz AES dwoma kluczami publicznymi
        encrypted_key_for_recipient = CryptoUtils.encrypt_aes_key(aes_key, recipient_public_key)
        encrypted_key_for_sender = CryptoUtils.encrypt_aes_key(aes_key, sender_public_key)

        return {
            "encrypted_message": b64encode(encrypted_message).decode(),
            "iv": b64encode(iv).decode(),
            "key_for_recipient": b64encode(encrypted_key_for_recipient).decode(),
            "key_for_sender": b64encode(encrypted_key_for_sender).decode()
        }

    @staticmethod
    def decrypt_message(encrypted_data, private_key):
        """Odszyfrowuje wiadomość AES."""
        encrypted_message = b64decode(encrypted_data["encrypted_message"])
        iv = b64decode(encrypted_data["iv"])

        # Próbujemy odszyfrować klucz AES (dla nadawcy lub odbiorcy)
        try:
            aes_key = CryptoUtils.decrypt_aes_key(b64decode(encrypted_data["key_for_recipient"]), private_key)
        except:
            aes_key = CryptoUtils.decrypt_aes_key(b64decode(encrypted_data["key_for_sender"]), private_key)

        # Odszyfrowanie wiadomości AES
        cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        decrypted_padded_message = decryptor.update(encrypted_message) + decryptor.finalize()

        return decrypted_padded_message.rstrip().decode()

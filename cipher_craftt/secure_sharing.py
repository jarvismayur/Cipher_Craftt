from cryptography.fernet import Fernet
import base64
import os

def generate_key():
    """
    Generate a secure encryption key.
    :return: Encryption key.
    """
    return base64.urlsafe_b64encode(os.urandom(32))

def encrypt_password(password, key):
    """
    Encrypt the given password using the provided key.
    :param password: Password to encrypt.
    :param key: Encryption key.
    :return: Encrypted password.
    """
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password.decode()

def decrypt_password(encrypted_password, key):
    """
    Decrypt the given password using the provided key.
    :param encrypted_password: Encrypted password to decrypt.
    :param key: Encryption key.
    :return: Decrypted password.
    """
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password.encode())
    return decrypted_password.decode()

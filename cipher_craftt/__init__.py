# cipher_craft/__init__.py

# Expose selected functions and classes at the package level
from .generator import generate_password
from .passphrase_generator import generate_passphrase
from .strength_checker import check_strength
from .expiry_checker import check_password_expiry, record_password_creation
from .entropy_calculator import calculate_entropy
from .obfuscator import obfuscate_password
from .breach_checker import check_breach
from .secure_sharing import generate_key, encrypt_password, decrypt_password
from .password_history import add_password_to_history, check_password_in_history, limit_password_history

__all__ = [
    "generate_password",
    "generate_passphrase",
    "check_strength",
    "check_password_expiry",
    "record_password_creation",
    "calculate_entropy",
    "obfuscate_password",
    "check_breach",
    "generate_key",
    "encrypt_password",
    "decrypt_password",
    "add_password_to_history",
    "check_password_in_history",
    "limit_password_history",
]

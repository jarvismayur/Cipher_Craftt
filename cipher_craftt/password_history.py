import hashlib
import json
import os
from datetime import datetime, timedelta

HISTORY_FILE = os.path.expanduser("~/.ciphercraft_password_history.json")

def load_password_history():
    """
    Load the password history from a JSON file.
    :return: A dictionary with hashed passwords and their creation dates.
    """
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_password_history(history):
    """
    Save the password history to a JSON file.
    :param history: A dictionary with hashed passwords and their creation dates.
    """
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=4)

def hash_password(password):
    """
    Hash a password using SHA-256.
    :param password: The password to hash.
    :return: The hashed password.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def add_password_to_history(password):
    """
    Add a hashed password with its creation date to the history file.
    :param password: The password to hash and add to history.
    """
    history = load_password_history()
    hashed_password = hash_password(password)
    creation_date = datetime.now().isoformat()
    history[hashed_password] = creation_date
    save_password_history(history)

def check_password_in_history(password):
    """
    Check if the given password is in the history.
    :param password: The password to check.
    :return: True if the password is in the history, False otherwise.
    """
    history = load_password_history()
    hashed_password = hash_password(password)
    return hashed_password in history

def check_password_expiry(password, days=90):
    """
    Check if the password has expired based on the number of days.
    :param password: The password to check.
    :param days: The number of days before a password expires.
    :return: A message indicating whether the password is expired or still valid.
    """
    history = load_password_history()
    hashed_password = hash_password(password)
    creation_date_str = history.get(hashed_password)
    if creation_date_str:
        creation_date = datetime.fromisoformat(creation_date_str)
        expiry_date = creation_date + timedelta(days=days)
        if datetime.now() > expiry_date:
            return f"Password has expired. Please update it."
        else:
            return f"Password is still valid. Expires on {expiry_date.strftime('%Y-%m-%d')}."
    else:
        return "Password not found in history."

def record_password_creation(password):
    """
    Record the creation date of a new password.
    :param password: The password to record.
    """
    add_password_to_history(password)

def limit_password_history(max_history=5):
    """
    Limit the number of stored passwords to avoid indefinite growth.
    :param max_history: Maximum number of passwords to store.
    """
    history = load_password_history()
    if len(history) > max_history:
        # Keep only the most recent `max_history` entries
        sorted_history = sorted(history.items(), key=lambda x: x[1], reverse=True)
        trimmed_history = dict(sorted_history[:max_history])
        save_password_history(trimmed_history)

import json
import os
from datetime import datetime, timedelta

PASSWORD_HISTORY_FILE = 'password_history.json'

def load_password_history():
    """Load the password history from a JSON file."""
    if os.path.exists(PASSWORD_HISTORY_FILE):
        with open(PASSWORD_HISTORY_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_password_history(history):
    """Save the password history to a JSON file."""
    with open(PASSWORD_HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=4)

def add_password_to_history(password, creation_date):
    """Add a new password to the history."""
    history = load_password_history()
    history[password] = creation_date.isoformat()
    save_password_history(history)

def check_password_expiry(password, days=90):
    """Check if the password has expired based on the number of days."""
    history = load_password_history()
    creation_date_str = history.get(password)
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
    """Record the creation date of a new password."""
    creation_date = datetime.now()
    add_password_to_history(password, creation_date)

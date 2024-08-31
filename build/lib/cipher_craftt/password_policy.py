import string
import random

class PasswordPolicyError(Exception):
    """Custom exception for password policy violations."""
    pass

def validate_password_policy(password, min_upper=0, min_lower=0, min_digits=0, min_special=0):
    """
    Validate the password against the custom policy.
    :param password: The password to validate.
    :param min_upper: Minimum number of uppercase letters.
    :param min_lower: Minimum number of lowercase letters.
    :param min_digits: Minimum number of digits.
    :param min_special: Minimum number of special characters.
    :return: None if the password meets the policy, otherwise raise PasswordPolicyError.
    """
    if sum(1 for c in password if c.isupper()) < min_upper:
        raise PasswordPolicyError(f"Password must contain at least {min_upper} uppercase letters.")
    if sum(1 for c in password if c.islower()) < min_lower:
        raise PasswordPolicyError(f"Password must contain at least {min_lower} lowercase letters.")
    if sum(1 for c in password if c.isdigit()) < min_digits:
        raise PasswordPolicyError(f"Password must contain at least {min_digits} digits.")
    if sum(1 for c in password if c in string.punctuation) < min_special:
        raise PasswordPolicyError(f"Password must contain at least {min_special} special characters.")

def generate_password_with_policy(length, min_upper, min_lower, min_digits, min_special):
    """
    Generate a password that adheres to the custom policy.
    :param length: Length of the password.
    :param min_upper: Minimum number of uppercase letters.
    :param min_lower: Minimum number of lowercase letters.
    :param min_digits: Minimum number of digits.
    :param min_special: Minimum number of special characters.
    :return: A password that meets the policy.
    """
    if length < (min_upper + min_lower + min_digits + min_special):
        raise PasswordPolicyError("Password length is too short for the specified policy.")

    # Generate the required number of each type
    password = []
    password += random.choices(string.ascii_uppercase, k=min_upper)
    password += random.choices(string.ascii_lowercase, k=min_lower)
    password += random.choices(string.digits, k=min_digits)
    password += random.choices(string.punctuation, k=min_special)

    # Fill the rest of the password with random choices from all characters
    remaining_length = length - len(password)
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password += random.choices(all_characters, k=remaining_length)

    # Shuffle to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

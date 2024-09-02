import random
import string
import hashlib

def generate_salt(passphrase):
    """
    Generate a salt based on a passphrase.
    :param passphrase: The passphrase to generate the salt.
    :return: The generated salt.
    """
    hash_object = hashlib.sha256(passphrase.encode())
    return hash_object.hexdigest()[:16]  # Use the first 16 characters of the hash as the salt

def load_common_words(filename='common_words.txt'):
    """
    Load common words from a file.
    :param filename: The path to the file containing common words.
    :return: A set of common words.
    """
    with open(filename, 'r') as file:
        return set(line.strip().lower() for line in file)

def is_dictionary_word(password, common_words):
    """
    Check if the password contains common dictionary words.
    :param password: The password to check.
    :param common_words: Set of common dictionary words.
    :return: True if the password contains common words, False otherwise.
    """
    return any(word in password.lower() for word in common_words)

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True,
                      exclude_chars=None, min_digits=0, salting=False, min_special=0, personalization=None,
                      common_words_file='common_words.txt'):
    """
    Generate a random password with constraints and optional salting, and ensure it is resistant to dictionary attacks.
    :param length: Total length of the generated password.
    :param use_upper: Include uppercase letters.
    :param use_lower: Include lowercase letters.
    :param use_digits: Include digits.
    :param use_special: Include special characters.
    :param exclude_chars: Characters to exclude from the password.
    :param min_digits: Minimum number of digits required in the password.
    :param salting: If True, apply passphrase-based salting to the password.
    :param min_special: Minimum number of special characters required in the password.
    :param personalization: Characters to personalize the password with.
    :param common_words_file: File containing common dictionary words for attack resistance.
    :return: The generated password or salted passphrase.
    """
    available_chars = ''
    if use_upper:
        available_chars += string.ascii_uppercase
    if use_lower:
        available_chars += string.ascii_lowercase
    if use_digits:
        available_chars += string.digits
    if use_special:
        available_chars += string.punctuation

    if exclude_chars:
        available_chars = ''.join(ch for ch in available_chars if ch not in exclude_chars)

    if len(available_chars) == 0:
        raise ValueError("No characters available to generate the password.")

    common_words = load_common_words(common_words_file)
    password = []

    while True:
        # Ensure minimum number of digits
        for _ in range(min_digits):
            password.append(random.choice(string.digits))

        # Ensure minimum number of special characters
        for _ in range(min_special):
            password.append(random.choice(string.punctuation))

        # Generate the rest of the password
        while len(password) < length:
            password.append(random.choice(available_chars))

        # Incorporate personalization
        if personalization:
            personalization_chars = ''.join(filter(lambda c: c in available_chars, personalization))
            if personalization_chars:
                password[:len(personalization_chars)] = list(personalization_chars)

        # Shuffle to avoid predictable patterns
        random.shuffle(password)

        # Join list to form the final password
        passphrase = ''.join(password)

        # Check if password is dictionary attack-resistant
        if not is_dictionary_word(passphrase, common_words):
            break

    # Apply salting if requested
    if salting:
        passphrase = generate_salt(passphrase)

    return passphrase

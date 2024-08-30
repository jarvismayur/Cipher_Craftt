import random

def generate_passphrase(wordlist, num_words=4, separator='-'):
    """Generate a passphrase from a given wordlist.

    Args:
        wordlist (list): List of words to use for generating the passphrase.
        num_words (int): Number of words in the passphrase.
        separator (str): Separator between words.

    Returns:
        str: Generated passphrase.
    """
    if len(wordlist) < num_words:
        raise ValueError("Wordlist does not contain enough words.")
    
    passphrase = separator.join(random.choice(wordlist) for _ in range(num_words))
    return passphrase

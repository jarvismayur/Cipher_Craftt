import random
import os

# Default language mappings (you should have these files within your package)
DEFAULT_WORDLISTS = {
    'ar': 'ar.txt',
    'cs': 'cs.txt',
    'da': 'da.txt',
    'de': 'de.txt',
    'en': 'en.txt',
    'es': 'es.txt',
    'fr': 'fr.txt',
    'he': 'he.txt',
    'hr': 'hr.txt',
    'it': 'it.txt',
    'ka': 'ka.txt',
    'nl': 'nl.txt',
    'no': 'no.txt',
    'pl': 'pl.txt',
    'pt': 'pt.txt',
    'ru': 'ru.txt',
    'sr': 'sr.txt',
    'sv': 'sv.txt',
    'tr': 'tr.txt',
    'uk': 'uk.txt',
    # Add more languages as needed
}

def load_default_wordlist(language='en'):
    """Load the default wordlist for the specified language.

    Args:
        language (str): Language code (e.g., 'en', 'es', 'fr').

    Returns:
        list: List of words from the default wordlist.
    """
    filename = DEFAULT_WORDLISTS.get(language, DEFAULT_WORDLISTS['en'])
    filepath = os.path.join(os.path.dirname(__file__), 'wordlist', 'languages', filename)
    
    with open(filepath, 'r') as file:
        wordlist = [line.strip() for line in file]
    
    return wordlist

def generate_passphrase(wordlist=None, num_words=4, separator='-', language='en'):
    """Generate a passphrase from a given or default wordlist.

    Args:
        wordlist (list): List of words to use for generating the passphrase.
        num_words (int): Number of words in the passphrase.
        separator (str): Separator between words.
        language (str): Language code for the default wordlist (if no wordlist is provided).

    Returns:
        str: Generated passphrase.
    """
    if wordlist:
        with open(wordlist) as f:
                wordlist = [line.strip() for line in f]


    if wordlist is None:
        wordlist = load_default_wordlist(language)
    
    if len(wordlist) < num_words:
        raise ValueError("Wordlist does not contain enough words.")
    
    passphrase = separator.join(random.choice(wordlist) for _ in range(num_words))
    return passphrase
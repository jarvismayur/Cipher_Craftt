VOWELS = "AEIOUYaeiouy"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz"

def pronounce_character(char):
    """Return a phonetic representation of a character."""
    if char in VOWELS:
        return char.upper()  # Keep vowels as they are, just uppercase for clarity
    elif char in CONSONANTS:
        return f"{char.upper()} as in {char.upper()}"  # E.g., B as in Bravo
    else:
        return char  # Return digits and special characters as is

def generate_pronunciation(password):
    """Generate a pronunciation guide for a given password."""
    pronunciation = [pronounce_character(char) for char in password]
    return " ".join(pronunciation)


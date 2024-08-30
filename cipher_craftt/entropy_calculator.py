import math

def calculate_entropy(password):
    """Calculate the entropy of a given password."""
    
    # Define the pool size based on the characters used in the password
    pool_size = 0
    if any(c.islower() for c in password):
        pool_size += 26  # 26 lowercase letters
    if any(c.isupper() for c in password):
        pool_size += 26  # 26 uppercase letters
    if any(c.isdigit() for c in password):
        pool_size += 10  # 10 digits
    if any(c in '!@#$%^&*()-_=+[]{}|;:,.<>?/`~' for c in password):
        pool_size += 32  # Special characters (adjust this list as needed)
    
    # Calculate entropy
    entropy = len(password) * math.log2(pool_size)
    
    return entropy

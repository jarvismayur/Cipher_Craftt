import requests
import hashlib

def check_breach(password):
    """
    Check if the given password has been involved in a data breach using the Have I Been Pwned API.
    
    :param password: The password to check.
    :return: Number of times the password has been breached, or None if not found.
    """
    # Hash the password using SHA-1
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    
    # First 5 characters for K-Anonymity search
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]
    
    # Query the Have I Been Pwned API
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching data from Have I Been Pwned API: {response.status_code}")
    
    # Check if the suffix is in the response
    breaches = (line.split(':') for line in response.text.splitlines())
    for hash_suffix, count in breaches:
        if hash_suffix == suffix:
            return int(count)
    
    return None  # Password not found in any breaches

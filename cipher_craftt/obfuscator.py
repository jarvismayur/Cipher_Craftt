import random

def obfuscate_password(password, level=1):
    """
    Obfuscate the given password to make it more secure.
    
    :param password: The original password to be obfuscated.
    :param level: The level of obfuscation (1, 2, or 3).
    :return: Obfuscated password.
    """
    obfuscation_methods = {
        1: replace_characters,
        2: reverse_password,
        3: add_random_noise,
    }
    
    obfuscated_password = password
    for i in range(1, level + 1):
        obfuscated_password = obfuscation_methods.get(i, lambda x: x)(obfuscated_password)
    
    return obfuscated_password

def replace_characters(password):
    replacements = {
        'a': '@',
        'i': '1',
        'e': '3',
        'o': '0',
        's': '$',
        'g': '9',
        't': '7',
        'l': '1',
    }
    return ''.join(replacements.get(c, c) for c in password)

def reverse_password(password):
    return password[::-1]

def add_random_noise(password):
    noise_chars = '!@#$%^&*()-_=+[]{}'
    noisy_password = list(password)
    for _ in range(len(password) // 2):
        pos = random.randint(0, len(noisy_password))
        noisy_password.insert(pos, random.choice(noise_chars))
    return ''.join(noisy_password)

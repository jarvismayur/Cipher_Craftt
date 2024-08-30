def check_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in '!@#$%^&*()-_=+[]{}|;:,.<>/?' for char in password)

    strength = 0
    if length >= 8:
        strength += 1
    if has_upper and has_lower:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1

    if strength <= 1:
        return "Weak"
    elif strength == 2:
        return "Moderate"
    else:
        return "Strong"



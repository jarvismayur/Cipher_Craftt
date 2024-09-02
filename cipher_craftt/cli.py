import argparse
from .generator import generate_password
from .strength_checker import check_strength
from .passphrase_generator import generate_passphrase
from .entropy_calculator import calculate_entropy
from .obfuscator import obfuscate_password
from .breach_checker import check_breach
from .secure_sharing import generate_key, encrypt_password, decrypt_password
from .password_history import add_password_to_history,check_password_expiry,record_password_creation, limit_password_history, check_password_in_history, limit_password_history  # Import history functions
from .pronunciation_guide import generate_pronunciation

def main():
    parser = argparse.ArgumentParser(description="Cipher-Craftt - Password and Passphrase Generator")
    parser.add_argument("--generate-password", action="store_true", help="Generate a random password")
    parser.add_argument("--generate-passphrase", action="store_true", help="Generate a passphrase")
    parser.add_argument("--calculate-entropy", type=str, help="Return the entropy of your password")
    parser.add_argument("--check-expiry", type=str, help="Check if a password has expired")
    parser.add_argument("--record-password", type=str, help="Record the creation date of a new password")
    parser.add_argument("--check-breach", type=str, help="Check if the password has been involved in a data breach")
    parser.add_argument("--share-password", type=str, help="Encrypt and share a password securely")
    parser.add_argument("--decrypt-password", nargs=2, help="Decrypt a shared password")
    parser.add_argument("--check-history", type=str, help="Check if the password has been used before")
    parser.add_argument("--max-history", type=int, help="Limit the number of stored passwords in history")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password")
    parser.add_argument("-u", "--no-upper", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("-lo", "--no-lower", action="store_true", help="Exclude lowercase letters")
    parser.add_argument("-d", "--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("-s", "--no-special", action="store_true", help="Exclude special characters")
    parser.add_argument("--num-words", type=int, default=4, help="Number of words in the passphrase")
    parser.add_argument("--wordlist", type=str, help="Path to a file containing words for passphrase generation")
    parser.add_argument("--separator", type=str, default='-', help="Separator between words in the passphrase")
    parser.add_argument("--expiry-days", type=int, default=90, help="Number of days before a password expires")
    parser.add_argument("--obfuscate", type=int, choices=[1, 2, 3], help="Obfuscate the password (level 1, 2, or 3)")
    parser.add_argument("--pronunciation-guide", type=str, help="Generate a pronunciation guide for a password")

    args = parser.parse_args()

    if args.generate_password:
        if args.check_history and check_password_in_history(args.check_history):
            print("Error: The password has been used before. Please choose a different one.")
            return

        password = generate_password(
            length=args.length,
            use_upper=not args.no_upper,
            use_lower=not args.no_lower,
            use_digits=not args.no_digits,
            use_special=not args.no_special
        )

        # Apply obfuscation if requested
        if args.obfuscate:
            password = obfuscate_password(password, level=args.obfuscate)

        print(f"Generated Password: {password}")
        print(f"Password Strength: {check_strength(password)}")

        # Add the password to history
        add_password_to_history(password)

        # Limit password history if specified
        if args.max_history:
            limit_password_history(max_history=args.max_history)

    if args.generate_passphrase:
        if not args.wordlist:
            print("Error: --wordlist argument is required for passphrase generation.")
            return
        
        with open(args.wordlist) as f:
            wordlist = [line.strip() for line in f]
        
        passphrase = generate_passphrase(
            wordlist=wordlist,
            num_words=args.num_words,
            separator=args.separator
        )

        # Apply obfuscation if requested
        if args.obfuscate:
            passphrase = obfuscate_password(passphrase, level=args.obfuscate)

        print(f"Generated Passphrase: {passphrase}")

        # Add the passphrase to history
        add_password_to_history(passphrase)

        # Limit passphrase history if specified
        if args.max_history:
            limit_password_history(max_history=args.max_history)

    if args.check_expiry:
        result = check_password_expiry(args.check_expiry, days=args.expiry_days)
        print(result)

    if args.record_password:
        record_password_creation(args.record_password)
        print(f"Password recorded with creation date.")
    
    if args.calculate_entropy:
        result = calculate_entropy(password=args.calculate_entropy)
        print(f'Entropy of your given password {args.calculate_entropy} is  {result}')
    
    # Add the data breach checker feature
    if args.check_breach:
        breach_count = check_breach(args.check_breach)
        if breach_count:
            print(f"The password '{args.check_breach}' has been breached {breach_count} times.")
        else:
            print(f"The password '{args.check_breach}' has not been found in any known data breaches.")

    # Secure Password Sharing
    if args.share_password:
        key = generate_key()
        encrypted_password = encrypt_password(args.share_password, key)
        print(f"Encrypted Password: {encrypted_password}")
        print(f"Share this key securely with the recipient: {key.decode()}")

    if args.decrypt_password:
        encrypted_password, key = args.decrypt_password
        decrypted_password = decrypt_password(encrypted_password, key.encode())
        print(f"Decrypted Password: {decrypted_password}")

    # Check if a password is in history
    if args.check_history:
        if check_password_in_history(args.check_history):
            print("The password has been used before.")
        else:
            print("The password has not been used before.")

    # Limit the number of stored passwords in history
    if args.max_history:
        limit_password_history(max_history=args.max_history)
    
    if args.pronunciation_guide:
        guide = generate_pronunciation(args.pronunciation_guide)
        print(f"Pronunciation Guide for '{args.pronunciation_guide}': {guide}")

if __name__ == "__main__":
    main()

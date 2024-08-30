import argparse
from .generator import generate_password
from .strength_checker import check_strength
from .passphrase_generator import generate_passphrase
from .expiry_checker import check_password_expiry, record_password_creation

def main():
    parser = argparse.ArgumentParser(description="Cipher-Craftt - Password and Passphrase Generator")
    parser.add_argument("--generate-password", action="store_true", help="Generate a random password")
    parser.add_argument("--generate-passphrase", action="store_true", help="Generate a passphrase")
    parser.add_argument("--check-expiry", type=str, help="Check if a password has expired")
    parser.add_argument("--record-password", type=str, help="Record the creation date of a new password")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password")
    parser.add_argument("-u", "--no-upper", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("-lo", "--no-lower", action="store_true", help="Exclude lowercase letters")
    parser.add_argument("-d", "--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("-s", "--no-special", action="store_true", help="Exclude special characters")
    parser.add_argument("--num-words", type=int, default=4, help="Number of words in the passphrase")
    parser.add_argument("--wordlist", type=str, help="Path to a file containing words for passphrase generation")
    parser.add_argument("--separator", type=str, default='-', help="Separator between words in the passphrase")
    parser.add_argument("--expiry-days", type=int, default=90, help="Number of days before a password expires")

    args = parser.parse_args()

    if args.generate_password:
        password = generate_password(
            length=args.length,
            use_upper=not args.no_upper,
            use_lower=not args.no_lower,
            use_digits=not args.no_digits,
            use_special=not args.no_special
        )
        print(f"Generated Password: {password}")
        print(f"Password Strength: {check_strength(password)}")

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
        print(f"Generated Passphrase: {passphrase}")

    if args.check_expiry:
        result = check_password_expiry(args.check_expiry, days=args.expiry_days)
        print(result)

    if args.record_password:
        record_password_creation(args.record_password)
        print(f"Password recorded with creation date.")

if __name__ == "__main__":
    main()

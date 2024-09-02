# CipherCraft
CipherCraft is a versatile and secure password generator designed to help you create strong, memorable passwords with ease. With a range of customizable features and unique tools, CipherCraft ensures your passwords are not only secure but also tailored to your needs.

 ## Key Features
- **Passphrase Generation**: Generate easy-to-remember passphrases from a customizable wordlist, perfect for both security and memorability.
- **Password Expiry Checker**: Track the age of your passwords and receive reminders to update them regularly to maintain security.
- **Entropy Calculation**: Evaluate the strength of your passwords with entropy metrics, providing a numeric value for better security assessment.
- **Customizable Wordlists**: Use your own wordlists or choose from various pre-defined ones to create unique passphrases.
- **Password Obfuscation**: Enhance security by obfuscating your passphrases with common letter-to-symbol substitutions.
- **Data Breach Checker**: Check if your passwords have been compromised in data breaches to avoid using vulnerable passwords.
- **Secure Password Sharing**: Share passwords securely with time-limited, expiring links to ensure safe transmission.
- **Password History Management**: Maintain a secure history of generated passwords to prevent reuse and enhance security.
- **Custom Password Policies**: Define and apply custom password policies to ensure compliance with specific security requirements. 
- **Password Pronunciation Guide**: Generate passwords that are easy to pronounce, making them simpler to share verbally.
  
## Installation
You can install CipherCraft via PyPI:

```bash
pip install cipher-craftt
```

## Updating the Package
To ensure you have the latest features and improvements, you can easily update the CipherCraft package using pip. Open your command line interface and run the following command:

```bash
pip install --upgrade cipher-craftt
```
This command will update your CipherCraft package to the latest version available on [PyPI](https://pypi.org/project/cipher-craftt/).

## Basic Usage
To use the CLI, run the following command:

```bash
python cli.py [options]
```
## Available Options
1. Password Generation
- `--generate-password`: Generates a random password.

```bash
python cli.py --generate-password
```
Options:

- `-l, --length`: Length of the generated password (default: 12).
- `-u, --no-upper`: Exclude uppercase letters.
- `-lo, --no-lower`: Exclude lowercase letters.
- `-d, --no-digits`: Exclude digits.
- `-s, --no-special`: Exclude special characters.
- `--exclude-chars`: Characters to exclude from the password.
- `--min-digits`: Minimum number of digits required (default: 0).
- `--min-special`: Minimum number of special characters required (default: 0).
- `--salting`: Apply passphrase-based salting to the password.
- `--personalization`: Personalized input to include in the password.
- `--file_path`: Path to a file containing common words (e.g., common_words.txt).
- `--obfuscate`: Apply obfuscation to the password (level 1, 2, or 3).

2. Passphrase Generation
-  `--generate-passphrase`: Generates a passphrase based on a word list.

```bash
python cli.py --generate-passphrase --wordlist path/to/wordlist.txt
```
Options:

- `--num-words`: Number of words in the passphrase (default: 4).
- `--separator`: Separator between words in the passphrase (default: '-').
- `--obfuscate`: Apply obfuscation to the passphrase (level 1, 2, or 3).

3. Password Entropy
- `--calculate-entropy`: Calculate the entropy of a given password.

```bash
python cli.py --calculate-entropy your_password
```
4. Password Expiry Check
- `--check-expiry`: Check if a password has expired.

```bash
python cli.py --check-expiry your_password
```
Options:

- `--expiry-days`: Number of days before a password expires (default: 90).
5. Password History Management
- `--record-password`: Record the creation date of a new password.

```bash
python cli.py --record-password your_password
```
- `--check-history`: Check if a password has been used before.

```bash
python cli.py --check-history your_password
```
- `--max-history`: Limit the number of stored passwords in history.

```bash
python cli.py --max-history 100
```
6. Data Breach Check
- `--check-breach`: Check if a password has been involved in a data breach.

```bash
python cli.py --check-breach your_password
```
7. Secure Password Sharing
- `--share-password`: Encrypt and share a password securely.

```bash
python cli.py --share-password your_password
```
- `--decrypt-password`: Decrypt a shared password.

```bash
python cli.py --decrypt-password encrypted_password key
```
8. Pronunciation Guide
- `--pronunciation-guide`: Generate a pronunciation guide for a password.

```bash
python cli.py --pronunciation-guide your_password
```
9. Password Strength Check
- `--check-strength`: Check the strength of the given password.

```bash
python cli.py --check-strength your_password
```
10. Mnemonic Password Generation
- `--generate-mnemonic`: Generate a mnemonic-based password.

```bash
python cli.py --generate-mnemonic --wordlist path/to/wordlist.txt
```
Options:

- `--num-words`: Number of words in the mnemonic password (default: 4).
- `--separator`: Separator between words in the mnemonic password (default: '-').
- `--length`: Length of the mnemonic password.
11. Context-Aware Password Generation
- `--context`: Specify the context for the password generation (e.g., finance, social, work).

```bash
python cli.py --generate-password --context finance
```
12. TOTP (Time-based One-Time Password)
- `--generate-totp`: Generate a TOTP using the provided secret.

```bash
python cli.py --generate-totp your_secret
```
- `--verify-totp`: Verify a TOTP using the provided secret and OTP.

```bash
python cli.py --verify-totp your_secret your_otp
```
## Examples
- Generate a password with specific constraints:

```bash
python cli.py --generate-password -l 16 --no-special --min-digits 2 --personalization "MySecret!"
```
- Generate a passphrase with a custom word list and separator:

```bash
python cli.py --generate-passphrase --wordlist path/to/wordlist.txt --separator "_"
```
- Check if a password has expired:

```bash
python cli.py --check-expiry your_password --expiry-days 60
```
- Encrypt and share a password securely:

```bash
python cli.py --share-password your_password
```
- Generate a TOTP:

```bash
python cli.py --generate-totp your_secret
```


## License
CipherCraft is licensed under the MIT [License](https://github.com/jarvismayur/Cipher_Craftt/blob/main/LICENSE). See the LICENSE file for details.

## Contact and Issues
If you have any questions, suggestions, or encounter issues, please feel free to [open an issue](https://github.com/yourusername/cipher-craftt/issues) on the GitHub repository. For direct communication, you can reach out to Mayur Tembhare via [email](mailto:tembharemayur@gmail.com) .

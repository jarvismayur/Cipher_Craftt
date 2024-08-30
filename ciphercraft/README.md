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
## Usage
- To generate a password or passphrase, use the command-line interface:

```bash
 cipher_craftt --generate-password --length 16 --no-digits --obfuscate
```
- To generate a passphrase:

```bash
cipher_craftt  --generate-passphrase --wordlist path/to/wordlist.txt --num-words 5 --separator '-'
```

- To record the creation date of a new password:

```bash
cipher_craftt  --record-password your-new-password
```

- To check password expiry:

```bash
cipher_craftt  --check-expiry your-password
```



## License
CipherCraft is licensed under the MIT License. See the LICENSE file for details.

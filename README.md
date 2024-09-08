# CipherCraft
CipherCraft is a versatile and secure password generator designed to help you create strong, memorable passwords with ease. With a range of customizable features and unique tools, CipherCraft ensures your passwords are not only secure but also tailored to your needs.

- For detailed documentation and usage instructions, please visit our [Read the Docs page](https://cipher-craftt.readthedocs.io).
- You can also explore the source code and contribute to the project on our [GitHub repository](https://github.com/jarvismayur/cipher-craftt).

## Features
CipherCraft offers a wide range of features to help you securely generate, manage, and share passwords and passphrases:

1. **Password and Passphrase Generation**
- **Random Password Generator**: Generate strong, random passwords with customizable options such as length, inclusion/exclusion of uppercase letters, lowercase letters, digits, and special characters.
- **Context-Aware Password Generator**: Generate passwords tailored to specific contexts, such as finance, social media, or work environments.
- **Mnemonic Password Generator**: Create mnemonic-based passwords using a custom wordlist, making them easier to remember.
- **Passphrase Generator**: Generate secure passphrases composed of random words from a user-defined wordlist, with customizable separators.
2. **Password Strength and Entropy**
- **Password Strength Checker**: Evaluate the strength of a given password to ensure its robustness against attacks.
- **Entropy Calculator**: Calculate the entropy of a password, giving you an indication of its unpredictability and security level.
3. **Password History Management**
- **Password History Checker**: Verify if a password has been used before, helping to prevent reuse of old passwords.
- **Password Expiry Checker**: Check if a password has expired based on a specified number of days.
- **Password Creation Recorder**: Record the creation date of a new password for tracking and expiry purposes.
- **Limit Password History**: Set a limit on the number of stored passwords in history to maintain a clean and secure password management process.
4. **Obfuscation and Pronunciation Guide**
- **Password Obfuscator**: Obfuscate your password to different levels (1, 2, or 3) for enhanced security.
- **Pronunciation Guide**: Generate a pronunciation guide for a given password to make it easier to recall.
5. **Secure Sharing and Breach Detection**
- **Secure Password Sharing**: Encrypt and securely share passwords using a generated key.
- **Password Decryption**: Decrypt a shared password using the provided key.
- **Data Breach Checker**: Check if your password has been involved in any known data breaches, ensuring its safety.
6. **Time-Based One-Time Password (TOTP)**
- **TOTP Generation**: Generate a Time-Based One-Time Password (TOTP) using a provided secret, for use in two-factor authentication.
- **TOTP Verification**: Verify the validity of a TOTP using the provided secret and OTP.
7. **Advanced Customization**
- **Salting**: Apply passphrase-based salting to generated passwords for added security.
- **Personalization**: Incorporate personalized inputs (e.g., names, favorite numbers) into password generation for more tailored security.
- **Common Words Filtering**: Exclude common words from the password using a custom dictionary file to enhance password security.

  
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
cipher-craftt [options]
```
## Available Options
### 1. **Password Generation**
- `--generate-password`: Generates a random password.

```bash
cipher-craftt --generate-password
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

### 2. **Passphrase Generation**
-  `--generate-passphrase`: Generates a passphrase based on a word list.

```bash
cipher-craftt --generate-passphrase 
```
Options:

- `--num-words`: Number of words in the passphrase (default: 4).
- `--separator`: Separator between words in the passphrase (default: '-').
- `--obfuscate`: Apply obfuscation to the passphrase (level 1, 2, or 3).
- `--wordlist` : Your custom wordlist can also be used.
- `--language`: Multiple language wordlist available.
  - `da` : Danish
  - `de` : German
  - `en` : Enlish ( default )
  - `es` : Spanish 
  - `fr` : French
  - `it` : Italian
  - `nl` : Dutch 
  - `no` : Norwegian 
  - `pl` : Polish 
  - `pt` : Portuguese 
  - `sv` : Swedish 
  - `tr` : Turkish 

### 3. **Password Entropy**
- `--calculate-entropy`: Calculate the entropy of a given password.

```bash
cipher-craftt --calculate-entropy your_password
```
### 4. **Password Expiry Check**
- `--check-expiry`: Check if a password has expired.

```bash
cipher-craftt --check-expiry your_password
```
Options:

- `--expiry-days`: Number of days before a password expires (default: 90).
### 5. **Password History Management**
- `--record-password`: Record the creation date of a new password.

```bash
cipher-craftt --record-password your_password
```
- `--check-history`: Check if a password has been used before.

```bash
cipher-craftt --check-history your_password
```
- `--max-history`: Limit the number of stored passwords in history.

```bash
cipher-craftt --max-history 100
```
### 6. **Data Breach Check**
- `--check-breach`: Check if a password has been involved in a data breach.

```bash
cipher-craftt --check-breach your_password
```
### 7. **Secure Password Sharing**
- `--share-password`: Encrypt and share a password securely.

```bash
cipher-craftt --share-password your_password
```
- `--decrypt-password`: Decrypt a shared password.

```bash
cipher-craftt --decrypt-password encrypted_password key
```
### 8. **Pronunciation Guide**
- `--pronunciation-guide`: Generate a pronunciation guide for a password.

```bash
cipher-craftt --pronunciation-guide your_password
```
### 9. **Password Strength Check**
- `--check-strength`: Check the strength of the given password.

```bash
cipher-craftt --check-strength your_password
```
### 10. **Mnemonic Password Generation**
- `--generate-mnemonic`: Generate a mnemonic-based password.

```bash
cipher-craftt --generate-mnemonic --wordlist path/to/wordlist.txt
```
Options:

- `--num-words`: Number of words in the mnemonic password (default: 4).
- `--separator`: Separator between words in the mnemonic password (default: '-').
- `--length`: Length of the mnemonic password.
### 11. **Context-Aware Password Generation**
- `--context`: Specify the context for the password generation (e.g., finance, social, work).

```bash
cipher-craftt --generate-password --context finance
```
### 12. TOTP (Time-based One-Time Password)
- `--generate-totp`: Generate a TOTP using the provided secret.

```bash
cipher-craftt --generate-totp your_secret
```
- `--verify-totp`: Verify a TOTP using the provided secret and OTP.

```bash
cipher-craftt --verify-totp your_secret your_otp
```
## Examples
- Generate a password with specific constraints:

```bash
cipher-craftt --generate-password -l 16 --no-special --min-digits 2 --personalization "MySecret!"
```
- Generate a passphrase with a custom word list and separator:

```bash
cipher-craftt --generate-passphrase --wordlist path/to/wordlist.txt --separator "_"
```
- Check if a password has expired:

```bash
cipher-craftt --check-expiry your_password --expiry-days 60
```
- Encrypt and share a password securely:

```bash
cipher-craftt --share-password your_password
```
- Generate a TOTP:

```bash
cipher-craftt --generate-totp your_secret
```

## Use Cases and Real-Life Implications of CipherCraft
1. **Personal Password Management**

- **Use Case**: A user needs to create a strong and memorable password for various online accounts, such as banking, social media, or email.
- **Real-Life Implication**: With CipherCraft, users can generate secure passwords that meet specific requirements, reducing the risk of account breaches due to weak or reused passwords. The tool also allows for personalized input, making passwords easier to remember.
2. **Corporate Security Compliance**

- **Use Case**: An organization requires its employees to regularly update their passwords and ensure they are strong enough to meet security policies.
- **Real-Life Implication**: CipherCraft can generate complex passwords with specific constraints, such as including a minimum number of digits or special characters. It also tracks password expiry and ensures that employees rotate their passwords as required, helping organizations maintain compliance with security standards.
3. **Multilingual Passphrase Generation**

- **Use Case**: A user or organization in a non-English-speaking country needs to generate passphrases in their native language for easier memorization and enhanced usability.
- **Real-Life Implication**: CipherCraft supports multiple languages for passphrase generation, making it accessible and practical for users worldwide. This feature can help in creating passphrases that are both secure and culturally relevant.
4. **Data Breach Prevention**

- **Use Case**: A user wants to check if their existing passwords have been compromised in any known data breaches.
- **Real-Life Implication**: CipherCraft can check passwords against databases of known breaches, alerting users to compromised credentials and prompting them to update their passwords immediately, thereby reducing the risk of unauthorized access.
5. **Secure Password Sharing**

- **Use Case**: A team member needs to securely share a password with a colleague.
- **Real-Life Implication**: CipherCraft offers secure password sharing options, ensuring that passwords are encrypted before being sent. This reduces the risk of interception or unauthorized access during transmission.
6. Password Entropy Calculation

- **Use Case**: A cybersecurity professional needs to assess the strength of a password by calculating its entropy.
- **Real-Life Implication**: CipherCraft calculates the entropy of passwords, providing a quantifiable measure of password strength. This helps professionals and users alike to understand the robustness of their passwords against various attack vectors.
7. **Context-Aware Password Generation**

- **Use Case**: A user needs to generate a password tailored specifically for different contexts, such as financial accounts, social media, or work-related applications.
- **Real-Life Implication**: CipherCraft’s context-aware password generation ensures that passwords are optimized for their intended use, enhancing both security and usability across different platforms and scenarios.
8. **Historical Password Management**

- **Use Case**: A user wants to ensure they are not reusing old passwords or violating a maximum password history policy.
- **Real-Life Implication**: CipherCraft manages password history, allowing users to track and compare past passwords. This feature helps prevent password reuse and ensures compliance with security policies that restrict password repetition.


## License
CipherCraft is licensed under the MIT [License](https://github.com/jarvismayur/Cipher_Craftt/blob/main/LICENSE). See the LICENSE file for details.

## Contact and Issues
If you have any questions, suggestions, or encounter issues, please feel free to [open an issue](https://github.com/jarvismayur/cipher_craftt/issues) on the GitHub repository. For direct communication, you can reach out to Mayur Tembhare via [email](mailto:tembharemayur@gmail.com) .

Usage
===========

To use the CLI, run the following command:

.. code-block:: bash

    cipher-craftt [options]

Available Options
-----------------

1. **Password Generation**

   - ``--generate-password``: Generates a random password.

   .. code-block:: bash

        cipher_craftt --generate-password

   Options:

   - ``-l, --length``: Length of the generated password (default: 12).
   - ``-u, --no-upper``: Exclude uppercase letters.
   - ``-lo, --no-lower``: Exclude lowercase letters.
   - ``-d, --no-digits``: Exclude digits.
   - ``-s, --no-special``: Exclude special characters.
   - ``--exclude-chars``: Characters to exclude from the password.
   - ``--min-digits``: Minimum number of digits required (default: 0).
   - ``--min-special``: Minimum number of special characters required (default: 0).
   - ``--salting``: Apply passphrase-based salting to the password.
   - ``--personalization``: Personalized input to include in the password.
   - ``--file_path``: Path to a file containing common words (e.g., common_words.txt).
   - ``--obfuscate``: Apply obfuscation to the password (level 1, 2, or 3).

2. **Passphrase Generation**

   - ``--generate-passphrase``: Generates a passphrase based on a word list.

   .. code-block:: bash

        cipher_craftt --generate-passphrase 

   Options:

   - ``--num-words``: Number of words in the passphrase (default: 4).
   - ``--separator``: Separator between words in the passphrase (default: '-').
   - ``--obfuscate``: Apply obfuscation to the passphrase (level 1, 2, or 3).
   - ``--wordlist`` : Your custom wordlist can also be used.
   - ``--language`` : Multiple language wordlist available.
     - ``da`` : Danish
     - ``de`` : German
     - ``en`` : Enlish ( default )
     - ``es`` : Spanish 
     - ``fr`` : French
     - ``it`` : Italian
     - ``nl`` : Dutch 
     - ``no`` : Norwegian 
     - ``pl`` : Polish 
     - ``pt`` : Portuguese 
     - ``sv`` : Swedish 
     - ``tr`` : Turkish 

3. **Password Entropy**

   - ``--calculate-entropy``: Calculate the entropy of a given password.

   .. code-block:: bash

        cipher_craftt --calculate-entropy your_password

4. **Password Expiry Check**

   - ``--check-expiry``: Check if a password has expired.

   .. code-block:: bash

        cipher_craftt --check-expiry your_password

   Options:

   - ``--expiry-days``: Number of days before a password expires (default: 90).

5. **Password History Management**

   - ``--record-password``: Record the creation date of a new password.

   .. code-block:: bash

        cipher_craftt --record-password your_password

   - ``--check-history``: Check if a password has been used before.

   .. code-block:: bash

        cipher_craftt --check-history your_password

   - ``--max-history``: Limit the number of stored passwords in history.

   .. code-block:: bash

        cipher_craftt --max-history 100

6. **Data Breach Check**

   - ``--check-breach``: Check if a password has been involved in a data breach.

   .. code-block:: bash

        cipher_craftt --check-breach your_password

7. **Secure Password Sharing**

   - ``--share-password``: Encrypt and share a password securely.

   .. code-block:: bash

        cipher_craftt --share-password your_password

   - ``--decrypt-password``: Decrypt a shared password.

   .. code-block:: bash

        cipher_craftt --decrypt-password encrypted_password key

8. **Pronunciation Guide**

   - ``--pronunciation-guide``: Generate a pronunciation guide for a password.

   .. code-block:: bash

        cipher_craftt --pronunciation-guide your_password

9. **Password Strength Check**

   - ``--check-strength``: Check the strength of the given password.

   .. code-block:: bash

        cipher_craftt --check-strength your_password

10. **Mnemonic Password Generation**

    - ``--generate-mnemonic``: Generate a mnemonic-based password.

    .. code-block:: bash

        cipher_craftt --generate-mnemonic --wordlist path/to/wordlist.txt

    Options:

    - ``--num-words``: Number of words in the mnemonic password (default: 4).
    - ``--separator``: Separator between words in the mnemonic password (default: '-').
    - ``--length``: Length of the mnemonic password.


11. **Context-Aware Password Generation**

    - ``--context``: Specify the context for the password generation (e.g., finance, social, work).

    .. code-block:: bash

        cipher_craftt --generate-password --context finance

Each context has its own security policy. Below is a summary of the available contexts and their respective password policies:

     .. list-table:: Context Policies
          :header-rows: 1
          :widths: 15 35 10 10 10 10 20

          * - Context
               - Description
               - Length
               - Uppercase
               - Lowercase
               - Digits
               - Special Characters
          * - finance
               - For financial services
               - 16
               - Yes
               - Yes
               - Yes
               - Yes
          * - social
               - For social media accounts
               - 10
               - Yes
               - Yes
               - Yes
               - No
          * - work
               - For work-related applications
               - 12
               - Yes
               - Yes
               - Yes
               - Yes
          * - gaming
               - For online gaming accounts
               - 8
               - No
               - Yes
               - Yes
               - No
          * - email
               - For email accounts
               - 14
               - Yes
               - Yes
               - Yes
               - Yes
          * - banking
               - For banking and financial platforms
               - 20
               - Yes
               - Yes
               - Yes
               - Yes
          * - shopping
               - For shopping platforms
               - 12
               - Yes
               - Yes
               - Yes
               - No
          * - medical
               - For healthcare services
               - 18
               - Yes
               - Yes
               - Yes
               - Yes
          * - cloud
               - For cloud storage and services
               - 16
               - Yes
               - Yes
               - Yes
               - Yes
          * - secure
               - For highly sensitive information
               - 24
               - Yes
               - Yes
               - Yes
               - Yes

12. **TOTP (Time-based One-Time Password)**

    - ``--generate-totp``: Generate a TOTP using the provided secret.

    .. code-block:: bash

        cipher_craftt --generate-totp your_secret

    - ``--verify-totp``: Verify a TOTP using the provided secret and OTP.

    .. code-block:: bash

        cipher_craftt --verify-totp your_secret your_otp
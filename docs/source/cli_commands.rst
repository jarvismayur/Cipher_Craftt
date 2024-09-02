CLI Commands
============

Here are some of the available commands for CipherCraft:

- **Password Generation**:

  .. code-block:: bash

     python cli.py --generate-password

  Options:
    - `-l, --length`: Length of the generated password (default: 12).
    - `--obfuscate`: Apply obfuscation to the password (level 1, 2, or 3).
    - `--salting`: Apply passphrase-based salting to the password.

- **Passphrase Generation**:

  .. code-block:: bash

     python cli.py --generate-passphrase --wordlist path/to/wordlist.txt

  Options:
    - `--num-words`: Number of words in the passphrase (default: 4).
    - `--separator`: Separator between words in the passphrase (default: '-').
    - `--obfuscate`: Apply obfuscation to the passphrase (level 1, 2, or 3).

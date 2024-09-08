Examples
========

- Generate a password with specific constraints:

  .. code-block:: bash

        cipher-craftt --generate-password -l 16 --no-special --min-digits 2 --personalization "MySecret!"

- Generate a passphrase with a custom word list and separator:

  .. code-block:: bash

        cipher-craftt --generate-passphrase --wordlist path/to/wordlist.txt --separator "_"

- Check if a password has expired:

  .. code-block:: bash

        cipher-craftt --check-expiry your_password --expiry-days 60

- Encrypt and share a password securely:

  .. code-block:: bash

        cipher-craftt --share-password your_password

- Generate a TOTP:

  .. code-block:: bash

        cipher-craftt --generate-totp your_secret